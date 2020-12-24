def list_animals(animals):
    st = ''
    for i in range(len(animals)):
        st += f"{i + 1}. {animals[i]}\n"
    return st