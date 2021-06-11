impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let vec: Vec<&str> = s.trim_end().split(" ").collect();

        vec[vec.len()-1].len() as i32
    }
}
