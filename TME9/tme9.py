#########################
# XU Ruizheng - 21111473
#########################

# -*- coding: utf-8 -*-
"""
Dictionnaires décrivants les transposés et symétries de relations, 
ainsi que les listes de relations obtenues avec les compositions de base
dans le tableau donné en TD
"""

'''
transpose : dict[str:str]
transpose[r] fournit la transposition de la relation r
'''
transpose = {
    '<':'>',
    '>':'<',
    'e':'et',
    's':'st',
    'et':'e',
    'st':'s',
    'd':'dt',
    'm':'mt',
    'dt':'d',
    'mt':'m',
    'o':'ot',
    'ot':'o',
    '=':'='                 
    }

'''
symetrie : dict[str:str]
symetrie[r] fournit la symetrie de la relation r
'''
symetrie = {
    '<':'>',
    '>':'<',
    'e':'s',
    's':'e',
    'et':'st',
    'st':'et',
    'd':'d',
    'm':'mt',
    'dt':'dt',
    'mt':'m',
    'o':'ot',
    'ot':'o',
    '=':'='
    }            

'''
compositionBase : dict[tuple[str,str]:set[str]]
compositionBase[(r1,r2)] est l’ensemble des relations obtenues
    lorsqu’on compose la relation r1 avec la relation r2
'''             
compositionBase = {        
        ('<','<'):{'<'},
        ('<','m'):{'<'},
        ('<','o'):{'<'},
        ('<','et'):{'<'},
        ('<','s'):{'<'},
        ('<','d'):{'<','m','o','s','d'},
        ('<','dt'):{'<'},
        ('<','e'):{'<','m','o','s','d'},
        ('<','st'):{'<'},
        ('<','ot'):{'<','m','o','s','d'},
        ('<','mt'):{'<','m','o','s','d'},
        ('<','>'):{'<','>','m','mt','o','ot','e','et','s','st','d','dt','='},
        ('m','m'):{'<'},
        ('m','o'):{'<'},
        ('m','et'):{'<'},
        ('m','s'):{'m'},
        ('m','d'):{'o','s','d'},
        ('m','dt'):{'<'},
        ('m','e'):{'o','s','d'},
        ('m','st'):{'m'},
        ('m','ot'):{'o','s','d'},
        ('m','mt'):{'e','et','='},
        ('o','o'):{'<','m','o'},
        ('o','et'):{'<','m','o'},
        ('o','s'):{'o'},
        ('o','d'):{'o','s','d'},
        ('o','dt'):{'<','m','o','et','dt'},
        ('o','e'):{'o','s','d'},
        ('o','st'):{'o','et','dt'},
        ('o','ot'):{'o','ot','e','et','d','dt','st','s','='},
        ('s','et'):{'<','m','o'},
        ('s','s'):{'s'},
        ('s','d'):{'d'},
        ('s','dt'):{'<','m','o','et','dt'},
        ('s','e'):{'d'},
        ('s','st'):{'s','st','='},
        ('et','s'):{'o'},
        ('et','d'):{'o','s','d'},
        ('et','dt'):{'dt'},
        ('et','e'):{'e','et','='},
        ('d','d'):{'d'},
        ('d','dt'):{'<','>','m','mt','o','ot','e','et','s','st','d','dt','='},
        ('dt','d'):{'o','ot','e','et','d','dt','st','s','='}       
    }


############
# Exercice 1
############

# Question 2

def transposeSet(S):
    '''
    Renvoie l’ensemble des relations transposées des relations
        qui apparaissent dans S
    '''
    return set(transpose[r] for r in S)

def symetrieSet(S):
    '''
    Renvoie l’ensemble des relations symétries des relations
        qui apparaissent dans S
    '''
    return set(symetrie[r] for r in S)

# Question 3

