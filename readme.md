#Python-count-csv

##Purpose

The goal of this tiny code is to provide a module to covert a column with a lot of occurence of several items into a csv with two columns.
The first column contains the item and the second contain the number of instances of each item

##Example

For example, if the input file is 

```csv
Z
A
I
J
K
L
M
P
M
O
O
I
T
R
E
A
T
T
H
U
M
```

the output file is:

```csv
A;2
E;1
I;2
H;1
K;1
J;1
M;3
L;1
O;2
P;1
R;1
U;1
T;3
Z;1
```

## How to use

To use it, add the input.csv file in the repo.
Then run :

```bash
python run.py
```

The terminal will ask you the name of both input and output file:

```bash
Enter input file : input.csv
Enter output file : output.csv
```





