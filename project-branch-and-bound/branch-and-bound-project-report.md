# Project Report - Branch and Bound

## Baseline

### Design Experience

I spoke to my brother Jeshua about my reduced cost matrix algorithm. It is actually super simple, just like the homework. 
I first subtract the minimum from each element in a row of a matrix(assuming it isn't 0 or infinity), add that to the cost every time,
and then I do the same for each element in the columns after the first reductions. 
I will use a list of a list to represent the matrix, should be easy to copy and modify, although iterating through elements will
take n^2 time. I believe other than a row having inf or 0 as its min value, there's no other edge cases. Maybe a matrix that's
already reduced. 


### Theoretical Analysis - Reduced Cost Matrix

#### Time 

Let's look at the annotated code for matrix reduction:

    
    def reduce_cost_matrix(matrix: list[list[float]]) -> tuple[list[list[float]], float]:
        n = len(matrix)
        m_copy = [row[:] for row in matrix]  #O(n^2)
        total_cost = 0.0
    
        #Row reduction
        for r in range(n):           #Runs O(n) times for every row
            row_min = min(m_copy[r])   #O(n), for every n element in that row
            if row_min == math.inf:
                continue
            if row_min == 0:
                continue
            total_cost += row_min
            for c in range(n):         #O(n) once again for every element in the row
                if m_copy[r][c] != math.inf:
                    m_copy[r][c] = m_copy[r][c] - row_min
    
    
        #Column reduction
        for c in range(n):          #O(n) times
            col_min = min(m_copy[r][c] for r in range(n)) #O(n)
            if col_min == math.inf:
                continue
            if col_min == 0:
                continue
            total_cost += col_min
    
            for r in range(n):                  #O(n)
                if m_copy[r][c] != math.inf:
                    m_copy[r][c] = m_copy[r][c] - col_min
    
    
        return m_copy, total_cost

We have O(n^2) for copy, and 2*O(n)*(O(n)+O(n)) for both row and col reduction. Total cost comes out to 
O(n^2).

#### Space

Let's look at the annotated code:

    
    def reduce_cost_matrix(matrix: list[list[float]]) -> tuple[list[list[float]], float]:
        n = len(matrix)               O(n)
        m_copy = [row[:] for row in matrix]  O(n^2) 
        total_cost = 0.0
    
        #Row reduction
        for r in range(n):
            row_min = min(m_copy[r])
            if row_min == math.inf:
                continue
            if row_min == 0:
                continue
            total_cost += row_min
            for c in range(n):
                if m_copy[r][c] != math.inf:
                    m_copy[r][c] = m_copy[r][c] - row_min
    
    
        #Column reduction
        for c in range(n):
            col_min = min(m_copy[r][c] for r in range(n))
            if col_min == math.inf:
                continue
            if col_min == 0:
                continue
            total_cost += col_min
    
            for r in range(n):
                if m_copy[r][c] != math.inf:
                    m_copy[r][c] = m_copy[r][c] - col_min
    
    
        return m_copy, total_cost

The copied matrix dominates the space complexity, leading to a O(n^2) complexity. 

## Core

### Design Experience

*Fill me in*

### Theoretical Analysis - Branch and Bound TSP

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data

| N   | time (ms) |
|-----|-----------|
| 5   |           |
| 10  |           |
| 15  |           |
| 20  |           |
| 30  |           |
| 50  |           |

### Comparison of Theoretical and Empirical Results

- Empirical order of growth: 
- Measured constant of proportionality: 

![img](img.png)

*Fill me in*

## Stretch 1 

### Design Experience

*Fill me in*

### Search Space Over Time

![Plot demonstrating search space explored over time]()

*Fill me in*

## Stretch 2

### Design Experience

*Fill me in*

### Selected PQ Key

*Fill me in*

### Branch and Bound versus Smart Branch and Bound

*Fill me in*

## Project Report 

*Fill me in*

