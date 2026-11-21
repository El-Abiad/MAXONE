def fitness(chromosome):
    return sum(chromosome)

def backtrack(chromosome, n, i):
    if i == n:
        return chromosome.copy()

    chromosome.append(0)
    best = backtrack(chromosome, n, i + 1)
    chromosome.pop()

    chromosome.append(1)
    candidate = backtrack(chromosome, n, i + 1)
    chromosome.pop()

    if fitness(candidate) > fitness(best):
        best = candidate

    return best
