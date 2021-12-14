# LRC - TME 8
-----------------------
#### Ruizheng Xu 21111473  
-----------------------

## Exercice 1

#### Question 1

```
*TME7hexa> model0
Mo [('r','v','j'),('r','j','v'),('j','r','v'),('j','v','r'),('v','r','j'),('v','j','r')] [a,b,c] [] [(a,[[('r','v','j'),('r','j','v')],[('j','r','v'),('j','v','r')],[('v','r','j'),('v','j','r')]]),(b,[[('r','v','j'),('j','v','r')],[('r','j','v'),('v','j','r')],[('v','r','j'),('j','r','v')]]),(c,[[('r','v','j'),('v','r','j')],[('j','v','r'),('v','j','r')],[('j','r','v'),('r','j','v')]])] []
```

#### Question 2

i)

```
*TME7hexa> upd_pa model0 (Kn a holds_b_verte)
Mo [] [a,b,c] [] [(a,[]),(b,[]),(c,[])] []
```

**Une annonce publique a pour effet d'éliminer les mondes dans lesquels la formule annoncée est fausse.**
Donc comme a ne sait pas que b possède la carte verte, alors la formule est fausse dans tous les mondes, donc tous les mondes sont éliminés.

ii)

```
*TME7hexa> upd_pa model0 (Ng (Kn a holds_b_verte))
Mo [('r','v','j'),('r','j','v'),('j','r','v'),('j','v','r'),('v','r','j'),('v','j','r')] [a,b,c] []
[(a,[[('r','v','j'),('r','j','v')],[('j','r','v'),('j','v','r')],[('v','r','j'),('v','j','r')]]),
(b,[[('r','v','j'),('j','v','r')],[('r','j','v'),('v','j','r')],[('v','r','j'),('j','r','v')]]),
(c,[[('r','v','j'),('v','r','j')],[('j','v','r'),('v','j','r')],[('j','r','v'),('r','j','v')]])] []
```

a annonce une information qui est vrai partout dans tous les mondes, car il ne peut pas savoir que b possède la carte verte ou pas, donc aucun monde n'est éliminé.

#### Question 3

i)

Les trois formules à appliquer sont :

- `upd_pa model0 (Kn b (Ng holds_b_jaune))`
- `upd_pa model0 (Ng (Kn a holds_b_rouge))`
- `upd_pa model0 (Kn a (Ng holds_a_jaune))`

Pour appliquer une séquence d'annonces, on doit créer des nouvelles variables.

```
*TME7hexa> let m1 = upd_pa model0 (Kn b (Ng holds_b_jaune))
*TME7hexa> let m2 = upd_pa m1 (Ng (Kn a holds_b_rouge))
*TME7hexa> upd_pa m2 (Kn a (Ng holds_a_jaune))
Mo [('r','v','j')] [a,b,c] [] 
[(a,[[('r','v','j')]]),
(b,[[('r','v','j')]]),
(c,[[('r','v','j')]])] []
```

On arrive alors dans une situation où personne hésite (on ne possède plus qu'un seul monde), et tous les agents savent que a a la carte rouge, b a la carte verte et c a la carte jaune.

ii)

La séquence d'annonces :
- `upd_pa model0 (Kn c (Ng holds_c_jaune))`
- `upd_pa model0 (Ng (Kn a (Kn b holds_b_jaune)))`
- `upd_pa model0 (Kn c (Ng holds_b_verte))`

Application :
```
let m1 = upd_pa model0 (Kn c (Ng holds_c_jaune))
let m2 = upd_pa m1 (Ng (Kn a (Kn b holds_b_jaune)))
upd_pa m2 (Kn c (Ng holds_b_verte))

*TME7hexa> let m1 = upd_pa model0 (Kn c (Ng holds_c_jaune))
*TME7hexa> let m2 = upd_pa m1 (Ng (Kn a (Kn b holds_b_jaune)))
*TME7hexa> upd_pa m2 (Kn c (Ng holds_b_verte))
Mo [('j','r','v')] [a,b,c] []
 [(a,[[('j','r','v')]]),
 (b,[[('j','r','v')]]),
 (c,[[('j','r','v')]])] []
```

Après la première annonce, tout le monde sait que c ne possède pas la carte jaune, donc les mondes où c possède la carte jaune s'éliminent, il reste plus que `[('r','j','v'),('j','r','v'),('j','v','r'),('v','j','r')]`.
Ensuite, a annonce qu'il ne sait pas que b sait qu'il possède la carte jaune, donc cette annonce élimine les mondes où a sait que b sait qu'il possède la carte jaune (plus explicite, les mondes où b a la carte jaune sont éliminés), donc il reste plus que `[('j','r','v'),('j','v','r')]`.
Enfin, c annonce qui'il sait que b ne possède pas la carte verte, donc le seul monde où b possède la carte verte s'élimine, et il nous reste un seul monde `('j', 'r', 'v')`. Donc tout le monde connaît la carte que les autres possèdent avec a qui a la carte jaune, b qui a la carte rouge et c qui a la carte verte.

