LRC - TME 4
===========
**Ruizheng Xu 21111473**
-----------------------

# 2 / Exercices
## Exercice 1

#### Calculs à la main :

1/ `[a, [b, c], d] = [X].`  
  false  
2/ `[a, [b, c], d] = [X, Y, Z].`  
  X = a, Y = [b, c], Z = d  
3/ `[a, [b, c], d] = [a | L].`  
  false  
4/ `[a, [b, c], d] = [X, Y].`  
  false  
5/ `[a, [b, c], d] = [X | Y].`  
  false
6/ `[a, [b, c], d] = [a, b | L].`  
  false  
7/ `[a, b, [c, d]] = [a, b | L].`  
  a, b, L = [c, d]  
8/ `[a, b, c, d | L1] = [a, b | L2].`  
  false

#### Vérification des résultats :

1/ `[a, [b, c], d] = [X].`  
  false  
2/ `[a, [b, c], d] = [X, Y, Z].`  
  X = a,  
  Y = [b, c],  
  Z = d.  
3/ `[a, [b, c], d] = [a | L].`  
  L = [[b, c], d].  
4/ `[a, [b, c], d] = [X, Y].`  
  false  
5/ `[a, [b, c], d] = [X | Y].`  
  X = a,  
  Y = [[b, c], d].  
6/ `[a, [b, c], d] = [a, b | L].`  
  false  
7/ `[a, b, [c, d]] = [a, b | L].`  
  L = [c, d]  
8/ `[a, b, c, d | L1] = [a, b | L2].`  
  L2 = [c, d | L1].

## Exercice 2

1. `concatene([], L, L).`  
`concatene([X | L1], L2, [X | Lres]) :- concatene(L1, L2, Lres).`

?- concatene([a,b,c],[d],L2).
L2 = [a, b, c, d].

2. `inverse([], []).`  
`inverse([X | L1], L3) :- inverse(L1, L2), concatene(L2, [X], L3).`  

?- inverse([a,b,c,d],L2).
L2 = [d, c, b, a].

3. `supprime([], X, []).`  
`supprime([X | L1], X, L2) :- supprime(L1, X, L2).`  
`supprime([X | L1], Y, L3) :- X \= Y, supprime(L1, Y, L2), concatene([X], L2, L3).`

?- supprime([a,b,a,c], a, L).
L = [b, c] .

4. `filtre([], X, []).`   
`filtre(X, [], X).`    
`filtre(L1, [X | L2], L4) :- supprime(L1, X, L3), filtre(L3, L2, L4).`   

?- filtre([1,2,3,4,2,3,4,2,4,1],[2,4], L).
L = [1, 3, 3, 1] 

## Exercice 3

1. `palindrome(L) :- reverse(L, L).`  

?- palindrome([l,a,v,a,l]).
true.

?- palindrome([n,a,v,a,l]).
false.

2. `palindrome2([]).`
`palindrome2([_]).`
`palindrome2([X | L1]) :- append(L2, [X], L1), palindrome2(L2).`

?- palindrome2([e,s,o,p,e,r,e,s,t,e,i,c,i,e,t,s,e,r,e,p,o,s,e]).
true .

?- palindrome2([n,a,v,a,l]).
false.