from collections import Counter

def top_three_digits_count(digits_str):
    count = Counter(int(d) for d in digits_str)
    most_common = count.most_common(3)
    result = {k: v for k, v in sorted(most_common)}
    return result

example_str = "2344448920201"
print(top_three_digits_count(example_str))
