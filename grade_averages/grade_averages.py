if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(n)
    # print(scores)
    # print(len(scores))
    # print(student_marks)

    avg_score = float(0)
    final_grade = float(0)

    for score in scores:
        avg_score = avg_score + score

        avg_grade = avg_score / len(scores)
        # final_grade = str(format(avg_grade, '.2f'))
    print(str(format(avg_grade, '.2f')))


