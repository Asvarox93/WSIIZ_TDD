def palindrome(arr):
    if type(arr) is not list:
        raise ValueError("Wrong input type! It must be a list")

    if len(arr) < 2:
        raise ValueError("List with elements is too short!")

    for a in arr:
        if type(a) is not str or a.isnumeric():
            raise ValueError("Elements in list are not type of string or is numeric")

