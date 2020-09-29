class Solution {
    public int numJewelsInStones(String J, String S) {
        int jewel = 0;
        for (int i = 0; i < S.length(); i++) {
            if (J.indexOf(S.charAt(i)) != -1) {
                jewel += 1;
            }
        }
        return jewel;
    }
}
