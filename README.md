# Lambda-NFA-implementation

### Lambda-NFA implementation + word validation in Python

[Română :romania:](#date)

[English :eu:](#data)

# Date

Daca exista mai multe trasee posibile, se va afisa doar primul gasit.

Datele de intrare contin pe prima linie n (numarul de noduri) si m (numarul de tranzitii). 
Pe urmatoarele m linii sunt descrise tranzitiile din fiecare automat.
Pe linia m + 2 se afla indicele starii initiale. Pe linia m + 3 se afla un numar nf (numarul de stari finale) urmat de indicii starilor finale respective, separate prin spatiu.

Datele de iesire, pentru fiecare string: contin DA, daca cuvantul este acceptat si un traseu posibil, respectiv NU, in caz contrar.

Exemplu de date introduse în fisier:

```
Input:
6 8
0 1 a
0 2 #
1 1 b
1 3 #
2 2 b
2 4 c
3 5 c
4 5 c
0
1 5
4
cc
baaaabac
ac
ababaaa
```
```
Output:
DA
Traseu: 0 2 4 5
NU
DA
Traseu: 0 1 3 5
NU
```

# Data

If there are multiple possible routes, only the first one found will be displayed.

The input data contains on the first line n (the number of nodes) and m (the number of transitions).
On the following m lines, the transitions of each automaton are described.
On line m + 2 is the index of the initial state. On line m + 3 is a number nf (the number of final states) followed by the indices of the final states, separated by a space.
Line m+ 4 contains ni, the number of input strings, and on the following ni lines, the strings themselves.

The output data, for each string: contains YES, if the word is accepted and a possible route, or NO, otherwise.

Example input data in file:

```
Input:
6 8
0 1 a
0 2 #
1 1 b
1 3 #
2 2 b
2 4 c
3 5 c
4 5 c
0
1 5
4
cc
baaaabac
ac
ababaaa
```
```
Output:
DA
Traseu: 0 2 4 5
NU
DA
Traseu: 0 1 3 5
NU
```
