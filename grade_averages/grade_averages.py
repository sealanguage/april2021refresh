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

    avg_score = 0
    final_grade = float(0)

    for score in scores:
        avg_score = avg_score + score
        final_grade = avg_score / len(scores)
        print(final_grade)
