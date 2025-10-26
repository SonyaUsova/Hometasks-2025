def slice_by_element(t, el):
    if el not in t:
        return ()
    first_idx = t.index(el)
    try:
        second_idx = t.index(el, first_idx + 1)
        return t[first_idx:second_idx + 1]
    except ValueError:
        return t[first_idx:]

print(slice_by_element((1, 2, 3), 8))
print(slice_by_element((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slice_by_element((1, 2, 8, 5, 1, 2, 9), 8))