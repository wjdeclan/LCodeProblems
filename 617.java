/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
            return null;
        }
        TreeNode t = new TreeNode();
        if (t1 == null) {
            t.val = t2.val;
            t.left = t2.left;
            t.right = t2.right;
            return t;
        } else {
            if (t2 == null) {
                t.val = t1.val;
                t.left = t1.left;
                t.right = t1.right;
                return t;
            } else {
                t.val = t1.val + t2.val;
                t.left = mergeTrees(t1.left, t2.left);
                t.right = mergeTrees(t1.right, t2.right);
                return t;
            }
        }
    }
}
