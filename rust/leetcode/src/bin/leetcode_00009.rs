// 9. Palindrome Number
// Easy
struct Solution {}


impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x_string = x.to_string();
        let it1 = x_string.bytes();
        let it2 = x_string.bytes().rev();
        for (x, y) in it1.zip(it2) {
            if x != y {
                return false
            }
        }
        return true
    }
}


fn main() {
    let res = Solution::is_palindrome(-121);
    println!("{}", res);
    
}