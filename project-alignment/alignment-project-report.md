# Project Report - Alignment

## Baseline

### Design Experience

I spoke with my brother Jeshua. My plan is to use a list of a list to create the matrix. The way that it works is that
for unbanded alignment the first column and row are initialized to multiples of the indel penalty, 
and then each subsequent square is filled by taking the smallest value out of the upper, left or diagonal values in the
matrix, and then adding the indel penalty for l or r, or adding the match award or sub penalty for diagonal values. 
While all of this is going on another matrix of the same dimensions is being filled with the trace of where the value at
a current box came from. I'll use L, D, U to represent the three possible trace values. 


### Theoretical Analysis - Unrestricted Alignment

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Unrestricted Alignment

| Size | Time (sec) |
|------|------------|
| 500  | 0.166      |
| 1000 | 0.644      |
| 1500 | 1.47       |
| 2000 | 2.626      |
| 2500 | 9.355      |
| 3000 | 8.087      |


### Comparison of Theoretical and Empirical Results - Unrestricted Alignment

- Theoretical order of growth: O(nm) or O(n^2) if m = n
- Empirical order of growth (if different from theoretical): 


![unbanded_empirical.png](unbanded_empirical.png)

*Fill me in*

## Core

### Design Experience

*Fill me in*


### Theoretical Analysis - Banded Alignment

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Banded Alignment

| Size  | Time (sec) |
|-------|------------|
| 100   | 0.001      |
| 1000  | 0.008      |
| 5000  | 0.032      |
| 10000 | 0.063      |
| 15000 | 0.119      |
| 20000 | 0.333      |
| 25000 | 0.381      |
| 30000 | 0.433      |

### Comparison of Theoretical and Empirical Results - Banded Alignment

- Theoretical order of growth: O(kn) or O(n)
- Empirical order of growth (if different from theoretical): It is the same


![banded_empirical.png](banded_empirical.png)

*Fill me in*

### Relative Performance Of Unrestricted Alignment versus Banded Alignment

*Fill me in*


## Stretch 1

### Design Experience

*Fill me in*

### Code

```python
     # Fill me in
```

### Alignment Scores

*Fill me in*

## Stretch 2

### Design Experience

*Fill me in*

### Alignment Outcome Comparisons

##### Sequences and Alignments

*Fill me in*

##### Chosen Parameters and Better Alignments Discussion

*Fill me in*

## Project Review

*Fill me in*
