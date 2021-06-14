impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut numMap = HashMap::new();
        let maj = nums.len()/2;
        
        for n in nums {
            let count = numMap.entry(n).or_insert(0);
            *count += 1;
            if *count > maj {
                return n;
            }
        }
        
        -1
    }
}
