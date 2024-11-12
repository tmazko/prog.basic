from random import randint, choice
import os


No = 1
languages = ["Python", "C++", "C#", "Java"]
used_grades=[]
with open("data.csv", "w") as datafile:
    datafile.write("No, Student, Age, Grade, Sex, Prog. Language\n")
    while No < 201:
        string = f"{No}, student{No}, "
        age = randint(13, 16)
        if age == 13:
            grade = randint(8, 9)
        elif age == 14:
            grade = randint(9, 10)
        elif age == 15:
            grade = randint(10, 11)
        else:
            grade = 11
        if grade not in used_grades:
            used_grades.append(grade)
        sex = choice(["m", "fm"])
        language = choice(languages)
        string += f"{age}, {grade}, {sex}, {language}\n"
        datafile.write(string)
        No += 1


#!!!! в мене по іншому зберігає файл з даними тому я змінила параметри в split()

used_grades.sort()
groups={int(i):{j:[] for j in languages} for i in used_grades}

students=[]

with open(os.getcwd()+"\data.csv","r") as file:
    next(file)
    for row in file:
        students.append([int(i) if i.isdigit() else i for i in row[:-1].split(", ")])


for grade in used_grades:
    for language in languages:
        for i in range(len(students)):
            if students[i][3]==grade and students[i][5]==language:
                groups[grade][language].append(students[i])


print("\nGROUPS:")
for grade, languages in groups.items():
    print(f"\nGrade {grade}:")
    for language, students_list in languages.items():
        print(f"  {language}:")
        for student in students_list:
            print(f"    {student}")