if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [student[1] for student in students]

    lowest = min(scores)
    second_lowest = min(score for score in scores if score != lowest)

    names = [student[0] for student in students if student[1] == second_lowest]
    names.sort()

    for name in names:
        print(name)
