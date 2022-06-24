import random
from cost import CostGen
from ga import GeneticAlgorithm
import numpy as np
import utils

'''
some set values

seed remaining

2d array, where row is a variable and columns are possible values (between 2 and 5)
1 fitness value for a row (the set of variables is good/bad)

'''


class Model:
    def __init__(self, variables, lower, upper, pop_sol, mating_parents, generations, values):
        """
        variables: array of strings containing variable types: ["float", "int", "float"] 
        lower, upper: bounds on integer/float params
        pop_sol: number of chromosomes
        mating_parents: number of parents to mate
        generations: number of times to repeat
        values: cost function coefficients (will be removed eventually)
        """ 
        
        self.pop_size = (pop_sol, len(variables))
        self.mating_parents = mating_parents
        self.generations = generations
        self.values = values
        self.range = (lower, upper)
        
        self.population = []
        for i in range(pop_sol):
            chromosome = []
            for var in variables:
                current = np.zeros(random.randint(1, 9))
                if var == "float":
                    for i in range(len(current)):
                        current[i] = random.random() * upper * utils.positive_or_negative()
                elif var == "int":
                    for i in range(len(current)):
                        current[i] = random.randint(lower, upper)
                chromosome.append(current)
            self.population.append(chromosome)


    def optimize(self):
        cg = CostGen()
        ga = GeneticAlgorithm()
    
        #[[[], [], []], [[], []]]

        best_over_time = []
        for generation in range(self.generations):
            

            # Measuring the fitness of each chromosome in the population.
            # input: 3d array of chromosomes, variables, values
            # output: 1d array of fitness for each chromosome (given variables, values)
            fitness = np.empty(len(self.population))
            fitness[:] = [cg.fitnessFunc(chromosome, self.values) for chromosome in self.population]
            
            
            # Selecting the best parents in the population for mating.
            parents = ga.select_mating_pool(self.population, fitness, self.mating_parents)

            # Generating next generation using crossover.
            offspring_crossover = ga.crossoverVariables(parents,
                                            offspring_size=(self.pop_size[0]-len(parents), self.pop_size[1]))

            offspring_crossover = ga.crossoverValues(offspring_crossover, 
                                            offspring_size=(self.pop_size[0]-len(parents), self.pop_size[1]))

            # Adding some variations to the offsrping using mutation.
            offspring_mutation = ga.mutation(offspring_crossover, self.range[0], self.range[1])

            # Creating the new population based on the parents and offspring.
            self.population[0:len(parents)] = parents
            self.population[len(parents):] = offspring_mutation
            
            # The best result in the current iteration.
            best_over_time.append(max(fitness))
            # print("Best result : ", max(fitness))

        fitness = [cg.fitnessFunc(variables, self.values) for variables in self.population]
        best_fitness_idx = fitness.index(max(fitness))

        return (self.population, fitness, best_fitness_idx, best_over_time)


