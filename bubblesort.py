my_array = [7,6,5,4,4,7,4]

n = len(my_array)
# print(n)
# print(n-1)
for i in range(n-1):
    # print(n-i-1)
    for j in range(n-i-1):
        print(j)
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            print(my_array)

print("Sorted array:", my_array)
