class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        for (int n = 0; n < nums.size(); n++)
        {
            for (int m = 0; m < nums.size(); m++)
            {
                if (nums[n] + nums[m] == target && m != n)
                {
                    ans.push_back(n);
                    ans.push_back(m);
                    return ans;
                }
            }
        }
        return ans;
    }
};
