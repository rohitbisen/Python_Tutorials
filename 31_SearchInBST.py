class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur=root
        while cur:
            if cur.val==val:
                return cur
            if cur.val>val:
                cur=cur.left
            elif cur.val<val:
                cur=cur.right
        return None