import random
import math

""""PARAMETROS A SEREM MODIFICADOS"""
#######################
n_population = 25 # População de possíveis soluções iniciais
n_selected = 5 # Número de melhores elementos selecionados da população inicial
max_iter = 500 # Quantidade de iterações que o algoritmo será executado
n_solutions = 10 # Quantas soluções serão geradas (quantas vezes o max_iter será repetido)

coef = [1,2,3,4,5,6,7,8] # Os coeficientes das incógnitas da igualdade. Novos elementos podem ser incluídos nesta lista para aumentar o número de incógnitas a serem encontradas.
target = 100 # O valor a ser chegado na igualdade.
#######################

def sort_aux(a: list):
    global coef
    global target
    res = 0
    for i in range(len(a)):
        res += a[i] * coef[i]
    return abs(res - target)

def new_coef(a):
    new_val_coef = random.uniform(0.5, 2)
    aux = a * new_val_coef
    return math.ceil(aux)

solutions = []
for s in range(n_solutions):
    c = []
    best = []
    for j in range(n_population):
        aux = []
        for k in range(len(coef)):
            aux.append(random.randrange(1, target))
        c.append(aux)
    c.sort(key=sort_aux)

    for i in range(1, max_iter):
        best = c[0:n_selected]
        c = []
        for j in best:
            c.append(j)
            for k in range(int(n_population/n_selected) - 1):
                c.append(list(map(new_coef, j)))

        c.sort(key=sort_aux)
    solutions.append(c[0])
print("---------------------------------")
for j in solutions:
    print(" ".join(str(x) for x in j) + " : " + str(sort_aux(j)))