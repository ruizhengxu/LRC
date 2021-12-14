# LRC - TME 5
-----------------------
#### Ruizheng Xu 21111473  
-----------------------

## Exercice 1

1. `subs(chat,felin).` -> `chat ⊑ felin` -> "Les chats sont des félins."
2.  `subs(chihuahua,and(chien,pet)).` ->  `chihuahua ⊑ (chien ⊓ pet)` -> "Un chihuahua est à la fois un chien et un animal de compagnie."
3.  `subs(and(animal,some(aMaitre)),pet).` -> `(animal ⊓ ∃aMaitre) ⊑ pet` -> "Un animal qui a un maître est un animal de compagnie."
4.  `subs(some(aMaitre),all(aMaitre,personne)).` -> `∃aMaitre ⊑ ∀aMaitre.personne` -> "Toute entité qui a maître ne peut avoir qu'un maître humain."
5. `subs(and(all(mange,nothing),some(mange)),nothing).` -> `(∀mange.⊥ ⊓ ∃mange) ⊑ ⊥` -> "On ne peut pas à la fois ne rien manger et manger quelque chose."
6. `equiv(carnivoreExc,all(mange,animal)).` -> `carnivoreExc ≡ ∀mange.animal` -> "Un carnivore exclusif est défini comme une entité qui mange uniquement des animaux."

## Exercice 2

```
subsS1(C,C).
subsS1(C,D):-subs(C,D),C\==D.
subsS1(C,D):-subs(C,E),subsS1(E,D).
```

#### Question 1

Ces règles mettent en place le fait qu'un concept atomique peut être subsumé par un autre, même si la règle n'est pas définit explicitement. Par exemple, sans ces règles, avec `subs(A, C). subs(B,C). subs(A,B).`, alors `subs(A,C)/` sera fausse. Mais en définissant ces règles, `subs(A,C).` sera vraie, car A est subsumé par B et que B est subsumé par C.  

Le résultat de `canari ⊑ animal` :
```
?- subsS1(canari, animal).
true.
```

Le résultat de `chat ⊑ etreVivant` :
```
?- subsS1(chat,etreVivant).
true .
```

#### Question 2

Le résulat de la requête est en-dessous. On remarque que c'est une boucle infinie. Tout d'abord, on cherche si chien est subsumé par souris, et on voit que non, alors, on cherche si canide est subsumé par souris (car chien est subsumé par canide), et c'est toujours non, puis on regarde si mammifere est susbumé par souris (car la ligne subs(canide, mammifere) est au-dessus de subs(canide, chien)), et on voit que non plus, et ainsi de suite. Lorsqu'on a exploré tous les concepts auquels mammifere est subsumé, on revient à la règle subs(canide, chien), et ainsi se forme la boucle infinie.

