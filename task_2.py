from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """

		# Тут повинен бути ваш код
    memo ={}

    def dp(remaining_length: int) -> Dict:
        if remaining_length == 0:
            return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}

        if remaining_length in memo:
            return memo[remaining_length]  # Используем кэшированное значение

        max_profit = 0
        best_cuts = []
    
   
        for item in range(1, remaining_length + 1):
            if item <= len(prices):
                remaining = dp(remaining_length - item)

                total_profit = prices[item - 1] + remaining["max_profit"]

                if total_profit > max_profit:
                    max_profit = total_profit
                    best_cuts = [item] + remaining["cuts"]
    
        memo[remaining_length] = {"max_profit": max_profit, "cuts": best_cuts, "number_of_cuts": len(best_cuts)}
        
        return memo[remaining_length] 
    
    
    return dp(length)

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    # Тут повинен бути ваш код
    
    dp=[0]*(length+1)
    cuts = [[] for _ in range(length + 1)]
    
    for item in range(1, length+1):
        max_profit = 0
        best_cut = []

        for cut in range(1, item+1):
            if cut <= len(prices):
                total_profit = prices[cut - 1] + dp[item - cut]
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_cut = [cut] + cuts[item - cut]
                
        dp[item] = max_profit
        cuts[item] = best_cut 

    
    return {
        "max_profit": dp[length],  
        "cuts": cuts[length],  
        "number_of_cuts": len(cuts[length])  
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
