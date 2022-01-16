

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