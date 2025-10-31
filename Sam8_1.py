from collections import Counter
import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    count = len(words)
    most_common = Counter(words).most_common(1)[0]

print(f'Количество слов: {count}')
print(f'Самое частое слово: {most_common[0]}, встречается {most_common[1]} раз(а)')

