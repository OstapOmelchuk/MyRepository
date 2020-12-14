div_by_two, div_by_three, Div_by_two_three = [], [], []

for i in range(1, 11):
    if i%2 == 0:
        div_by_two.append(i)
    if i%3 == 0:
        div_by_three.append(i)
    if i%3 != 0 and i%2 != 0:
        Div_by_two_three.append(i)

print(f"even numbers that are divisible by 2: {div_by_two}")
print(f"odd numbers, which are divisible by 3: {div_by_three}")
print(f"numbers that are not divisible by 2 and 3: {Div_by_two_three}")