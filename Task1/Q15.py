n = int(input("Enter the size of matrix (n): "))
matrix = []
print("Enter the elements row-wise:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

print("Original Matrix:")
for row in matrix:
    print(row)

rotated = []

for j in range(n):
    new_row = []
    for i in range(n-1, -1, -1):
        new_row.append(matrix[i][j])
    rotated.append(new_row)

print("Matrix after 90° rotation:")
for row in rotated:
    print(row)
print("Spiral order of rotated matrix:")

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:
    for i in range(left, right+1):
        print(rotated[top][i], end=" ")
    top += 1

    for i in range(top, bottom+1):
        print(rotated[i][right], end=" ")
    right -= 1
    for i in range(right, left-1, -1):
        print(rotated[bottom][i], end=" ")
    bottom -= 1
    for i in range(bottom, top-1, -1):
        print(rotated[i][left], end=" ")
    left += 1




