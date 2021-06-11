use std::sync::{Arc, Mutex, mpsc};
use std::thread::{self, JoinHandle};

struct Worker {
    id: usize,
    thread: Option<JoinHandle<()>>,
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Message>>>) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv().unwrap();
            match message {
                Message::NewJob(job) => {
                    println!("Worker {} got a job. executing.", id);
                    job();
                }
                Message::Terminate => {
                    println!("Got terminate signal. Exiting worker {}", id);
                    break;
                }
            }
        });
        let thread = Some(thread);
        Worker{id, thread}
    }
    
}

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Message>,
}

type Job = Box<dyn FnOnce() + Send + 'static>;

enum Message {
    NewJob(Job),
    Terminate,
}

impl ThreadPool {
    /// Create a new ThreadPool.
    /// 
    /// The size is the number of threads.
    ///
    /// # Panics
    ///
    /// The `new` function will panic if the size == 0
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);
        let mut workers = Vec::with_capacity(size);

        let (sender, receiver) = mpsc::channel();
        let receiver = Arc::new(Mutex::new(receiver));

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPool {workers, sender}
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Message::NewJob(Box::new(f));
        self.sender.send(job).unwrap();
    }
} 

impl Drop for ThreadPool {
    fn drop(&mut self) {
        println!("terminating workers...");
        for _ in &self.workers {
            self.sender.send(Message::Terminate).unwrap();
        }
        println!("Joining on workers");
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);
            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
        println!("workers terminated");
    }
}