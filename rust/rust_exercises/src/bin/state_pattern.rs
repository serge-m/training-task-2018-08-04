use rust_exercises::post_with_state::post::Post;


fn main() {
    let mut post = Post::new();

    post.add_text("start"); 
    // assert_eq!("", post.content());
    println!("{:?}", post);
    println!("{:?}", post.content());    

    post.approve(); 
    // assert_eq!("start", post.content());
    println!("{:?}", post);
    println!("{:?}", post.content());  

    post.request_review();
    // assert_eq!("", post.content());
    println!("{:?}", post);
    println!("{:?}", post.content());    

    post.approve();
    // assert_eq!("start", post.content());
    println!("{:?}", post);
    println!("{:?}", post.content());    

}
