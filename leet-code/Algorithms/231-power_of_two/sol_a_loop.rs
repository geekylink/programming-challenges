impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        for i in 0..31 {
            if n == i32::pow(2, i) {
                return true;
            }
        }
        
        false
    }
}
