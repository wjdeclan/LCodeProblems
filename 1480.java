class Solution {
    public int[] runningSum(int[] nums) {
        int[] runSumArray = new int[nums.length];
        int runSum = 0;
        for (int i = 0; i < nums.length; i++) {
            runSum = runSum + nums[i];
            runSumArray[i] = runSum;
        }
        return runSumArray;
    }
}
