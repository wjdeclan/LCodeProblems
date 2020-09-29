class Solution {
    public void moveZeroes(int[] nums) {
        int offset = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] == 0) {
                int temp2 = nums[nums.length - 1 - offset];
                for (int j = nums.length - 1 - offset; j > i; j--) {
                    int temp = nums[j-1];
                    nums[j-1] = temp2;
                    temp2 = temp;
                }
                nums[nums.length - 1 - offset] = 0;
                offset += 1;
            }
        }
    }
}
