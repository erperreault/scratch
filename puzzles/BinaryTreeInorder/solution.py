class Solution:
    def solution(self, root) -> list[int]:
        ans = []
        self.helper(ans, root)
        return ans
        
    def helper(self, ans: list, node) -> None:
        if node:
            self.helper(ans, node.left)
            ans.append(node.val)
            self.helper(ans, node.right)