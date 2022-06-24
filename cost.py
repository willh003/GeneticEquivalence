
class CostGen:

    # eventually replace this with a function that evaluates structural coverage
    def fitnessFunc(self, chromosome, coefs):
        # chromosome: 2d array of variables and coefs

        fitness = 0
        for variable in chromosome:
            for value in range(len(variable)):

                fitness += variable[value] * coefs[value % len(coefs)]
        
        return fitness
