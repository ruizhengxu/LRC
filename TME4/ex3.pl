palindrome(L) :- reverse(L, L).

palindrome2([]).
palindrome2([_]).
palindrome2([X | L1]) :- append(L2, [X], L1), palindrome2(L2).