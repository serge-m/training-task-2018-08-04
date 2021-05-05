/*
15. 3Sum
Medium
	336 ms	3.7 MB
*/

use std::collections::HashSet;
use std::collections::HashMap;


struct Solution {}

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums.clone();
        nums.sort_unstable();
        
        let mut last_pos = HashMap::new();
        for (i, val) in nums.iter().enumerate() {
            last_pos.insert(val, i);
        }
        let mut triplets = HashSet::new();
        let n = nums.len();
        for i in 0..n {
            for j in i+1..n {
                let a = &nums[i];
                let b = &nums[j];
                let c = - (a + b);

                match last_pos.get(&c) {
                    Some(&k) => {
                        if k > j {
                            triplets.insert((a,b,&nums[k]));
                        }
                    },
                    _ => {},
                }
                // println!("a{:?} i{:?} b{:?} j{:?} c{:?}", a, i, b, j, c);                  
            }
        }
        let res : Vec<Vec<i32>> = triplets.into_iter().map(|t| Solution::to_vec(t)).collect();
        res
    }


    pub fn to_vec(input: (&i32, &i32, &i32)) -> Vec<i32> {
        let mut v : Vec<i32> = Vec::new();
        v.push(*input.0);
        v.push(*input.1);
        v.push(*input.2);
        v
    }
}

fn main () {
    let s = Solution::three_sum(vec![1,2,3,-4,-5]);
    println!("{:?}", s);
}