Le résultat de `chien ⊑ souris` :
```
[trace]  ?- subsS1(chien,souris).
   Call: (10) subsS1(chien, souris) ? creep
   Call: (11) subs(chien, souris) ? creep
   Fail: (11) subs(chien, souris) ? creep
   Redo: (10) subsS1(chien, souris) ? creep
   Call: (11) subs(chien, _4652) ? creep
   Exit: (11) subs(chien, canide) ? creep
   Call: (11) subsS1(canide, souris) ? creep
   Call: (12) subs(canide, souris) ? creep
   Fail: (12) subs(canide, souris) ? creep
   Redo: (11) subsS1(canide, souris) ? creep
   Call: (12) subs(canide, _9178) ? creep
   Exit: (12) subs(canide, mammifere) ? creep
   Call: (12) subsS1(mammifere, souris) ? creep
   Call: (13) subs(mammifere, souris) ? creep
   Fail: (13) subs(mammifere, souris) ? creep
   Redo: (12) subsS1(mammifere, souris) ? creep
   Call: (13) subs(mammifere, _13704) ? creep
   Exit: (13) subs(mammifere, animal) ? creep
   Call: (13) subsS1(animal, souris) ? creep
   Call: (14) subs(animal, souris) ? creep
   Fail: (14) subs(animal, souris) ? creep
   Redo: (13) subsS1(animal, souris) ? creep
   Call: (14) subs(animal, _18230) ? creep
   Exit: (14) subs(animal, etreVivant) ? creep
   Call: (14) subsS1(etreVivant, souris) ? creep
   Call: (15) subs(etreVivant, souris) ? creep
   Fail: (15) subs(etreVivant, souris) ? creep
   Redo: (14) subsS1(etreVivant, souris) ? creep
   Call: (15) subs(etreVivant, _22756) ? creep
   Fail: (15) subs(etreVivant, _22756) ? creep
   Fail: (14) subsS1(etreVivant, souris) ? creep
   Redo: (14) subs(animal, _18230) ? creep
   Exit: (14) subs(animal, some(mange)) ? creep
   Call: (14) subsS1(some(mange), souris) ? creep
   Call: (15) subs(some(mange), souris) ? creep
   Fail: (15) subs(some(mange), souris) ? creep
   Redo: (14) subsS1(some(mange), souris) ? creep
   Call: (15) subs(some(mange), _29548) ? creep
   Fail: (15) subs(some(mange), _29548) ? creep
   Fail: (14) subsS1(some(mange), souris) ? creep
   Fail: (13) subsS1(animal, souris) ? creep
   Fail: (12) subsS1(mammifere, souris) ? creep
   Redo: (12) subs(canide, _60) ? creep
   Exit: (12) subs(canide, chien) ? creep
   Call: (12) subsS1(chien, souris) ? creep
   Call: (13) subs(chien, souris) ? creep
   Fail: (13) subs(chien, souris) ? creep
   Redo: (12) subsS1(chien, souris) ? creep
   Call: (13) subs(chien, _5324) ? abort
```

#### Question 3

Les résultats sont bien ceux attendus. `subs(chien, souris)` nous renvoie false, car cette fois-ci on a une liste contenant des concepts déjà vu, donc, une fois qu'on arrive sur le début de la boucle infinie (`subsS(canide, chien)`), on aurait déjà vu le concept chien, et ainsi `not(member(E,L))` va renvoyer false, donc `subsS` renvera false.

