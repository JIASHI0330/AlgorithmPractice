"""
Questions to ask during the interview to clarify the constraints
1. What happens when two #'s appear beside each other
2. What happens to # when there is no character to remove
3. Are two empty string equal to each other
4. Does case sensitivity matter
"""


# Brute force solution
def backspaceCompare(s, t):
    new_s = []
    new_t = []
    for i in range(len(s)):
        if s[i] == "#":
            if len(new_s) != 0:
                new_s.pop()
        else:
            new_s.append(s[i])

    for j in range(len(t)):
        if t[j] == "#":
            if len(new_t) != 0:
                new_t.pop()
        else:
            new_t.append(t[j])

    if len(new_s) != len(new_t):
        return False

    if new_s == new_t:
        return True
    else:
        return False

# def backspaceCompare(s, t):
#     sPointer = len(s) - 1
#     tPointer = len(t) - 1
#     while (sPointer >= 0) or (tPointer >= 0):
#         if s[sPointer] == "#" or t[tPointer] == "#":
#             if s[sPointer] == "#":
#                 jumpCount = 2
#                 while jumpCount > 0:
#                     sPointer -= 1
#                     jumpCount -= 1
#                     if s[sPointer] == "#":
#                         jumpCount = jumpCount + 2



s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))
