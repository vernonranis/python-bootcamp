# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# print(type(student_heights))

counter = 0
total_height = 0
for student in student_heights:
  counter += 1
  total_height += student_heights[counter-1]


print(round(total_height/counter))