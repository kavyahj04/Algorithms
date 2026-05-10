def binarySearch2DMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        if target > matrix[row][col]:
            left = mid + 1
        elif target < matrix[row][col]:
            right = mid - 1
        else:
            print("True")
            return True
    print("False")
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 4

binarySearch2DMatrix(matrix, target)