def compose(r1, r2):
    '''
    renvoie l’ensemble des relations que l’on peut obtenir
        par composition des relations r1 et r2
    '''

    # Si une des relations est =, alors on renvoie celle qui n'est pas =
    # Si les deux relations sont =, alors on renvoie =
    if r1 == '=' or r2 == '=':
        if r1 == '=': return set(r2)
        else: return set(r1)

    # On regarde d'abord si r1 et r2 sont dans la composition de base
    if (r1, r2) in compositionBase.keys():
        return set(compositionBase[(r1, r2)])
    else:
        # Règle de transposition (cf TME9, Ex1Q3)
        r1_t = transpose[r1]
        r2_t = transpose[r2]
        if (r2_t, r1_t) in compositionBase.keys():
            return set(transposeSet(compositionBase[(r2_t, r1_t)]))
        # Règle de symétrie (cf TME9, Ex1Q3)
        r1_s = symetrie[r1]
        r2_s = symetrie[r2]
        if (r1_s, r2_s) in compositionBase.keys():
            return set(symetrieSet(compositionBase[(r1_s, r2_s)]))
        # Règle de deux transformation (cf TME9, Ex1Q3)
        r1_st = symetrie[transpose[r1]] 
        r2_st = symetrie[transpose[r2]]
        if (r2_st, r1_st) in compositionBase.keys():
            return set(transposeSet(symetrieSet(compositionBase[(r2_st, r1_st)])))
    
    # Si aucune des règles vérifient, on renvoie vide
    return set()

print(compose('=', 'd')) # {d}
print(compose('m', 'd')) # {d, o, s}
print(compose('ot', '>')) # {>}
print(compose('>', 'e')) # {>}
print(compose('ot', 'm')) # {dt, et, o}
print("\n")

# Question 4

def compositionSet(S1, S2):
    '''
    renvoie l’ensemble des relations que l’on peut obtenir par composition
        des relations qui apparaissent dans l’ensemble S1 avec les relations
        qui apparaissent dans l’ensemble S2
    '''
    return set.union(*[compose(r1, r2) for r1 in S1 for r2 in S2])

############
# Exercice 2
############

# Question 1
class Graphe:
    
    def __init__(self, noeuds, relations):
        self.noeuds = noeuds
        self.relations = {}
        for k, v in relations.items():
            self.relations[k] = v

    def getRelations(self, i, j):
        if (i, j) in self.relations.keys():
            return (set(self.relations[(i, j)]))
        if (j, i) in self.relations.keys():
            return transposeSet((set(self.relations[(j, i)]))) # Mettre transposee à la place si existe
        return set(transpose.keys())
    
    # Question 2    
    def propagation(self, n1, n2, verbose=False):
        '''
        Utilise l’algorithme d’Allen pour propager la relation entre les noeuds
        n1 et n2 dans le reste du graphe G
        '''
        pile = [(n1, n2, self.getRelations(n1, n2))]
        step = 0
        while len(pile) != 0:
            step += 1
            (i, j, Rij) = pile.pop(0)
            if verbose : print("Propagation de R" + i + j + " =", Rij, "\n------------------------")
            for k in [n for n in self.noeuds if n != i and n!= j]:
                Rik = self.getRelations(i, k)
                nRik = Rik.intersection(compositionSet(Rij, self.getRelations(j, k)))
                if verbose:
                    print("R"+i+k + " = ", Rik, "\n", "R"+i+k + " & " + "R"+i+j+ " o R"+j+k + " =",\
                    Rik, "&", Rij, "o", self.getRelations(j, k), '=', nRik)
                    if nRik != Rik:print("R"+i+k + " !=", nRik, "\n")
                    else: print("inchangé\n")
                Rkj = self.getRelations(k, j)
                nRkj = Rkj.intersection(compositionSet(self.getRelations(k, i), self.getRelations(i, j)))
                if verbose : 
                    print("R"+k+j + " = ", Rkj, "\n", "R"+k+j + " & " + "R"+k+i+ " o R"+i+j + " =",\
                    Rkj, "&", self.getRelations(k, i), "o", self.getRelations(i, j), '=', nRkj)
                    if nRkj != Rkj: print("R"+k+j + " !=", nRkj, "\n")
                    else: print("inchangé\n")
                if len(nRik) == 0 or len(nRkj) == 0:
                    if verbose: print("Contradiction temporelle.\nFin en", step , "propagations.\n\n")
                    return
                if nRik != Rik:
                    Rik = nRik
                    self.ajouter(Rik, i, k, verbose)
                    pile.append((i, k, Rik))
                if nRkj != Rkj:
                    Rkj = nRkj
                    self.ajouter(Rkj, k, j, verbose)
                    pile.append((k, j, Rkj))
        if verbose: print("Fin en", step , "propagations.\nAprès propagation :", self, "\n\n")
        
    # Question 3
    def ajouter(self, r, i, j, verbose=False):
        '''
        Ajouter relations r au graphe G
        '''
        if (i, j) not in self.relations:
            if verbose: print("Mise à jour de la valeur de R"+i+j + " : ", self.getRelations(i, j), end="")
            self.relations[(i, j)] = self.getRelations(i, j).intersection(r)
            if verbose: print(" -->", self.getRelations(i, j), "\n")
        else:
            if verbose: print("Mise à jour de la valeur de R"+i+j + " : ", self.getRelations(i, j), end="")
            self.relations[(i, j)] = set(r)
            if verbose: print(" -->", self.getRelations(i, j), "\n")
            
    # Question 5
    def retirer(self, i):
        self.noeuds.remove(i)
        for k in list(self.relations.keys()):
            if i in k: self.relations.pop(k)

    def __repr__(self):
        return str(self.noeuds) + ", " + str(self.relations)

