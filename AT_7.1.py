def count_positives_sum_negatives(arr):
    pos, neg = 0, 0
    if arr != []:
        for el in arr:
            if el > 0:
                pos += 1
            else:
                neg += el
        return [pos, neg]
    return arr