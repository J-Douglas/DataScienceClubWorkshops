class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Dynamic Programming - O(nm)
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        n = len(text1)
        m = len(text2)
        
        dp = [[0 for a in range(m+1)] for b in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(1+dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
        return dp[n][m]