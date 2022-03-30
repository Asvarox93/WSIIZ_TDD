def palindrome(arr):
    if type(arr) is not list:
        raise ValueError("Wrong input type! It must be a list")

    if len(arr) < 2:
        raise ValueError("List with elements is too short!")

    counter = 0
    palindrome_list = []
    for a in arr:
        if type(a) is not str or a.isnumeric():
            raise ValueError("Elements in list are not type of string or is numeric")

        el = a.lower().replace(" ", "").replace(",", "").replace(".", "")

        reversed_arr = []
        index = len(el)
        while index > 0:
            reversed_arr += el[index - 1]
            index = index - 1

        reversed_el = ""
        reversed_el = reversed_el.join(reversed_arr)

        if el == reversed_el:
            counter += 1
            palindrome_list.append(a)

    result = {counter:palindrome_list}
    return result

