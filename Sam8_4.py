import re


with open('input.txt', encoding='utf-8') as f:
    banned = [line.strip() for line in f.read().split() if line.strip()]

sentence = input("Введите предложение: ")

def censor(text, banned):
    def repl(match):
        return '*' * len(match.group())

    pattern = '|'.join(map(re.escape, banned))
    return re.sub(pattern, repl, text, flags=re.IGNORECASE)

print(censor(sentence, banned))
