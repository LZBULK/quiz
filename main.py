
questions = {"Сколько планет в Солнечной системе?":"8",
             "Столица Франции":"Париж"}

ochki = 0

for q, a in questions.items():
    user_answer = input(q + " ")
    if user_answer.lower() == a.lower():
        print("Привильно!")
        ochki +=1
    else:
        print("Неправильно!")

print(f"Ваш результат: {ochki} из {len(questions)}")



