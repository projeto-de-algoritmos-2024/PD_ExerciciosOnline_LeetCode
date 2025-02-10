class Solution:
    """
    Problema em que é necessário descobrir o menor custo para comprar passes de transporte dado os dias que se deseja viajar e os custos dos passes.
    
    OPT(dia) = {
                min(custo_dia + OPT(dia + 1),  |
                custo_semana + OPT(dia + 7),   |    Se o dia atual é um dia de viagem
                custo_mes + OPT(dia + 30))     |
                
                OPT(dia + 1)                   |    Se o dia atual não é um dia de viagem
                
                0                              |    Se o dia atual é maior que 365
    }
    
    """
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)  # Decorador que guarda em cache os resultados de chamadas anteriores
        
        def OPT(day):
            # Primeira condição de parada
            if day > 365:
                return 0
            if day not in days:
                return OPT(day + 1)  # Se não há viagem nesse dia, não compramos nada
            return min(
                costs[0] + OPT(day + 1),   # Passe de 1 dia
                costs[1] + OPT(day + 7),   # Passe de 7 dias
                costs[2] + OPT(day + 30)   # Passe de 30 dias
            )

        return OPT(1)
    
###### Testes ###### 
# sol = Solution()

# dias = [1,4,6,7,8,20]
# passagens = [2,7,15]

# print(sol.mincostTickets(dias, passagens))
