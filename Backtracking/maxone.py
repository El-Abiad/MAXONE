def fitness(chromosome):
    return sum(chromosome)

def backtrack(chromosome, n, i):
    if i == n:
        return fitness(chromosome)

    chromosome.append(0)
    best = backtrack(chromosome, n, i+1)
    chromosome.pop()

    chromosome.append(1)
    best = max(best, backtrack(chromosome, n, i+1))
    chromosome.pop()

    return best

len = 5
chromosome = []
print("Best fitness:", backtrack(chromosome, len, 0))
