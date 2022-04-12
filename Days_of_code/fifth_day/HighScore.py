# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


# engenharia reversa (max())
max_value = None
for score in student_scores:
  if max_value is None or score > max_value:
    max_value = score


print(f"The highest score in the class is: {max_value}")