impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut vec: Vec<&str> = s.trim().split(" ").collect();
        let mut revStr = String::new();
        
        vec.reverse();
        
        for v in vec {
            if v == "" {
                continue;
            }
            
            revStr.push_str(&v);
            revStr.push_str(" ");
        }
        
        revStr.trim_end().to_string()
    }
}
