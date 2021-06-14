impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashMap;
        
        let mut numMap = HashMap::new();
        
        for n in nums {
            let count = numMap.entry(n).or_insert(0);
            *count += 1;
        }
        
        for (key, count) in numMap {
            if count > 1 {
                return true;
            }
        }
        
        false
    }
}
