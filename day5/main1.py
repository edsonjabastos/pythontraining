# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    print(student_scores[n])
    print(student_scores[n - 1])
    student_scores[n] = int(student_scores[n])

# print(student_scores)
# print(max(student_scores))
# print(min(student_scores))
# 78 65 89 86 55 91 64 89 <-inputs

# 🚨 Don't change the code above 👆
#Write your code below this row 👇
current = 0
for n in range(0, len(student_scores)):
    if student_scores[n] < student_scores[n - 1]:
        current = student_scores[n - 1]
print(f"The highest scores is: {current}")

# teacher solution

# for score in student_scores:
#     if score > current:
#         current = score