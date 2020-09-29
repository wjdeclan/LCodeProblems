class Solution {
    public int subtractProductAndSum(int n) {
        int p = 1;
        int s = 0;
        while (n > 0) {
            int t = n % 10;
            n = n / 10;
            p = p * t;
            s = s + t;
        }
        return p - s;
    }
}
