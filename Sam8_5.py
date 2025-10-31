name = input("Имя игрока: ")
score = int(input("Очки: "))

with open('scores.txt', 'a', encoding='utf-8') as f:
    f.write(f"{name},{score}\n")

with open('scores.txt', 'r', encoding='utf-8') as f:
    scores = [line.strip().split(',') for line in f]
    scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)

print("Топ 3 результата:")
for i, row in enumerate(scores[:3], 1):
    print(f"{i}. {row[0]} - {row[1]}")
