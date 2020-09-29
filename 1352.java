class ProductOfNumbers {

    private ArrayList<Integer> s;

    public ProductOfNumbers() {
        s = new ArrayList<Integer>();
    }

    public void add(int num) {
        s.add(num);
    }

    public int getProduct(int k) {
        int p = 1;
        for (int i = 1; i <= k; i++) {
            p = p * s.get(s.size() - i);
        }
        return p;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
