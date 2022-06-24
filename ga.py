import random
import math
import numpy as np
import utils

class GeneticAlgorithm:
    # This project is extended and a library called PyGAD is released to build the genetic algorithm.
    # PyGAD documentation: https://pygad.readthedocs.io
    # Install PyGAD: pip install pygad
    # PyGAD source code at GitHub: https://github.com/ahmedfgad/GeneticAlgorithmPython

    def cal_pop_fitness(self, equation_inputs, pop):
        # Calculating the fitness value of each solution in the current population.
        # The fitness function caulcuates the sum of products between each input and its corresponding weight.
        fitness = np.sum(pop*equation_inputs, axis=1)
        return fitness

    def select_mating_pool(self, pop, fitness, num_parents):
        # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
        parents = []
        for parent_num in range(num_parents):
            max_fitness_idx = np.where(fitness == np.max(fitness))
            max_fitness_idx = max_fitness_idx[0][0]
            parents.append(pop[max_fitness_idx])
            
            fitness[max_fitness_idx] = -99999999999
        
        return parents

    def crossoverVariables(self, parents, offspring_size):
        offspring = []
        # The point at which crossover takes place between two parents. Usually it is at the center.
        crossover_point = np.uint8(offspring_size[1]/2)

        for k in range(offspring_size[0]):
            # Index of the first parent to mate.
            parent1_idx = k%len(parents)
            # Index of the second parent to mate.
            parent2_idx = (k+1)%len(parents)
            # The new offspring will have its first half of its genes taken from the first parent.
            #offspring[k, 0:crossover_point] = parents[parent1_idx][0:crossover_point]
            # The new offspring will have its second half of its genes taken from the second parent.
            #offspring[k, crossover_point:] = parents[parent2_idx][crossover_point:]
            offspring.append(parents[parent1_idx][0:crossover_point] + parents[parent2_idx][crossover_point:])

        return offspring

    def crossoverValues(self, parents, offspring_size):
        # TODO: add crossover for individual values (only crossing over variables right now)
        
        return parents

    def mutation(self, offspring_crossover, lower, upper):
        # Mutation changes a single gene in each offspring randomly.
        for idx in range(len(offspring_crossover)):
            targetGene_idx = random.randint(0, len(offspring_crossover[idx]) - 1)            
            
            # Gene to be mutated
            mutateGene = offspring_crossover[idx][targetGene_idx]
            
            # Gene to replace mutateGene
            newGene = np.zeros(random.randint(1, 9))
            for i in range(len(newGene)):
                mu = mutateGene[i % len(mutateGene)]
                sigma = mutateGene[i % len(mutateGene)] # Hyperparameter for tightness of distribution.

                #newVal = random.gauss(mu, sigma)
                newVal = random.random() * upper * utils.positive_or_negative()
                while newVal > upper or newVal < lower:
                    newVal = random.gauss(mu, sigma) # mutated values will be distributed normally around old value
                
                if type(mutateGene[0]) == int:
                    newVal = math.floor(newVal)
                    if newVal < lower: # if the floor put it out of range, add 1
                        newVal += 1
                newGene[i] = newVal

            offspring_crossover[idx][targetGene_idx] = newGene
        return offspring_crossover
    
