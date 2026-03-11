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
        trace = [[None] * (m + 1) for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[0][j] = j * indel_penalty
            trace[0][j] = "L"
        for i in range(1, n + 1):
            dp[i][0] = i * indel_penalty
            trace[i][0] = "U"
    else:
        band = 2 * banded_width + 1
        dp = [[math.inf] * band for _ in range(n + 1)]
        trace = [[None] * band for _ in range(n + 1)]
        dp[0][banded_width] = 0
        for col in range(1, banded_width + 1):
            dp[0][banded_width + col] = col * indel_penalty
            trace[0][banded_width + col] = "L"
        for i in range(1, banded_width + 1):
            dp[i][banded_width - i] = i * indel_penalty
            trace[i][banded_width - i] = "U"

    if banded_width == -1:
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                compute_cell(dp, trace, seq1, seq2, i, j, j, j - 1, match_award, indel_penalty, sub_penalty, up_col=j)
    else:
        for i in range(1, n + 1):
            band = 2 * banded_width + 1
            for col in range(band):
                real_j = i + col - banded_width
                if real_j < 1 or real_j > m:
                    continue
                compute_cell(dp, trace, seq1, seq2, i, col, real_j, col, match_award, indel_penalty, sub_penalty, up_col=col + 1)

    complete_seq1 = []
    complete_seq2 = []
    i = n
    if banded_width == -1:
        j = m
        while i > 0 or j > 0:
            if trace[i][j] == "D":
                complete_seq1.append(seq1[j - 1])
                complete_seq2.append(seq2[i - 1])
                i -= 1
                j -= 1
            elif trace[i][j] == "U":
                complete_seq1.append(gap)
                complete_seq2.append(seq2[i - 1])
                i -= 1
            elif trace[i][j] == "L":
                complete_seq1.append(seq1[j - 1])
                complete_seq2.append(gap)
                j -= 1
        cost = dp[n][m]
    else:
        band = 2 * banded_width + 1
        col = m - n + banded_width
        while i > 0 or (i + col - banded_width) > 0:
            real_j = i + col - banded_width
            if trace[i][col] == "D":
                complete_seq1.append(seq1[real_j - 1])
                complete_seq2.append(seq2[i - 1])
                i -= 1
            elif trace[i][col] == "U":
                complete_seq1.append(gap)
                complete_seq2.append(seq2[i - 1])
                i -= 1
                col += 1
            else:
                complete_seq1.append(seq1[real_j - 1])
                complete_seq2.append(gap)
                col -= 1
            if i == 0 and (i + col - banded_width) <= 0:
                break
        cost = dp[n][m - n + banded_width]

    complete_seq1 = "".join(reversed(complete_seq1))
    complete_seq2 = "".join(reversed(complete_seq2))
    return cost, complete_seq1, complete_seq2


def compute_cell(
        dp: list[list[int]],
        trace: list[list[str | None]],
        seq1: str,
        seq2: str,
        i: int,
        col: int,
        real_j: int,
        diag_col: int,
        match_award: int,
        indel_penalty: int,
        sub_penalty: int,
        up_col: int,
) -> None:
    diff = match_award if seq1[real_j - 1] == seq2[i - 1] else sub_penalty
    width = len(dp[0])

    diag = diff + dp[i - 1][diag_col]           if i > 0                      else math.inf
    up   = indel_penalty + dp[i - 1][up_col]    if i > 0 and up_col < width   else math.inf
    left = indel_penalty + dp[i][col - 1]        if col > 0                    else math.inf

    best = min(diag, up, left)
    dp[i][col] = best
    trace[i][col] = "D" if best == diag else ("U" if best == up else "L")


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
    :param seq2: the second sequence to align; should be on the "top" of the parameter
    :param match_award: how many points to award a match
    :param indel_penalty: how many points to award a gap in either sequence
    :param sub_penalty: how many points to award a substitution
    :param banded_width: banded_width * 2 + 1 is the width of the banded alignment; -1 indicates full alignment
    :param gap: the character to use to represent gaps in the alignment strings
    """

    return 0, "", ""