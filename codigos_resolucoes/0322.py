class Solution:
    """
    Este exercício seria o problema dos selos, onde há a possibilidade de moedas não múltiplas
    """
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        matrix_M = []
        
        # Inicializa a primeira coluna e a primeira linha com 0
        matrix_M = [[0 if j == 0 else float('inf') for j in range(amount + 1)] for i in range(len(coins) + 1)]
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j < coins[i - 1]:
                    matrix_M[i][j] = matrix_M[i-1][j]
                elif j >= coins[i - 1] and j < 2*coins[i - 1]:
                    matrix_M[i][j] = min(matrix_M[i-1][j], 1 + matrix_M[i-1][j - coins[i-1]])
                else:
                    matrix_M[i][j] = min(matrix_M[i-1][j], 1 + matrix_M[i-1][j - coins[i-1]], 1 + matrix_M[i][j - coins[i-1]])
        
        final_result = matrix_M[len(coins)][amount]
        
        return final_result if final_result != float('inf') else -1
    
### TESTES ###
sol = Solution()
moedas = [2147483647]
valor_total = 2

print(sol.coinChange(moedas, valor_total))