```
?- subsS(chat,etreVivant).
true .

?- subsS(chien,canide).
true .

?- subsS(chien,chien).
true .

?- subsS(chien,souris).
[trace]  ?- subsS(chien,souris).
   Call: (10) subsS(chien, souris) ? creep
   Call: (11) subsS(chien, souris, [chien]) ? creep
   Call: (12) subs(chien, souris) ? creep
   Fail: (12) subs(chien, souris) ? creep
   Redo: (11) subsS(chien, souris, [chien]) ? creep
   Call: (12) subs(chien, _21768) ? creep
   Exit: (12) subs(chien, canide) ? creep
^  Call: (12) not(member(canide, [chien])) ? creep
^  Exit: (12) not(user:member(canide, [chien])) ? creep
   Call: (12) subsS(canide, souris, [canide, chien]) ? creep
   Call: (13) subs(canide, souris) ? creep
   Fail: (13) subs(canide, souris) ? creep
   Redo: (12) subsS(canide, souris, [canide, chien]) ? creep
   Call: (13) subs(canide, _27844) ? creep
   Exit: (13) subs(canide, mammifere) ? creep
^  Call: (13) not(member(mammifere, [canide, chien])) ? creep
^  Exit: (13) not(user:member(mammifere, [canide, chien])) ? creep
   Call: (13) subsS(mammifere, souris, [mammifere, canide, chien]) ? creep
   Call: (14) subs(mammifere, souris) ? creep
   Fail: (14) subs(mammifere, souris) ? creep
   Redo: (13) subsS(mammifere, souris, [mammifere, canide, chien]) ? creep
   Call: (14) subs(mammifere, _33920) ? creep
   Exit: (14) subs(mammifere, animal) ? creep
^  Call: (14) not(member(animal, [mammifere, canide, chien])) ? creep
^  Exit: (14) not(user:member(animal, [mammifere, canide, chien])) ? creep
   Call: (14) subsS(animal, souris, [animal, mammifere, canide, chien]) ? creep
   Call: (15) subs(animal, souris) ? creep
   Fail: (15) subs(animal, souris) ? creep
   Redo: (14) subsS(animal, souris, [animal, mammifere, canide, chien]) ? creep
   Call: (15) subs(animal, _39996) ? creep
   Exit: (15) subs(animal, etreVivant) ? creep
^  Call: (15) not(member(etreVivant, [animal, mammifere, canide, chien])) ? creep
^  Exit: (15) not(user:member(etreVivant, [animal, mammifere, canide, chien])) ? creep
   Call: (15) subsS(etreVivant, souris, [etreVivant, animal, mammifere, canide, chien]) ? creep
   Call: (16) subs(etreVivant, souris) ? creep
   Fail: (16) subs(etreVivant, souris) ? creep
   Redo: (15) subsS(etreVivant, souris, [etreVivant, animal, mammifere, canide, chien]) ? creep
   Call: (16) subs(etreVivant, _46072) ? creep
   Fail: (16) subs(etreVivant, _46072) ? creep
   Fail: (15) subsS(etreVivant, souris, [etreVivant, animal, mammifere, canide, chien]) ? creep
   Redo: (15) subs(animal, _39996) ? creep
   Exit: (15) subs(animal, some(mange)) ? creep
^  Call: (15) not(member(some(mange), [animal, mammifere, canide, chien])) ? creep
^  Exit: (15) not(user:member(some(mange), [animal, mammifere, canide, chien])) ? creep
   Call: (15) subsS(some(mange), souris, [some(mange), animal, mammifere, canide, chien]) ? creep
   Call: (16) subs(some(mange), souris) ? creep
   Fail: (16) subs(some(mange), souris) ? creep
   Redo: (15) subsS(some(mange), souris, [some(mange), animal, mammifere, canide, chien]) ? creep
   Call: (16) subs(some(mange), _54418) ? creep
   Fail: (16) subs(some(mange), _54418) ? creep
   Fail: (15) subsS(some(mange), souris, [some(mange), animal, mammifere, canide, chien]) ? creep
   Fail: (14) subsS(animal, souris, [animal, mammifere, canide, chien]) ? creep
   Fail: (13) subsS(mammifere, souris, [mammifere, canide, chien]) ? creep
   Redo: (13) subs(canide, _27844) ? creep
   Exit: (13) subs(canide, chien) ? creep
^  Call: (13) not(member(chien, [canide, chien])) ? creep
^  Fail: (13) not(user:member(chien, [canide, chien])) ? creep
   Fail: (12) subsS(canide, souris, [canide, chien]) ? creep
   Fail: (11) subsS(chien, souris, [chien]) ? creep
   Fail: (10) subsS(chien, souris) ? creep
false.
```

#### Question 4

La requête `souris ⊑ ∃mange` marche car on a définit la règle `subs(animal, some(mange))`, et comme souris subsumé par mammifere, mammifere subsumé par animal et animal par some(mange), alors la requête renvoie vrai.

```
?- subsS(souris,some(mange)).
true .
```

#### Question 5

La requête `chat ⊑ X` devrait renvoyer : **[felin]** pour `subs(chat, X)` et **[felin, mammifere, animal, etreVivant, some(mange)]** pour `subsS(chat, X)`. Et `X ⊑ mammifere` devrait renvoyer : **[felin, canide, souris]** pour `subs(X, mammifere)` et **[felin, chat, lion, canide, chien]** pour `subsS(X, mammifere)`.

Vérification : 

```
?- subsS(chat,X).
X = chat .

?- subsS(chat,X).
X = chat ;
X = felin ;
X = mammifere ;
X = animal ;
X = etreVivant ;
X = some(mange) ;

?- subs(X,mammifere).
X = felin ;
X = canide ;
X = souris.

?- subsS(X,mammifere).
X = mammifere ;
X = felin ;
X = canide ;
X = souris ;
X = chat ;
X = chien ;
X = lion ;
```

