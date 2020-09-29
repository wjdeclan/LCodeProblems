class Solution {
    public int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> r = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i+=2) {
            for (int j = 0; j < nums[i]; j++) {
                r.add(nums[i+1]);
            }
        }
        int[] ret = new int[r.size()];
        for (int i = 0; i < r.size(); i++) {
            ret[i] = r.get(i);
        }
        return ret;
    }
}
