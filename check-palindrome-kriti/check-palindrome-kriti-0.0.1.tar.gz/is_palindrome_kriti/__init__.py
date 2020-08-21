def is_palindrome(string):
    rev=string[::-1]
    if string==rev:
        return True
    else:
        return False