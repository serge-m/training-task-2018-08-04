use crate::post_with_state::states::{State, Draft};

#[derive(Debug)]
pub struct Post {
    content: String,
    state: Option<Box<dyn State>>,
}



impl Post {
    pub fn new() -> Self {
        Self {
            content: "abc".to_string(),
            state: Some(Box::new(Draft{})),
        }
    }

    pub fn content(&self) -> &str {
        (self.content).as_str()
    }

    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }

    pub fn request_review(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.request_review());
        }
    }

    pub fn approve(&mut self) {
        self.content.push_str("approved");
    }
}
