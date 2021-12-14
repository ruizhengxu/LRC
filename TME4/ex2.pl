concatene([], L, L).
concatene([X | L1], L2, [X | Lres]) :- concatene(L1, L2, Lres).

inverse([], []).
inverse([X | L1], L3) :- inverse(L1, L2), concatene(L2, [X], L3).

supprime([], X, []).
supprime([X | L1], X, L2) :- supprime(L1, X, L2).
supprime([X | L1], Y, L3) :- X \= Y, supprime(L1, Y, L2), concatene([X], L2, L3).

filtre([], X, []).
filtre(X, [], X).
filtre(L1, [X | L2], L4) :- supprime(L1, X, L3), filtre(L3, L2, L4).
