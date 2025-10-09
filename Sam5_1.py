
cheques = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
           1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
           5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
           5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
           3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

total_cheques = len(cheques)
unique_visitors = len(set(cheques))
from collections import Counter
most_visits = Counter(cheques).most_common(1)[0]

print(f"Выдано чеков: {total_cheques}")
print(f"Разных посетителей: {unique_visitors}")
print(f"Чаще всех приходил работник с кодом {most_visits[0]} ({most_visits[1]} раз)")
print()

results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)
best_three = sorted_results[:3]
worst_three = sorted_results[-3:]
from_10_onwards = [r for r in results if r >= 10]
