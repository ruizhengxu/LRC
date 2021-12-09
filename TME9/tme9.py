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

a = compose('=', 'd')
b = compose('m', 'd')
c = a.union(b)
print(c)

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

