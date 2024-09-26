for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count from 0 to 100 in steps of 10
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# count down from 20 to 0 in steps of -1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# count number of stars of user iput
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# print out n to number of stars
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
