import random

# PROBLEM 1 (Fibonacci)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

done = False
a = int(1)

b = int(1)


while not done:
    print(a, end=" ")
    print(b, end=" ")
    a += int(b)
    b += int(a)
    if a > 1000 or b > 1000:
        done = True

print()
print()
# PROBLEM 2 (Dice Sequence)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

counter = 0
for i in range(1, 1000001):
    a = random.randrange(1, 6)
    b = random.randrange(1, 6)
    c = random.randrange(1, 6)
    d = random.randrange(1, 6)
    e = random.randrange(1, 6)
    if a <= b <= c <= d <= e:
        counter += 1
print("The probability of that thing mentioned happening is ", counter, " in ", i, " or ", round(counter/i, 3), "%.")

print()
# PROBLEM 3 (Number Puzzler)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in range(1, 10):
                number_1 = str(i) + str(j) + str(k) + str(l)
                number_2 = str(l) + str(k) + str(j) + str(i)
                if (int(number_2)/int(number_1)) == 4:
                    print(number_1)
