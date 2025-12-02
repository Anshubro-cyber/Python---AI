import requests

url = "https://opentdb.com/api.php?amount=5&type=multiple"

requests = requests.get(url)
if requests.status_code == 200:
    trivia_data = requests.json()
    score = 0

    for i, question_data in enumerate(trivia_data['results']):
        print(f"Q{i+1}: {question_data['question']}")
        options = question_data['incorrect_answers'] + [question_data['correct_answer']]
        options = sorted(options)  
        for j, option in enumerate(options):
            print(f" {j + 1}. {option}")

        user_answer = input("Your answer (1-4): ")
        if options[int(user_answer) - 1] == question_data['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data['correct_answer']}\n")

    print(f"Your final score is: {score} out of {len(trivia_data['results'])}")
else:
    print("Failed to retrieve trivia questions.")
        