#### Question 4

L'ordre de l'annonce ne devrait pas impacté le résultat puisque chaque annonce est indépendante.

On change l'ordre de la séquence de la question 3) ii):
```
let m1 = upd_pa model0 (Kn c (Ng holds_b_verte))
let m2 = upd_pa m1 (Kn c (Ng holds_c_jaune))
upd_pa m2 (Ng (Kn a (Kn b holds_b_jaune)))

*TME7hexa> let m1 = upd_pa model0 (Kn c (Ng holds_b_verte))
*TME7hexa> let m2 = upd_pa m1 (Kn c (Ng holds_c_jaune))
*TME7hexa> upd_pa m2 (Ng (Kn a (Kn b holds_b_jaune)))
Mo [('j','r','v')] [a,b,c] [] 
[(a,[[('j','r','v')]]),
(b,[[('j','r','v')]]),
(c,[[('j','r','v')]])] []
```

On obtient bien le même résultat.

## Exercice 2

#### Question 1

```
*TME7cheryl> model0
Mo [(15,"May"),(16,"May"),(19,"May"),(17,"June"),(18,"June"),(14,"July"),(16,"July"),(14,"August"),(15,"August"),(17,"August")] [a,b] [] 
[(a,[[(15,"May"),(16,"May"),(19,"May")],[(17,"June"),(18,"June")],[(14,"July"),(16,"July")],[(14,"August"),(15,"August"),(17,"August")]]),
(b,[[(14,"July"),(14,"August")],[(15,"May"),(15,"August")],[(16,"May"),(16,"July")],[(17,"June"),(17,"August")],[(18,"June")],[(19,"May")]])] []
```

#### Question 2

Le code est implémenté comme suit :
```
knWhich :: Agent -> Form (Int, [Char])
knWhich i = Disj [ Kn i (Info s) | s <- allDays ]
```

Pour indiquer que l'agent ***i*** connaît une date d'anniversaire, il faut taper `knWhich i`.

#### Question 3

i)

Albert annonce qu'il ne sait pas quelle est date d'anniversaire : `let m1 = upd_pa model0 (Ng (knWhich a))`, mais il sait que Bernard ne sait pas non plus : `let m2 = upd_pa m1 (Kn a (Ng (knWhich b)))`

```
*TME7cheryl> let m1 = upd_pa model0 (Ng (knWhich a))
*TME7cheryl> let m2 = upd_pa m1 (Kn a (Ng (knWhich b)))
*TME7cheryl> m2
Mo [(14,"July"),(16,"July"),(14,"August"),(15,"August"),(17,"August")] [a,b] []
 [(a,[[(14,"July"),(16,"July")],[(14,"August"),(15,"August"),(17,"August")]]),
 (b,[[(14,"July"),(14,"August")],[(15,"August")],[(16,"July")],[(17,"August")]])] []
```

On remarque que toutes les dates du mois de Mai et de Juin sont éliminées. Car Albert annonce qu'il sait que Bernard ne sait pas la date d'anninversaire, donc on doit éliminer les dates où Albert ne sait pas que Bernard ne sait pas. Ainsi, Albert hésite entre les dates du mois de Mai, et il ne peut pas savoir que Bernard ne sait pas la date puisque 19 Mai est une date que Bernard n'hésite pas, donc le mois de Mai doit être éliminé.
Même intuition pour le mois de Juin.

ii)

Bernard annonce maintenant qu'il sait la date d'anniversaire : `let m3 = upd_pa m2 (knWhich b)`

```
*TME7cheryl> let m3 = upd_pa m2 (knWhich b)
*TME7cheryl> m3
Mo [(16,"July"),(15,"August"),(17,"August")] [a,b] [] 
[(a,[[(16,"July")],[(15,"August"),(17,"August")]]),
(b,[[(15,"August")],[(16,"July")],[(17,"August")]])] []
```

iii)

Enfin, Albert annonce aussi qu'il sait la date d'anniversaire : `upd_pa m3 (knWhich a)`

```
*TME7cheryl> upd_pa m3 (knWhich a)
Mo [(16,"July")] [a,b] [] [(a,[[(16,"July")]]),(b,[[(16,"July")]])] []
```

Donc la date d'anniversaire de Cheryl est le 16 Juillet.

#### Question 4

La première partie de l'annonce i) est superflue, puisqu'il est vrai que Albert ne connaît pas la date d'anninversaire, donc cette première partie de l'annonce n'élimine aucun monde.

```
*TME7cheryl> m1 == model0
True
*TME7cheryl> m2 == model0
False
```

