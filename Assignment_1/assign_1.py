
def calculate_result(first_incourse, second_incourse, attendance, final):
    """Calculate the total score based on given marks."""
    return (first_incourse + second_incourse) / 2 + attendance + final

def get_grade(score):
    """Return the letter grade and grade point based on the score."""
    grades = [
        (80, "A+", 4.00), (75, "A", 3.75), (70, "A-", 3.50),
        (65, "B+", 3.25), (60, "B", 3.00), (55, "B-", 2.75),
        (50, "C+", 2.50), (45, "C", 2.25), (40, "D", 2.00),
        (0, "F", 0.00)
    ]
    for threshold, letter, point in grades:
        if score >= threshold:
            return letter, point
    return "Invalid", 0.00  # Fallback case

def is_valid(roll, first_incourse, second_incourse, attendance, final):
    """Validate input values."""
    return (
        int(roll) >= 0 and 
        0 <= first_incourse <= 25 and 0 <= second_incourse <= 25 and 
        0 <= attendance <= 5 and 0 <= final <= 70
    )

# Read and process the file
with open('D:\PythonFiles\Assignment_1\marks.txt') as file:
    lines = file.readlines()

print('Roll  Letter Grade  Grade Point')
print('====  ============  ===========')

for line in lines:
    parts = line.strip().split()  # Using default split to handle spaces flexibly
    roll, first_incourse, second_incourse, attendance, final = map(int, parts)

    if not is_valid(roll, first_incourse, second_incourse, attendance, final):
        print(f"{roll}: Invalid marks detected!")
        continue

    total_score = calculate_result(first_incourse, second_incourse, attendance, final)
    letter_grade, grade_point = get_grade(total_score)

    print(f"{roll:<4}  {letter_grade:<12}  {grade_point:.2f}")