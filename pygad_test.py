import pygad
import random
import numpy as np

# 5 input variables, 10 possible valuesw

desired_output = 0
cutoff_indices = [4, 6, 8, 10, 15, 20] # list of cutoff indices for variables
types = ["float", "int", "boolean", "float", "int"]
counter = 0
def fitness_func(solution, solution_idx):
    out = np.sum(solution)
    global counter
    counter += 1
    fitness = 1.0/np.abs((desired_output - out))
    return fitness


fitness_function = fitness_func

num_generations = 1000
num_parents_mating = 4

sol_per_pop = 8
num_genes = 100

init_range_low = -500
init_range_high = 500
# 010011000100101
parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = np.sum(solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
print(counter)