def find_bigger(*args):
    """
    Returns the largest number of the given numbers.
    Input parameters: *args
    Output parameters: args
    """
    max = args[0]
    for i in range(len(args)):
        if args[i] > max:
            max = args[i]
    return max

print(find_bigger.__doc__)
print("max number = ", find_bigger(2, 8.4, 0, -67, 17))
