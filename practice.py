
names_list = input("names of the students:").split()
marks_list = list(map(int, input("marks of students:").split()))
updated_marks = list(map(int, input("updated marks of students:").split()))
up_set = []
for i in range(len(names_list)):
    up_set.append(marks_list[i] + updated_marks[i])
#creting list with current marks
n = len(names_list)
current_marks_list = [[0 for j in range(2)] for i in range(n)]
for m in range(n):
    current_marks_list[m][0] = names_list[m]
    current_marks_list[m][1] = marks_list[m]
#sorting out the current_marks_list
l = len(current_marks_list)
for i in range(0, l):
        for j in range(0, l-i-1):
            if (current_marks_list[j][1] < current_marks_list[j + 1][1]):
                tempo = current_marks_list[j]
                current_marks_list[j]= current_marks_list[j + 1]
                current_marks_list[j + 1]= tempo
for i in range(len(current_marks_list)):
    current_marks_list[i] += [i+1]


neww = []
for i in range(len(current_marks_list)):
    neww.append(current_marks_list[i][0])
print("current_marks_list with ranks(before updating marks):")
print(current_marks_list)


#creating list with updated marks
updated_marks_list = [[0 for j in range(2)] for i in range(n)]
for i in range(n):
    updated_marks_list[i][0] = names_list[i]
    updated_marks_list[i][1] = marks_list[i] + updated_marks[i]
#sorting updated_marks_list to find updated_rank
ls = len(updated_marks_list)
for i in range(0, ls):
        for j in range(0, ls-i-1):
            if (updated_marks_list[j][1] < updated_marks_list[j + 1][1]):
                tempo = updated_marks_list[j]
                updated_marks_list[j]= updated_marks_list[j + 1]
                updated_marks_list[j + 1]= tempo
for i in range(len(updated_marks_list)):
    updated_marks_list[i] += [i+1]
print("updated_marks_list with ranks(aftrer updating marks):")
print(updated_marks_list)

hgh = []
highest = updated_marks_list[0]
for z in range(1,len(updated_marks_list)):
    if updated_marks_list[z][1] > highest[1]:
        highest = updated_marks_list[z]

print("Student with highest marks:" + highest[0])
rk = neww.index(highest[0])
print("Jump from previous rank to current rank:" + str(rk))