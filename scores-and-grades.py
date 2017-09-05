import random

def scores_and_grades():
    print "Scores and Grades"
    for i in range(10):
        random_num = random.randint(60,100)
        score = str(random_num)
        grade = ""
        if random_num <= 69:
            grade = "D"
        elif random_num > 69 and random_num <= 79:
            grade = "C"
        elif random_num > 79 and random_num <= 89:
            grade = "B"
        elif random_num > 89 and random_num <= 100:
            grade = "A"
        print "Score: " + score + "; Your grade is " + grade
    print "End of program. Bye!"

scores_and_grades()