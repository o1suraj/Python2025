marks = []
while True:
    sub_mark = input("Enter the marks of each subject")
    if sub_mark == "":
        break

    else :
        marks.append(float(sub_mark))

average = sum(marks) / len(marks)
print(average)