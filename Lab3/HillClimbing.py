import random

def objective_function(x):
    return -(x-3)**2+9

def hill_climbing(objective, bounds, n_iterations, step_size):
    current_solution = random.uniform(bounds[0], bounds[1])
    current_score = objective(current_solution)
    print(f"Starting at x={current_solution:.5f}, score={current_score:.5f}\n")

    for i in range(n_iterations):
        candidate = current_solution + random.uniform(-step_size, step_size)
        candidate = max(min(candidate, bounds[1]), bounds[0])
        candidate_score = objective(candidate)

        if candidate_score > current_score:
            current_solution, current_score = candidate, candidate_score
            print(f">Iteration {i+1}: x={current_solution:.5f}, score={current_score:.5f}")

    return current_solution, current_score

bounds = (-5.0, 5.0)
n_iterations = 50
step_size = 0.1

best_solution, best_score = hill_climbing(objective_function, bounds, n_iterations, step_size)
print(f"\nBest solution: x={best_solution:.5f}, score={best_score:.5f}")

#OUTPUT:
"""
Starting at x=2.52087, score=8.77043

>Iteration 1: x=2.60187, score=8.84149
>Iteration 2: x=2.63082, score=8.86371
>Iteration 3: x=2.69935, score=8.90961
>Iteration 5: x=2.79825, score=8.95930
>Iteration 6: x=2.89091, score=8.98810
>Iteration 8: x=2.95325, score=8.99781
>Iteration 9: x=3.01007, score=8.99990
>Iteration 28: x=3.00373, score=8.99999

Best solution: x=3.00373, score=8.99999
"""