import json
import matplotlib.pyplot as plt


def main():

    # COMMENT AND UNCOMMENT appropriate lines as necessary

    filename = "_b_and_b_runtimes.json"

    with open(filename, "r") as f:
        runtimes = json.load(f)

    # FILL THIS IN with your theoretical time complexity
    def theoretical_big_o(n):
        return n^3 * 3^n

    # FILL THIS IN from result using compute_coefficient
    coeff = 0.00179826815923055


    NN, times = zip(*runtimes)
    nn = [n[0] for n in NN]

    # Plot empirical values
    fig = plt.figure()
    plt.scatter(nn, times, marker="o")
    predicted_runtime = [coeff * theoretical_big_o(*n) for n, _ in runtimes]

    # Plot theoretical fit
    plt.plot(nn, predicted_runtime, c="k", ls=":", lw=2, alpha=0.5)

    # Update title, legend, and axis labels as needed
    plt.legend(["Observed", "Theoretical O(n^3*3^n)"])
    plt.xlabel("n")
    plt.ylabel("Runtime (sec)")
    plt.title("Time for Branch and Bound")

    fig.show()
    fig.savefig("empirical.png")


if __name__ == "__main__":
    main()
