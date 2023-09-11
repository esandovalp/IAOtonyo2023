#Hill climbing is a simple optimization algorithm used in Artificial Intelligence (AI) to find the best possible solution for a given problem. It belongs to the family of local search algorithms and is often used in optimization problems where the goal is to find the best solution from a set of possible solutions.
import random

# Define the objective function to be optimized
def objective_function(x):
    return -x**2 + 10*x + 9  # Example objective function (you can change this)

# Hill climbing algorithm
def hill_climbing(max_iterations, step_size, initial_solution):
    current_solution = initial_solution

    for _ in range(max_iterations):
        # Generate a random neighbor within the specified step_size
        neighbor = current_solution + random.uniform(-step_size, step_size)
        
        # Calculate the objective function values for current and neighbor solutions
        current_value = objective_function(current_solution)
        neighbor_value = objective_function(neighbor)
        
        # If the neighbor solution is better, move to it; otherwise, stop
        if neighbor_value > current_value:
            current_solution = neighbor
    
    return current_solution, objective_function(current_solution)

# Parameters for the algorithm
max_iterations = 1000
step_size = 0.1
initial_solution = random.uniform(-10, 10)

# Run the hill climbing algorithm
best_solution, best_value = hill_climbing(max_iterations, step_size, initial_solution)

# Print the best solution and its objective value
print(f"Best solution: {best_solution}")
print(f"Best value: {best_value}")
