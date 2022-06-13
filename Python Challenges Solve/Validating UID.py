"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a - z, A - Z &  0-9 ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354: 1 is repeating → Invalid
B1CDEF2354: Valid
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    uid = input()
    if len(uid) > 10:
        print('Invalid')
        continue
    string = ''
    upper = 0
    digits = 0
    rep_char = False
    for j in uid:
        if j.isalpha() or j.isdigit():
            if j.isupper():
                upper += 1
            if j.isdigit():
                digits += 1

            if j not in string:
                string += j
            else:
                rep_char = True
                break
    if upper >= 2 and digits >= 3 and not rep_char:
        print('Valid')

    else:
        print('Invalid')

# Using Regex

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
