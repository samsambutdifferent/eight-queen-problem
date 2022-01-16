
from BasicGaAlgorithim import (
                                fitness_function,
                                generate_population
                            )


### CROSSOVER

import random

def crossover(selected_pairs, number_of_queens):

    offspring = []
    for s_p in selected_pairs:

        parent_one = s_p[0]
        parent_two = s_p[1]   

        # generate random cross over points - 0 - max number of queens
        cross_over_index_one = random.randint(0, number_of_queens - 2)
        cross_over_index_two = random.randint(cross_over_index_one + 1, number_of_queens - 1)
 

        child = _crssover(parent_one, parent_two, cross_over_index_one, cross_over_index_two)
        offspring.append(child)

    return offspring


def _crssover(parent_one, parent_two, cross_over_index_one, cross_over_index_two):
    
    child = parent_one[:cross_over_index_one] + parent_two[cross_over_index_one:cross_over_index_two] + parent_one[cross_over_index_two:]
    
    return child


### SELECTION

import random
import math

def selection(population, size_of_population, tournament_population_size):
    """return a list of selected pairs"""

    selected = []

    for _ in range(size_of_population):
        selected.append(_tournament_selection(population, tournament_population_size))

    return selected
    

def _tournament_selection(population, tournament_population_size):
    tournament_population = random.choices(population=population, k=tournament_population_size)
    fitness_socres = [(entrant, fitness_function(entrant)) for entrant in tournament_population]
    srted = sorted(fitness_socres, key=lambda x: x[1], reverse=True)

    return srted[0][0], srted[1][0]


### ELITISM

import math
from random import sample

def elitism(population, fitness_scores, elitism_ratio, size_of_population):
    number_of_elites = math.floor(size_of_population * elitism_ratio)
    pop_fitness = [(population[i], fitness_scores[i]) for i in range(len(population))]
    sorted_by_score = sorted(pop_fitness, key=lambda x: x[1], reverse=True)

    return [sorted_by_score[i][0] for i in range(number_of_elites)]


def remove_parent_pairs(population, elitism_ratio, size_of_population):
    """
    """
    number_to_remove = math.floor(size_of_population * elitism_ratio)

    return _remove_n_random_values_from_list(population, number_to_remove)


def _remove_n_random_values_from_list(values, number_to_remove):
    remove = set(sample(range(len(values)),number_to_remove))
    return [value for index,value in enumerate(values) if not index in remove]
