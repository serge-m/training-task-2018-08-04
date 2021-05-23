#[derive(Debug)]
pub struct Post {
    content: String,
    state: String,
}

impl Post {
    pub fn new() -> Self {
        Self {
            content: "abc".to_string(),
            state: "draft".to_string(),
        }
    }

    pub fn content(&self) -> &str {
        (self.content).as_str()
    }

    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }

    pub fn request_review(&mut self) {
        self.state.push_str("reviewing");
    }

    pub fn approve(&mut self) {
        self.state.push_str("approved");
    }
}
