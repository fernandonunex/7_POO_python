

def knapsack(capacity, weight, values, n):
    
    if n == 0 or capacity == 0:
        return 0
    
    if weight[n - 1] > capacity:
        return knapsack(capacity, weight, values, n - 1)
    
    return max(values[n-1] + knapsack(capacity - weight[n - 1], weight, values, n - 1),
                knapsack(capacity, weight, values, n - 1))



if __name__ == '__main__':
    valores = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(valores)

    result = knapsack(capacity, weights, valores, n)
    print(result)