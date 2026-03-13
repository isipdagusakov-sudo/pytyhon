students = [
    "Герасимов Никита",
    "Гусэйков Дмитрий", 
    "Афанасьев Михаил",
    "Пузырёв Максим",
    "Владислав Скорбилин",
    "Борисов Иван"
]

subjects = [
    "ОСИС",
    "РПМ",
    "ОАИП", 
    "ИТ"
]
grades = [
    [5, 4, 5, 5],
    [3, 4, 3, 4],
    [5, 5, 5, 5],
    [4, 3, 4, 3],
    [5, 4, 4, 5],
    [2, 3, 2, 3]
]
print("ЖУРНАЛ УСПЕВАЕМОСТИ ГРУППЫ")

print("\nСписок студентов:")
for i in range(len(students)):
    print(f"{i + 1}. {students[i]}")

print("\nСписок предметов:")
for i in range(len(subjects)):
    print(f"{i + 1}. {subjects[i]}")

print("ОЦЕНКИ СТУДЕНТОВ")
for i in range(len(students)):
    print(f"\n{students[i]}:")
    for j in range(len(subjects)):
        print(f"  {subjects[j]}: {grades[i][j]}")

print("СРЕДНИЙ БАЛЛ ПО ПРЕДМЕТАМ")
subject_averages = []
for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total += grades[i][j]
    avg = total / len(students)
    subject_averages.append(avg)
    print(f"{subjects[j]}: {avg:.2f}")

print("СРЕДНИЙ БАЛЛ КАЖДОГО СТУДЕНТА")
student_averages = []
for i in range(len(students)):
    total = 0
    for j in range(len(subjects)):
        total += grades[i][j]
    avg = total / len(subjects)
    student_averages.append(avg)
    print(f"{students[i]}: {avg:.2f}")

print("ЛУЧШИЙ СТУДЕНТ")
best_index = 0
best_avg = student_averages[0]
for i in range(1, len(student_averages)):
    if student_averages[i] > best_avg:
        best_avg = student_averages[i]
        best_index = i

print(f"{students[best_index]} со средним баллом {best_avg:.2f}")

print("ПРЕДМЕТ С НАИМЕНЬШИМ СРЕДНИМ БАЛЛОМ")
worst_index = 0
worst_avg = subject_averages[0]
for i in range(1, len(subject_averages)):
    if subject_averages[i] < worst_avg:
        worst_avg = subject_averages[i]
        worst_index = i

print(f"{subjects[worst_index]} со средним баллом {worst_avg:.2f}")


print("ОБЩИЙ СРЕДНИЙ БАЛЛ ПО ГРУППЕ")
total_sum = 0
total_count = 0
for i in range(len(students)):
    for j in range(len(subjects)):
        total_sum += grades[i][j]
        total_count += 1

overall_average = total_sum / total_count
print(f"Общий средний балл: {overall_average:.2f}")

print("ПЕРЕЧЕНЬ ПРЕДМЕТОВ")
print(f"Количество предметов: {len(subjects)}")
print("Список предметов:")
for subject in subjects:
    print(f"  - {subject}")

print("СТУДЕНТЫ БЕЗ ОЦЕНОК 2")
students_without_twos = []
for i in range(len(students)):
    has_two = False
    for j in range(len(subjects)):
        if grades[i][j] == 2:
            has_two = True
            break
    if not has_two:
        students_without_twos.append(students[i])

if len(students_without_twos) > 0:
    for student in students_without_twos:
        print(f"  - {student}")
else:
    print("Нет таких студентов")

print("СТУДЕНТЫ С ОЦЕНКАМИ НЕ НИЖЕ 4")
students_good = []
for i in range(len(students)):
    all_good = True
    for j in range(len(subjects)):
        if grades[i][j] < 4:
            all_good = False
            break
    if all_good:
        students_good.append(students[i])

if len(students_good) > 0:
    for student in students_good:
        print(f"  - {student}")
else:
    print("Нет таких студентов")