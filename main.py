def palindrome(arr):
    if type(arr) is not list:
        raise ValueError("Wrong input type! It must be a list")

    if len(arr) < 2:
        raise ValueError("List with elements is too short!")