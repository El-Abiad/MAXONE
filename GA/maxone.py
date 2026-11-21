import random

def fitness(chromosome):
    return sum(chromosome)

def generate_chromosome(n):
    chromosome = []
    while(n):
        chromosome.append(random.randint(0, 1))
        n -= 1
    return chromosome

def initialize_population(pop_size, n):
    population = []
    while(pop_size):
        population.append(generate_chromosome(n))
        pop_size -= 1
    return population

def selection(population):
    parents = random.sample(population, 3)
    parents.sort(key=fitness, reverse=True)
    return parents[:2]

def crossover(parent1, parent2):
    slice = random.randint(0, len(parent1))
    offspring = parent1[:slice] + parent2[slice:]
    return offspring

def remove_bad(population):
    parents = sorted(population, key=fitness, reverse=True)
    parents.pop()
    return population

def mutation(chromosome, mutation_rate):
    for index in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[index] = 1 - chromosome[index]

    return chromosome


def get_best(population):
    chromosome = []
    best = 0
    for i in population:
        if sum(i) > best:
            best = sum(i)
            chromosome = i

    return chromosome

def genetic_algorithm(pop_size, n, generations, mutation_rate):
    population = initialize_population(pop_size, n)

    while(generations):
        parents = selection(population)
        parent1 = parents[0]
        parent2 = parents[1]

        offspring = crossover(parent1, parent2)
        offspring = mutation(offspring, mutation_rate)
        population.append(offspring)
        population = remove_bad(population)
        generations -= 1

    return get_best(population)

n = 5
pop_size = 10
generations = 30
mutation_rate = 0.2

answer = genetic_algorithm(pop_size, n, generations, mutation_rate)

print(answer)