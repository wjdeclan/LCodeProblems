class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] ret = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int c = 0;
            for (int j = 0; j < nums.length; j++) {
                if (j != i && nums[j] < nums[i]) {
                    c+=1;
                }
            }
            ret[i] = c;
        }
        return ret;
    }
}
