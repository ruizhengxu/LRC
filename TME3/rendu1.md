LRC - TME 3
===========
**Ruizheng Xu, 21111473**
***Binôme : Luka Laval***
-----------------------

# 2 / Exercices
## Exercice 1
Les étapes affichées lors du *trace* ressemblent à une procédure récursive. On entre dans différents niveaux puis une fois "bloqué" on remonte le résultat en repassant par chacune des couches.

Pour essayer de mieux comprendre le processus, on peut faire en sorte de faire une boucle infinie. En changeant les clauses en:  
`r(a,b).`  
`r(f(X),Y) :- r(f(X),Y).`  
`p(f(X),Y) :- r(X,Y).`  
(expliquer en quoi la boucle est infinie)

## Exercice 2
Il y a un deuxième cas possible pour `q(X,b)`. Il est intéressant de voir la *trace* quand on inverse l'ordre des clauses. Dans l'ordre normal, **swipl** passe par trois étapes principales (décrire les étapes).  
(expliquer le choix de swipl pour pour clause 3 lors du parcours r ou q)

## Exercice 3
`consciencieux(pascal).`  
`consciencieux(zoe).`  
`reviser(Etudiant) :- serieux(Etudiant).`  
`devoirs(Etudiant) :- consciencieux(Etudiant).`  
`reussir(Etudiant) :- reviser(Etudiant).`  
`serieux(Etudiant) :- devoirs(Etudiant).`  

Requête "qui va réussir ?" : `reussir(X).`  
Résultat : X = pascal ; X = zoe.

## Exercice 4

Les réponses et les résultats (tests) sont dans le fichier ex4.pl.

6. Dans cette question, il est demandé de faire le prédicat ancêtre, et il y a deux manière de représenter ce dernier dans prolog :<br>
   a. `ancetre(X,Y) :- parent(X,Y).`
        `ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).`
   b. `ancetre(X,Y) :- parent(X,Y).`
        `ancetre(X,Y) :- ancetre(Z,Y), parent(X,Z).`
<br> Pour la définition a, X est ancêtre de Y si X est parent de Y, **ET** que si X est parent de Z et Z est un ancêtre de Y.
<br> Pour la définition b, X est ancêtre de Y si X est parent de Y **ET** que si Z est un ancêtre de Y et X est parent de Z.
<br> Les deux définitions sont identiques, mais au point de vu de prolog, ce n'est pas exactement pareil. Prolog étudie les clauses dans l'ordre, donc dans b), comme la clause qui fait la récursivité `ancetre(Z,Y)` est placé devant, alors on rentre plus tôt dans la boucle de récursion, alors premièrement, on fera plus de boucles que a), et deuxièmement, on arrive sur une boule infinie lorsqu'on aura trouvé les solutions possibles.
(essayer `ancetre(abe, X)` avec les deux versions, en activant le mode *trace*)

## Exercice 5