<u>Remarque</u> : l'ordre des résultats que j'ai écrit (**[felin, chat, lion, canide, chien]**) ne correspond pas à ce qu'on obtient (**[mammifere, felin, canide, souris, chat, chien, lion]**), et j'ai oublié le que le concept est subsumé par lui-même dans les deux requêtes.

#### Question 6

On rajoute les règles suivantes : ```subs(C,D):-equiv(C,D). | subs(C,D):-equiv(D,C).```, ainsi la requête `lion ⊑ ∀mange.animal` devrait renvoyer vrai.

Vérification :

```
Avant l'ajout des règles :
?- subsS(lion, all(mange,animal)).
false.

Après l'ajout des règles :
?- subsS(lion, all(mange,animal)).
true.
```

## Exercice 3

#### Question 1

```
?- subsS(chihuahua, and(mammifere, some(aMaitre))).
true.

?- subsS(and(chien, some(aMaitre)), pet).
true.

?- subsS(chihuahua, and(pet, chien)).
true.
```

#### Question 2

Les règles ajoutées sont : 

```
1 - subsS(C,and(D1,D2),L):-D1\=D2,subsS(C,D1,L),subsS(C,D2,L).
2 - subsS(C,D,L):-subs(and(D1,D2),D),E=and(D1,D2),not(member(E,L)), subsS(C,E,[E|L]),E\==C.
3 - subsS(and(C,C),D,L):-nonvar(C),subsS(C,D,[C|L]).
4 - subsS(and(C1,C2),D,L):-C1\=C2,subsS(C1,D,[C1|L]).
5 - subsS(and(C1,C2),D,L):-C1\=C2,subsS(C2,D,[C2|L]).
6 - subsS(and(C1,C2),D,L):-subs(C1,E1),E=and(E1,C2),not(member(E,L)),subsS(E,D,[E|L]),E\==D.
7 - subsS(and(C1,C2),D,L):-Cinv=and(C2,C1),not(member(Cinv,L)),subsS(Cinv,D,[Cinv|L]).
```

La règle 1 ==> Si C est subsumé par D1 et subsumé par D2, alors C est subsumé par C et D. Et la reègle est traitée lorsqu'on a une requête de type `subsS(chihuahua, and(mammifere, some(aMaitre))).`. Car chihuahua est subsumé par mammifere et par some(aMaitre), alors chihuahua est subsumé par l'intersection des deux concepts.

La règle 2 ==> L'intersection de D1 et D2 (E) est subsumé par D, et que C est subsumé par E, alors C est subsumé par D (C ⊑ E et E ⊑ D alors C ⊑ D, règle de transitivité). La règle est traité lorsqu'on une requête de type `subsS(chihuahua, pet)`. chihuahua (C) est subsumé par chien et pet, et chien subsumé par animal, et on a aussi animal et pet subsumé par pet.

La règle 3 ==> Si C est subsumé par D ,alors l'intersection du C et C est aussi subsumé par D. La règle est traité par une requête de type `subsS(and(chat, chat), felin)`.

La règle 4 et 5 ==> Si C1 est subsumé par D et C2 est subsumé par D, alors l'intersection de C1 et C2 est subsumé par D. La règle est traitée par des requête de type `subsS(and(lion, chat), felin).`.

La règle 6 ==> Si C1 est subsumé par E1, et E (E1 ⊓ C2) subsumé par D, alors C1 ⊓ C2 subsumé par D. Plus intuitivement, si D subsume l'intersection de deux concepts, alors D subsume aussi n'importe quel concept qui est subsumé par les concepts de cet intersection. La règle est traitée par des requête de type `subsS(and(chien, some(aMaitre)), pet).`.

La règle 7 ==> Si D subsume l'intersection de deux concepts, alors il subsume l'intersection de ces concepts peu importe leur ordre dans l'intersection (C1 ⊓ C2 ou C2 ⊓ C1).

## Exercice 4

#### Question 1

La règle à ajouter : `subsS(all(R,C),all(R,D), _):-subs(C,D).`

```
?- subsS(lion, all(mange, etreVivant)).
true .
```