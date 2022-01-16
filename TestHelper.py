## GENERATE TEST POPULATION

import pickle

from BasicGaAlgorithim import generate_population

def generate_test_population(test_populations_name, number_of_queens, size_of_population, number_of_tests):

    test_populations_name = "testpopulations/" + test_populations_name
    test_population = []

    for i in range(number_of_tests):
            test_population.append(generate_population(
                                        number_of_queens, 
                                        size_of_population
                                    ))

    with open(test_populations_name, 'wb') as f:
            pickle.dump(test_population, f)


### IMPORT TEST POPULATION

def load_test_population(test_populations_name):

    with open(test_populations_name, 'rb') as f:
        return pickle.load(f)
