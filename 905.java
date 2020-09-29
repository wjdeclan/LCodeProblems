class Solution {
    public int[] sortArrayByParity(int[] A) {
        int[] ret = new int[A.length];
        int[] odd = new int[A.length];
        int c1 = 0;
        int c2 = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] % 2 == 0) {
                ret[c1] = A[i];
                c1++;
            } else {
                odd[c2] = A[i];
                c2++;
            }
        }
        for (int i = 0; i < c2; i++) {
            ret[c1] = odd[i];
            c1++;
        }
        return ret;
    }
}
