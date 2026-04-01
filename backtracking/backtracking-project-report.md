# Project Report - Backtracking

## Baseline

### Design Experience

I spoke to my brother Jeshua about my design. I understand backtracking and greedy
algorithms pretty well. For the greedy tour baseline requirements 
I will follow the instructions on the lab page and always
pick the smallest path to follow. Obviously this will lead to dead ends,
but the timer provided will help me exit the current branch if I've arrived at a 
dead end. I'll use a set to keep track of unvisited nodes, and store a solution if it
is the best I've found and also if all nodes were visited. 



### Theoretical Analysis - Greedy

#### Time 

Let's look at the annotated code:

    def greedy_tour(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
        n = len(edges)
        solutions = []
        best_score = math.inf
    
        #loop to iterate through different paths
        for i in range(n):                       #O(n), for every node 
            unvisited = set(range(n))
            tour = [i]
            unvisited.remove(i)
            while unvisited and not timer.time_out():  #O(n) in the worst case
                current = tour[-1]
                next_node = min(unvisited, key=lambda j: edges[current][j])   #O(n) for every node 
                tour.append(next_node)
                unvisited.remove(next_node)
            score = score_tour(tour, edges)  #O(n) time
    
            if not math.isinf(score):
                if best_score > score:
                    solutions.append(SolutionStats(tour, score, timer.time(), 0, 0, 0, 0, 0))
                    best_score = score
    
        return solutions

Total time complexity becomes O(n^3)

#### Space

Let's look at the annotated code for time complexity:

    def greedy_tour(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
        n = len(edges)
        solutions = []         #O(n) SolutionStats stored at worst
        best_score = math.inf
    
        #loop to iterate through different paths
        for i in range(n):
            unvisited = set(range(n))    #O(n)
            tour = [i]                      #O(n) at worst
            unvisited.remove(i)
            while unvisited and not timer.time_out():   
                current = tour[-1]
                next_node = min(unvisited, key=lambda j: edges[current][j])
                tour.append(next_node)
                unvisited.remove(next_node)
            score = score_tour(tour, edges)
    
            if not math.isinf(score):
    
                if best_score > score:
                    solutions.append(SolutionStats(tour, score, timer.time(), 0, 0, 0, 0, 0))  #O(n) for every solutionStats
                    best_score = score
    
        return solutions

Because every solution stat can hold up to O(n) complexity, and we can store up to O(n) solutions, space complexity is 
O(n^2)

### Empirical Data - Greedy

| Size | Reduction | Time (sec) |
|------|-----------|------------|
| 5    | 0         | 0.0        |
| 10   | 0         | 0.0        |
| 15   | 0         | 0.0        |
| 20   | 0         | 0.001      |
| 25   | 0         | 0.001      |
| 30   | 0         | 0.002      |
| 35   | 0         | 0.002      |
| 40   | 0         | 0.003      |
| 45   | 0         | 0.005      |
| 50   | 0         | 0.006      |

### Comparison of Theoretical and Empirical Results - Greedy


![empirical_greed.png](empirical_greed.png)


- Theoretical order of growth: O(n^3)
- Empirical order of growth (if different from theoretical): Looks like O(n^2)

There is a slight difference between the values in the empirical data and the theoretical order of growth. This could
simply be due to noise considering how small the n values are. If we compared the runtimes of bigger n values the data
could come closer to the theoretical. 

## Core

### Design Experience

*Fill me in*

### Theoretical Analysis - Backtracking

#### Time 

*Fill me in*

#### Space

*Fill me in*

### Empirical Data - Backtracking

| N   | reduction | time (ms) |
|-----|-----------|-----------|
| 5   | 0         |           |
| 10  | 0         |           |
| 15  | 0         |           |
| 20  | 0         |           |
| 25  | 0         |           |
| 30  | 0         |           |
| 35  | 0         |           |
| 40  | 0         |           |
| 45  | 0         |           |
| 50  | 0         |           |

### Comparison of Theoretical and Empirical Results - Backtracking

- Theoretical order of growth: 
- Empirical order of growth (if different from theoretical): 

### Greedy v Backtracking

*Fill me in*

### Water Bottle Scenario 

#### Scenario 1

**Algorithm:** 

*Fill me in*

#### Scenario 2

**Algorithm:** 

*Fill me in*

#### Scenario 3

**Algorithm:** 

*Fill me in*


## Stretch 1

### Design Experience

*Fill me in*

### Demonstrate BSSF Backtracking Works Better than No-BSSF Backtracking 

*Fill me in*

### BSSF Backtracking v Backtracking Complexity Differences

*Fill me in*

### Time v Solution Cost

![Plot]()

*Fill me in*

## Stretch 2

### Design Experience

*Fill me in*

### Cut Tree

*Fill me in*

### Plots 

*Fill me in*

## Project Review

*Fill me in*
