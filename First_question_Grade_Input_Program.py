def get_grade():
    try:
        user_input = input("Enter your grade (or -999 to finish): ")
        return int(user_input)
    except ValueError:
        print('Invalid input. Please enter a number.')
        return None
list_of_grades = []

while True:
    student_grade = get_grade()

    if student_grade is None:
        continue

    if student_grade == -999:
        if len(list_of_grades) >= 10:
            print('\n--- SUMMARY ---')
            print('THE SUM IS: ', sum(list_of_grades))
            print('YOU HAVE TOTAL OF: ', len(list_of_grades))
            print('THE MAX GRADE IS: ', max(list_of_grades))
            print('THE CLASS AVG IS: ', sum(list_of_grades) / len(list_of_grades))
            break
        else:
            print(f'You need more grades. Currently you have: {len(list_of_grades)}/10')
            continue

    if 0 <= student_grade <= 100:
        list_of_grades.append(student_grade)
    else:
        print('Grade must be between 0 and 100.')