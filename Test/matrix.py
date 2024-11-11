# input:
# 1 2 3
# 4 5 6
# 7 8 9

# output:
# 7 4 1
# 8 5 2
# 9 6 3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

rotated_matrix = rotate_matrix(matrix)

# Print the output
for row in rotated_matrix:
    print(' '.join(map(str, row)))
