
data = {}

while True:
    student = input("Student Name: ")
    if student == "done":
        break
    grade = int(input("Grade: "))
    if student in data:
        data[student].append(grade)
    else:
        data[student] = [grade]

for name, gradelist in data.items():
    average_grade = sum(gradelist)/len(gradelist)
    print("Student name: ", name)
    print("Grade: ", average_grade)