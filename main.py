from Backtracking import maxone as bt
from GA import maxone as ga
from MA import maxone as ma

def main():
    n = 10
    chromosome = []
    pop_size = 10
    generations = 20
    mutation_rate = 0.2
    
    
    backtracking_ans = bt.backtrack(chromosome, n, 0)
    GA_ans = ga.genetic_algorithm(pop_size, n, generations, mutation_rate)
    MA_ans = ma.memetic_algorithm(pop_size, n, generations, mutation_rate)

    print("Backtrack:\n", backtracking_ans)
    print("GA:\n", GA_ans)
    print("MA:\n", MA_ans)
    


if __name__ == "__main__":
    main()