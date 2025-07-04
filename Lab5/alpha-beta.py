def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, path):
    if depth == 3:
        return values[nodeIndex], path+[nodeIndex]
    
    if maximizingPlayer:
        best = float('-inf')
        best_path = []
        for i in range(2):
            val, new_path = alphabeta(depth+1, nodeIndex*2+i, False, values, alpha, beta, path+[nodeIndex])

            if val > best:
                best = val
                best_path = new_path

            alpha = max(alpha, best)
            if beta <= alpha:
                break

        return best, best_path
    
    else:
        best = float('inf')
        best_path = []
        for i in range(2):
            val, new_path = alphabeta(depth+1, nodeIndex*2+i, True, values, alpha, beta, path+[nodeIndex])

            if val < best:
                best = val
                best_path = new_path

            beta = min(beta, best)
            if beta <= alpha:
                break

        return best, best_path
    
values = [3, 5, 2, 9, 12, 5, 23, 23]
optimal_value, optimal_path = alphabeta(0, 0, True, values, float('-inf'), float('inf'), [])

print("The optimal value is : ", optimal_value)
print("The path taken is : ", optimal_path)


#OUTPUT:
'''
The optimal value is :  12
The path taken is :  [0, 1, 2, 4]
'''