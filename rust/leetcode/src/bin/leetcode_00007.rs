// 7. Reverse Integer
// Easy

struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut v = (x as i64).abs();
        let mut res = 0i64;

        while v != 0 {
            let dig = v % 10;
            v = v / 10;

            res = res * 10 + dig;
            // println!("dig {} v {} res {}", dig, v, res);
        }
        if x < 0 {
            res = -res;
        }
        if res > i32::MAX as i64 || res < i32::MIN as i64 {
            0
        } else {
            res as i32
        }
    }
}

fn main() {
    let s = Solution::reverse(2i32 << 31);
    println!("{:?}", s);
}
