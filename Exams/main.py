# =====================
# main.py: Enter 4 exams and outputs the letter grade - message
# By: Husnain Masood
# Modified: 3/11/2025
# =====================

# 1. Prompt the user for 4 exams
exam_one = int(input("Please enter Exam 1 score: "))
exam_two = int(input("Please enter Exam 2 score: "))
exam_three = int(input("Please enter Exam 3 score: "))
exam_four = int(input("Please enter Exam 4 score: "))

# 2. Convert the exams into a float
exam_one = float(exam_one)
exam_two = float(exam_two)
exam_three = float(exam_three)
exam_four = float(exam_four)

# 3. Round the exams to one decimal place
exam_one = round(exam_one, 1)
exam_two = round(exam_two, 1)
exam_three = round(exam_three, 1)
exam_four = round(exam_four, 1)

# 4. Create a list for exams and output the highest and lowest scores 
all_exams = [exam_one, exam_two, exam_three, exam_four]
high_score = max(all_exams)
low_score = min(all_exams)
print(f"\nHighest score: {high_score:.2f}")
print(f"Lowest score: {low_score:.2f}")

# 5. Sort the exams
all_exams.sort()
print("Exams Entered:", all_exams)

# 6. Calculate the average score based on the highest scores using lists
all_exams.remove(low_score)
average_score = sum(all_exams) / len(all_exams)
print(f"Average Score (lowest exam dropped): {average_score:.2f}")

# 7. Use an if statement to output the grade and a message following the grade
if (sum(all_exams) / len(all_exams)) >= 90:
    print("Grade: A - Good Job!")
elif (sum(all_exams) / len(all_exams)) >= 80:
    print("Grade: B - That's Great!")
elif (sum(all_exams) / len(all_exams)) >= 70:
    print("Grade: C - OK")
elif (sum(all_exams) / len(all_exams)) >= 60:
    print("Grade: D - Sorry")
else:
    print("Grade: F - Try harder")
    


