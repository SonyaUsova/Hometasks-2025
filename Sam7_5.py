def top_three_unique(numbers):
    uniq = set(numbers)
    top_three = sorted(uniq, reverse=True)[:3]
    return tuple(top_three)


print(top_three_unique([1, 3, 5, 7, 5, 3, 1]))
print(top_three_unique([10, 9, 8, 7, 6]))
print(top_three_unique([1, 1, 1, 1]))
