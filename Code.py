class Solution:
    def countBits(self, n: int) -> List[int]:
        x = [bin(x)[2:].count('1') for x in range(n+1)]
        return x
