/* * * * * *
 *
 * EXERCICE 4
 *
 * * * * * */

pere(abe, homer).
pere(homer, lisa).
pere(homer, bart).
pere(homer, maggie).
mere(marge, lisa).
mere(marge, bart).
mere(marge, maggie).
parent(X,Y) :- mere(X,Y).
parent(X,Y) :- pere(X,Y).

/*
?- parent(X,bart).
X = marge ;
X = homer.

?- parent(bart,X).
false.

?- parent(marge,Y).
Y = lisa ;
Y = bart ;
Y = maggie ;
false.

?- parent(A,B).
A = marge,
B = lisa ;
A = marge,
B = bart ;
A = marge,
B = maggie ;
A = homer,
B = lisa ;
A = homer,
B = bart ;
A = homer,
B = maggie.s
*/

parents(X,Y,Z) :- pere(X,Z), mere(Y,Z).

/*
?- parents(X,marge,Y).
X = homer,
Y = lisa ;
X = homer,
Y = bart ;
X = homer,
Y = maggie.
*/

grandPere(X,Z) :- pere(X,Y), pere(Y,Z).
grandPere(X,Z) :- pere(X,Y), mere(Y,Z).
frereOuSoeur(Y,Z) :- pere(XY,Y), pere(XY,Z), mere(XX,Y), mere(XX,Z), Y\==Z.
/* definir frereOuSoeur de cette maniere permet d'eviter les doublons
et que une personne ne soit pas son.sa propre frereOuSoeur.
On différencie donc les demi-frereOuSoeurs et les frereOuSoeurs */

/*
?- grandPere(X,marge).
false.

?- grandPere(X,bart).
X = abe .

?- grandPere(X,Y).
X = abe,
Y = lisa ;
X = abe,
Y = bart ;
X = abe,
Y = maggie ;

?- frereOuSoeur(X,maggie).
X = lisa ;
X = bart ;
*/

ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).
/* importance de l'ordre des prédicats */

/*
ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- parent(X,Z), ancetre(Z,Y).

?- ancetre(abe,Y).
Y = homer ;
Y = lisa ;
Y = bart ;
Y = maggie ;
*/



/*
ancetre(X,Y) :- parent(X,Y).
ancetre(X,Y) :- ancetre(Z,Y), parent(X,Z).

à tester
*/
