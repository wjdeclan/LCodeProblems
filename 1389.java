class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] target = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (index[i] == i) {
                target[i] = nums[index[i]];
            } else {
                int temp2 = target[index[i]];
                for (int j = index[i]; j < i; j++) {
                    int temp = target[j+1];
                    target[j+1] = temp2;
                    temp2 = temp;
                }
                target[index[i]] = nums[i];
            }
        }
        return target;
    }
}
