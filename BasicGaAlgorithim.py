
##### INITIAL POPULATION

import random

def generate_population(number_of_queens=8, size_of_population=19):
        return [_generate_genotype(number_of_queens) for _ in range(size_of_population)]


def _generate_genotype(number_of_queens):
    return  [random.randrange(number_of_queens) for num in range(number_of_queens )]


##### FITNESS_FUCTION

def fitness_function(genotype):
    """finds a score based off the number of queens which are not being attacked
    """



    fitness_score = 0

    for i_p, phenotype in enumerate(genotype):
        for i_o_p, other_phenotype in enumerate(genotype):

            if phenotype == other_phenotype:
                # is on the same row
                continue
            if i_p - phenotype == i_o_p - other_phenotype:
                # is diagonally attacked
                continue
            if i_p + phenotype == i_o_p + other_phenotype:
                # is diagonally attacked
                continue
            fitness_score += 1
    
    return fitness_score / 2


##### SELECTION

def selection(population, fitness_scores, size_of_population):
    """return a list of selected pairs"""
    ### TODO if the fitness score is high they will always be selected
    ### should they only be chosen once
    ### or could use tournament selection
    ### book claims that they can be selecte multilpe times
    ### so should be fine, but maybe the weighted choice is too high
    ### leave this as is and look at tournament selection
    ### for optimisation
    ### https://brandinho.github.io/genetic-algorithm/

    selected = []
    for _ in range(size_of_population):
        parent_one = _random_weighted_choice(population, fitness_scores)
        parent_two = _random_weighted_choice(population, fitness_scores, selected=parent_one)

        selected.append((parent_one, parent_two))

    return selected


def _random_weighted_choice(population, weights, selected=None):
    """pick one from list proportional to weights"""

    if selected is not None:
        index = population.index(selected)
        population = population[:index] + population[index+1:]
        weights = weights[:index] + weights[index+1:]

    # avoid zero weights constraint
    if sum(weights) == 0.0:
        weights[0] = 0.1

    return random.choices(population, weights=weights, k=1)[0]


### CROSSOVER

def crossover(selected_pairs, number_of_queens):

    offspring = []
    for s_p in selected_pairs:
        # generate random cross over points - 0 - max number of queens
        cross_over_index = random.randint(0, number_of_queens - 1)
        parent_one = s_p[0]
        parent_two = s_p[1]   

        child = _crssover(parent_one, parent_two, cross_over_index)
        offspring.append(child)

    return offspring


def _crssover(parent_one, parent_two, cross_over_index):
    return parent_one[:cross_over_index] + parent_two[cross_over_index:]



### MUTATION

import random

def _mutate(current_value, number_of_queens):
    new_value = current_value

    while new_value == current_value:
        new_value = random.randint(0, number_of_queens - 1)

    return new_value


def mutation(population, mutation_frequency, number_of_queens):        
    for genotype in population:
        for s_i,_ in enumerate(genotype):
            x = random.randint(1, mutation_frequency)
            if x == 1:
                genotype[s_i] = _mutate(genotype[s_i], number_of_queens)
    return population


### HELPER

from scipy import special

def check_for_perfect_genotype(population, perfect_score):

    for pop in population:
        if fitness_function(pop) == perfect_score:
            return pop

    return []

def calculate_perfect_score(number_of_queens):
    return special.comb(
                    number_of_queens,
                    2
                )

