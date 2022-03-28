# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇
heights_sum = 0
count = 0
for individual_height in student_heights:
    heights_sum += individual_height
    count += 1
average = heights_sum / count

print(f"The average height of this class is: {average}")