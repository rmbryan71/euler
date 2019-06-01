from itertools import accumulate
# https://docs.python.org/3/library/itertools.html#itertools.accumulate

def walk_matrix(matrix):
    """Step through given matrix, print coordinates and value."""
    if not matrix:
        return 0

    size = len(matrix)

    for i in range(1, size):
        for j in range(1, size):
            print('At x = ', i, ' and y = ', j, ' matrix value is ', matrix[i][j])

def min_path_sum(matrix):
    size = len(matrix)

    rows = iter(matrix)
    best = list(accumulate(next(rows)))

    for row in rows:
        best[0] += row[0]
        for j in range(1, len(row)):
            best[j] = row[j] + min(best[j-1], best[j])
    return best[-1]


if __name__ == '__main__':
    with open("p081_matrix.txt") as file:
        matrix = [
            [int(n) for n in line.strip().split(',')] for line in file
        ]
    print(min_path_sum(matrix))
