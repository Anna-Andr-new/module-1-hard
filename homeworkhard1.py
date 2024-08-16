grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
result = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
student_sort= sorted(students)
dict_1= zip(student_sort,result)
print(dict(dict_1))

# второе решение
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades_m = []
for num in grades:
    s= sum(num)/len(num)
    grades_m.append(s)

grades_m = (dict(zip(students, grades_m)))
grades_sort = (sorted(grades_m.items()))
print(grades_sort)