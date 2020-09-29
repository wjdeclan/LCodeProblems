class Solution {
    public int rotatedDigits(int N) {
        int c = 0;
        for (int i = 1; i <= N; i++) {
            int t = i;
            boolean flag = false;
            while (t > 0) {
                int n = t % 10;
                if (n == 2 || n == 5 || n == 6 || n == 9) {
                    flag = true;
                } else if (n == 3 || n == 4 || n == 7) {
                    flag = false;
                    break;
                }
                t = t / 10;
            }
            if (flag) {
                c += 1;
            }
        }
        return c;
    }
}
