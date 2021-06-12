impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut i = 0;
        let mut l = nums.len();

        while i < l {
            if nums[i] == val {
                nums.remove(i);
                i = i - 1;
                l = l - 1;
            }
            i = i + 1;
        }

        nums.len() as i32
    }
}
