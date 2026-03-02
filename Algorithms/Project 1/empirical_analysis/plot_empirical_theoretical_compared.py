import json
import matplotlib.pyplot as plt


def main():

    # COMMENT AND UNCOMMENT appropriate lines as necessary

    #filename = "_primes_runtimes.json"
    filename = '_keypairs_runtimes.json'
    # filename = '_encryption_runtimes.json'
    # filename = '_decryption_runtimes.json'

    with open(filename, "r") as f:
        runtimes = json.load(f)

    # FILL THIS IN with your theoretical time complexity
    def theoretical_big_o(n):
        return n^4

    # FILL THIS IN from result using compute_coefficient
    coeff = 0.0038364376168094783

    nn = [n for n, _ in runtimes]
    times = [t for _, t in runtimes]

    # Plot empirical values
    fig = plt.figure()
    plt.scatter(nn, times, marker="o")

    predicted_runtime = [coeff * theoretical_big_o(n) for n, t in runtimes]

    # Plot theoretical fit
    plt.plot(nn, predicted_runtime, c="k", ls=":", lw=2, alpha=0.5)

    # Update title, legend, and axis labels as needed
    plt.legend(["Observed", "Theoretical O(n^4)"])
    plt.xlabel("n")
    plt.ylabel("Runtime")
    plt.title("Time for Keypair Generation")

    fig.show()
    fig.savefig("empirical_key.svg")


if __name__ == "__main__":
    main()
