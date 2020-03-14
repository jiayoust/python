from math import *
from random import *
import sys
import numpy as np
import matplotlib.pyplot as plt

def GA():
    seed()
    generation_num = 500
    population_num = 20
    codebit_num = 17
    prob_crossover = 0.7
    prob_mutation = 0.02
    POPULATION = []
    FITNESS = []
    PROB = []
    for t in range(generation_num):
        fitness_sum = 0
        P_TMP = POPULATION[:]
    for i in range(0, population_num, 2):
        d1 = Select(P_TMP)
        d2 = Select(P_TMP)
        Crossover(d1, d2)
        Mutate(d1)
        Mutate(d2)
        POPULATION[i] = d1
        POPULATION[i + 1] = d2
        f1 = CalculateFitness(d1)
        FITNESS[i] = f1
        fitness_sum += f1
        f2 = CalculateFitness(d2)
        FITNESS[i + 1] = f2
        fitness_sum += f2
        PROB[0] = FITNESS[0] / fitness_sum
        for i in range(1, len(FITNESS)):
            PROB[i] = PROB[i - 1] + FITNESS[i] / fitness_sum
        # return x with MAX_FITNESS of POPULATION
    def Init():
        max_fitness=-sys.maxsize
        max_individual=None
        fitness_sum = 0
        for i in range(population_num):
            individual=[str(randint(0,1000))]
            POPULATION.append(individual)
            f = CalculateFitness(individual)
            FITNESS.append(f)
            fitness_num += f
        PROB.append(FITNESS[0] / fitness_sum)
        for i in range(1, len(FITNESS)):
            PROB.append(PROB[i - 1] + FITNESS[i] / fitness_sum)

    def Fitness(xx):
        x = 0 + xx * 10 / 131071  # pow(2,17)-1=131071
        return x + 2 * sin(2 * x) + 3 * sin(3 * x) + 4 * sin(4 * x)

    def Select(population):
        r = random()
        for i in range(len(PROB)):
            if r <= PROB[i]:
                return population[i][:]

    def Crossover(d1, d2):
        r = random()
        if r <= prob_crossover:
            point = randint(0, len(d1) - 1)
            d1[point:], d2[point:] = d2[point:], d1[point:]

    def Mutate(d):
        for i in range(len(d)):
            if random() <= prob_mutation:
                d[i] = str((int(d[i]) + 1) % 2)

    def CalculateFitness(d):
        xx = int(''.join(d), base=2)
        f = Fitness(xx)
        if f < 0:  # abandon negative value
            f = 0
        return f

