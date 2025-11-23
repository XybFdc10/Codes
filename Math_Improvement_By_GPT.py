import random

def Is_math():
    nums = [5, 6, 7, 8, 9]
    used_question = set()

    # Generate 5 unique questions
    while len(used_question) < 5:
        pair = tuple(sorted((random.choice(nums), random.choice(nums))))
        used_question.add(pair)

    # Convert to list of lists
    questions = [list(q) for q in used_question]

    print("-----------------")
    print("| MATH QUESTION |")
    print("-----------------")

    score = 0

    # Loop setiap soal otomatis
    for a, b in questions:
        print(f"What Is The Result Of {a} × {b}?")
        user_ans = int(input("Answer: "))
        if user_ans == a * b:
            score += 1

    print("----------------")
    print("| YOUR ANSWER  |")
    print("----------------")
    print(f"Your Right Answer is {score}/5")

Is_math()
