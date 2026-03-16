# ---------------------------------------------
# Topic : Function
# ---------------------------------------------


# defining a palindrome function
def palindrome(st):
    # variable for stroring reversed string
    rev = ""

    for i in range(len(st) - 1, -1, -1):
        rev = rev + st[i]

    if rev == st:
        print(f"{st} is a palindrome")
    else:
        print(f"{st} is not a palindrome")


palindrome("naman")
palindrome("sneha")

""" OUTPUT:
naman is a palindrome
sneha is not a palindrome
"""
