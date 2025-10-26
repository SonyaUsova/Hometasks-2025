with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    letters = [c for c in text if c.isalpha() and c.isascii()]
    words = text.split()
    lines = text.splitlines()
    print(f"{len(letters)} letters")
    print(f"{len(words)} words")
    print(f"{len(lines)} lines")

