# HERE ARE THREE BRAIN TWISTERS TO TRY WHILE I AM HOME WITH MY SON WHO IS SICK TODAY...
# PLEASE COMPLETE AT LEAST ONE OF THEM DURING CLASS. (10pts)
# WE WILL GET BACK TO KIVY WHEN WE NEXT MEET (NEXT WEEK)
# EACH PROBLEM IS SOLVABLE BY COMBINING TECHNIQUES FROM CLASS; THEY VARY SLIGHTLY IN DIFFICULTY.

'''
PROBLEM 1
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either 1) become a palindrome in less than fifty iterations,
or, 2) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
'''

lychrel_list = []
for i in range(10000):
    palindrome = False
    counter = 1
    placeholder = i
    while counter < 50 and not palindrome:
        counter += 1
        other_number = int(str(placeholder)[::-1])
        if other_number == placeholder and not other_number == i:
            palindrome = True
        placeholder += other_number
    if not palindrome:
        lychrel_list.append(i)

print(len(lychrel_list))


'''
PROBLEM 2 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How is the largest circular prime below one million?
'''

# I couldn't think of a way to do this faster
'''starting_number = 99999997
done = False
while not done:
    placeholder = str(starting_number)
    prime = True
    complete_rotation = False
    counter = len(placeholder)
    print(starting_number)
    while prime and not complete_rotation:
        # print(placeholder)
        dummy = placeholder[0]
        placeholder = int(str(placeholder[1:len(placeholder) + 1]) + str(dummy))
        while prime:
            i = 3
            if not placeholder % i == 0:
                i += 2
            else:
                prime = False
            if i > ((starting_number**(1/2)) + 1):
                prime = True
        if counter == 0:
            complete_rotation = True
            done = True
            print(starting_number)
    starting_number -= 2'''


'''
PROBLEM 3
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.  What is it?
'''
a = 0
a_thousand_exactly = False
while not a_thousand_exactly:
    a += 1
    b = a + 1
    pythag_triple = False
    while not pythag_triple:
        b += 1
        try:
            c = ((a**2 + b**2)**(1/2))
            if c % 1 == 0:
                pythag_triple = True
                print("hi")
        except:
            pass
    if a + b + c == 1000:
        print("a =", a, "b =", b, "c =", c)
        a_thousand_exactly = True
    elif a > 500:
        a_thousand_exactly = True
        print("failed")
