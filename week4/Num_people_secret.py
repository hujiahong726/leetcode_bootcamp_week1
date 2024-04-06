class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            for j in range(min(i+1, forget)):
                if j > 0:
                    dp[i][j] = dp[i-1][j-1]
                if delay-1 <= j <= forget-2:
                    dp[i][0] = (dp[i][0] + dp[i-1][j]) % MOD
        return sum(dp[n-1]) % MOD
