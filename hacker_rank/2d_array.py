# def hourglassSum(arr):
#     # Write your code here
#     max_hourglass_sum = 0
#     for line in arr:
#         for i in range(len(line)):
#             try:
#                 first_row = line[i] + line[i + 1] + line[i + 2]
#                 second_row = arr[arr.index(line) + 1][i + 1]
#                 third_row = arr[arr.index(line) + 2]
#                 third_row_value = third_row[i] + third_row[i + 1] + third_row[i + 2]
#                 hourglass_sum = first_row + second_row + third_row_value
#                 if hourglass_sum > max_hourglass_sum:
#                     max_hourglass_sum = hourglass_sum
#             except Exception:
#                 pass
#     return max_hourglass_sum


# def hourglassSum(arr):
#     max_hourglass_sum = float('-inf')  # Set initial value to negative infinity

#     for i in range(len(arr) - 2):  # Iterate over rows, leaving space for the hourglass
#         for j in range(len(arr[i]) - 2):  # Iterate over columns, leaving space for the hourglass
#             top_sum = sum(arr[i][j:j+3])
#             middle = arr[i+1][j+1]
#             bottom_sum = sum(arr[i+2][j:j+3])

#             hourglass_sum = top_sum + middle + bottom_sum

#             max_hourglass_sum = max(max_hourglass_sum, hourglass_sum)

#     return max_hourglass_sum

def hourglassSum(arr):
    # Write your code here
    max_hourglass_sum = float('-inf')
    
    for i in range(len(arr[:-2])):
        for j in range(len(arr[i][:-2])):
            top_value = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            middle_value = arr[i + 1][j + 1]
            bottom_value = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            hourglass_sum = top_value + middle_value + bottom_value
            max_hourglass_sum = max(hourglass_sum, max_hourglass_sum)
    return max_hourglass_sum


if __name__ == '__main__':
    arr = []
    arr.append([-9, -9, -9, 1, 1, 1])
    arr.append([ 0, -9, 0, 4, 3, 2])
    arr.append([-9, -9, -9, 1, 2, 3])
    arr.append([0, 0, 8, 6, 6, 0])
    arr.append([0, 0, 0, -2, 0, 0])
    arr.append([0, 0, 1, 2, 4, 0])
    print(hourglassSum(arr))



 
