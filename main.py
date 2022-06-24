from model import Model
import matplotlib.pyplot as plt

def showResults(population, fitness, idx, delta):

    print("Best Solution: ")
    print(population[idx])
    print("Best solution fitness : " + str(fitness[idx]))

    plt.plot(delta)
    plt.xlabel("Generation #")
    plt.ylabel("Fitness")
    plt.show()


if __name__ == "__main__":    
    
    model = Model(variables=["float", "int", "float"], lower=0, upper=50, pop_sol=100, mating_parents=4, generations=1000, values=[1, 1, 1, 1])
    results = model.optimize()
    
    population = results[0]
    fitness = results[1]
    idx = results[2]
    delta = results[3]

    showResults(population, fitness, idx, delta)



    