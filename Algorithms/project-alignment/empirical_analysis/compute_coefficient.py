from byu_pytest_utils import compute_coefficient


def main():

    # COMMENT AND UNCOMMENT appropriate lines as necessary

    filename = "_unbanded_align_runtimes.json"
    # filename = "_banded_align_runtimes.json"

    def theoretical_big_o(n):
        # FILL THIS IN with your theoretical time complexity
        return 1

    # Changing these values takes a slice of your runtimes corresponding with the indices

    start = None
    end = None

    compute_coefficient(filename, theoretical_big_o, start, end)


if __name__ == "__main__":
    main()