# Question 4

# Exemple du cours
# G = Graphe(['S', 'L', 'J'], {('S', 'L'): ['o', 'm'],
#                               ('S', 'J'): ['<', 'm', 'mt', '>'],
#                               ('L', 'J'): ['o', 's']})
# print("G :", G, "\n")
# G.propagation('L', 'J')
# print("G après propagation L{o, s}J :", G, "\n")

G1 = Graphe(['A', 'B', 'C'], {('A', 'B'): ['<'],
                              ('A', 'C'): ['>'],
                              ('B', 'C'): ['=']})
G1.propagation('B', 'C')
print("G1 :", G1)
print("G1 après propagation B{=}C :", G1, "\n")

G2 = Graphe(['A', 'B', 'C'], {('A', 'B'): ['<'],
                              ('A', 'C'): ['<'],
                              ('B', 'C'): ['=']})
print("G2 :", G2)
G2.propagation('B', 'C')
print("G2 après propagation B{=}C :", G2, "\n")
    
# Question 6
G1.propagation('B', 'C', verbose=True)

# Question 7

G = Graphe(['Tc', 'Tm', 'Ts', 'Te', 'Tb'], {('Tm', 'Tc'): ['d'],
                                ('Ts', 'Tc'): ['m']})
G.propagation('Ts', 'Tc', verbose=True)

# ---------------------------------------------------

G.ajouter('<', 'Ts', 'Te')
G.ajouter('<', 'Te', 'Tm')
G.propagation('Ts', 'Te', verbose=True) # Propagation de la contrainte entre Ts et Te
G.propagation('Te', 'Tm', verbose=True) # Propagation de la contrainte entre Te et Tm
print("La relation de Te et Tc après les propagations :", G.relations[('Te', 'Tc')])

# ---------------------------------------------------

G.retirer('Ts')
G.ajouter(['o', 'dt', 'et'], 'Te', 'Tb')
G.ajouter(['<', 'm', 'mt', '>'], 'Tb', 'Tc')
G.propagation('Tb', 'Tc', verbose=True)

G.noeuds.append('Ts')
G.propagation('Tb', 'Tc', verbose=True)