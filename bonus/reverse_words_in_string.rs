impl Solution {
    pub fn reverse_words(s: String) -> String {
        let vec: Vec<&str> = s.trim().split(" ").collect();
        let mut revStr = String::new();
        
        for v in vec {
            if v == "" {
                continue;
            }
            
            let word = String::from(v).chars().rev().collect::<String>();
            
            revStr.push_str(&word);
            revStr.push_str(" ");
        }
        
        revStr
    }
}
