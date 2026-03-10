import math

def align(
    seq1: str,
    seq2: str,
    match_award=-3,
    indel_penalty=5,
    sub_penalty=1,
    banded_width=-1,
    gap="-",
) -> tuple[float, str | None, str | None]:
    """
    Align seq1 against seq2 using Needleman-Wunsch
    Put seq1 on left (j) and seq2 on top (i)
    => matrix[i][j]
    :param seq1: the first sequence to align; should be on the "left" of the matrix
    :param seq2: the second sequence to align; should be on the "top" of the matrix
    :param match_award: how many points to award a match
    :param indel_penalty: how many points to award a gap in either sequence
    :param sub_penalty: how many points to award a substitution
    :param banded_width: banded_width * 2 + 1 is the width of the banded alignment; -1 indicates full alignment
    :param gap: the character to use to represent gaps in the alignment strings
    """
    m = len(seq1)
    n = len(seq2)

    if banded_width != -1 and abs(n - m) > banded_width:
        return math.inf, None, None

    if banded_width == -1:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
    else:
        dp = [[math.inf] * (m + 1) for _ in range(n + 1)]

    trace =  [[None]*(m+1) for _ in range(n+1)]

    if banded_width == -1:
        for j in range(1, m + 1):
            dp[0][j] = j * indel_penalty
            trace[0][j] = "L"

        for i in range(1, n + 1):
            dp[i][0] = i * indel_penalty
            trace[i][0] = "U"
    else:
        dp[0][0] = 0


    for i in range(1, n + 1):
        if banded_width == -1:
            j_start = 1
            j_end = m
        else:
            j_start = max(1, i - banded_width)
            j_end = min(m, i + banded_width)
        for j in range(j_start, j_end + 1):
            compute_cell(dp, trace, seq1, seq2, i, j, match_award, indel_penalty, sub_penalty)

    complete_seq1 = []
    complete_seq2 = []
    i = n
    j = m
    while i > 0 or j > 0:
        if trace[i][j] == "D":
            complete_seq1.append(seq1[j-1])
            complete_seq2.append(seq2[i-1])
            i = i - 1
            j = j - 1
        elif trace[i][j] == "U":
            complete_seq1.append(gap)
            complete_seq2.append(seq2[i-1])
            i = i - 1
        elif trace[i][j] == "L":
            complete_seq1.append(seq1[j-1])
            complete_seq2.append(gap)
            j = j - 1

    complete_seq1 = "".join(reversed(complete_seq1))
    complete_seq2 = "".join(reversed(complete_seq2))
    cost = dp[n][m]

    return cost, complete_seq1, complete_seq2


def compute_cell(
        dp: list[list[int]],
        trace: list[list[str | None]],
        seq1: str,
        seq2: str,
        i: int,
        j: int,
        match_award: int,
        indel_penalty: int,
        sub_penalty: int,
) -> None:
    if seq1[j - 1] == seq2[i - 1]:
        diff = match_award
    else:
        diff = sub_penalty

    diag = diff + dp[i-1][j-1]
    up = indel_penalty + dp[i-1][j]
    left = indel_penalty + dp[i][j-1]

    best = min(diag,up,left)

    dp[i][j] = best

    if best == diag:
        trace[i][j] = "D"
    elif best == up:
        trace[i][j] = "U"
    else:
        trace[i][j] = "L"


def local_align(
    seq1: str,
    seq2: str,
    match_award=-3,
    indel_penalty=5,
    sub_penalty=3,
    banded_width=-1,
    gap="-",
) -> tuple[float, str | None, str | None]:
    """
    Align seq1 against seq2 using Smith-Waterman
    Put seq1 on left (j) and seq2 on top (i)
    => matrix[i][j]
    :param seq1: the first sequence to align; should be on the "left" of the matrix
    :param seq2: the second sequence to align; should be on the "top" of the matrix
    :param match_award: how many points to award a match
    :param indel_penalty: how many points to award a gap in either sequence
    :param sub_penalty: how many points to award a substitution
    :param banded_width: banded_width * 2 + 1 is the width of the banded alignment; -1 indicates full alignment
    :param gap: the character to use to represent gaps in the alignment strings
    """

    return 0, "", ""
