"""
Consider the following:

A string, s, of length n where .
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.
Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string .
Given s and k, print n/k lines where each line i denotes string ui.

Example

s = "AAABCADDE"
K = 3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so u1 = 'A'. The second substring has all distinct characters, so u2 = "BCA". The third substring has 2 different characters, so u3 = "DE". Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format

The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

Sample Input

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD
"""


def merge_the_tools(string, k):
    l = []
    n = 0
    n2 = k
    if k == 1:
        l = [[x] for x in string]
    else:
        for i in range(k):
            l.append(string[n:n2])
            n += k
            n2 += k

    l2 = []
    for i in range(len(l)):
        s = ''
        for j in range(len(l[i])):
            if l[i][j] not in s:
                s += l[i][j]
        l2.append(s)
    print('\n'.join(l2))
