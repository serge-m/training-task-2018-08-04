use std::time::Duration;
use std::{fs, thread};
use std::net::{TcpListener, TcpStream};
use std::io::prelude::*;
use hello_server::ThreadPool;

fn main() {
    println!("And now we start!");
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);
    for stream in listener.incoming() {
        if let Ok(stream) = stream  {
            println!("connection established");
            pool.execute(|| {
                handle_connection(stream);
            });
        } else {
            println!("connection failed. just skipping");
        }
        
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut  buffer = [0; 1024];
    stream.read(&mut buffer).unwrap();
    let req = String::from_utf8_lossy(&buffer[..]);
    let first_line = req.split('\n').into_iter().next().unwrap();
    println!("Request {}...", first_line);
    let get = b"GET / HTTP/1.1\r\n";
    let sleep = b"GET /sleep HTTP/1.1\r\n";

    let (status_line, filename) = if buffer.starts_with(get) {
        ("HTTP/1.1 200 OK", "hello.html")
    } else if buffer.starts_with(sleep) {
        thread::sleep(Duration::from_secs(5));
        ("HTTP/1.1 OK", "hello.html")
    } else {
        ("HTTP/1.1 404 Not Found", "404.html")
    };
    let contents = fs::read_to_string(filename).unwrap();
    let response = format!(
        "{}\r\nContent-Length: {}\r\n\r\n{}",
        status_line, contents.len(), contents
    );
    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}