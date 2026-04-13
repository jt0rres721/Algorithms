import json
import matplotlib.pyplot as plt
from byu_pytest_utils import compute_average_runtimes

# Load and average both runtime files
with open("_greedy_runtimes.json", "r") as f:
    greedy_runtimes = json.load(f)

with open("_backtracking_runtimes.json", "r") as f:
    backtracking_runtimes = json.load(f)

greedy_avg = compute_average_runtimes(greedy_runtimes)
backtracking_avg = compute_average_runtimes(backtracking_runtimes)

# Extract sizes and times
greedy_sizes = [entry[0] for entry in greedy_avg]
greedy_times = [entry[2] for entry in greedy_avg]

backtracking_sizes = [entry[0] for entry in backtracking_avg]
backtracking_times = [entry[2] for entry in backtracking_avg]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(greedy_sizes, greedy_times, marker='o', label='Greedy')
plt.plot(backtracking_sizes, backtracking_times, marker='o', label='Backtracking')

plt.xlabel('Problem Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Greedy vs Backtracking: Size vs Runtime')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('greedy_vs_backtracking.png')
plt.show()