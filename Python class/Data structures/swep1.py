def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. H2"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. Jane Austen", "C. William Shakespeare", "D. Mark Twain"],
            "answer": "C"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
            "answer": "B"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"],
            "answer": "C"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Sapphire"],
            "answer": "C"
        },
        {
            "question": "Which element has the chemical symbol 'Fe'?",
            "options": ["A. Fluorine", "B. Iron", "C. Francium", "D. Gold"],
            "answer": "B"
        },
        {
            "question": "How many continents are there?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
            "answer": "B"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A. Tomato", "B. Avocado", "C. Pepper", "D. Onion"],
            "answer": "B"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["A. 1910", "B. 1912", "C. 1914", "D. 1916"],
            "answer": "B"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Golgi apparatus"],
            "answer": "C"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
            "answer": "C"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["A. Yen", "B. Dollar", "C. Euro", "D. Peso"],
            "answer": "A"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
            "answer": "B"
        },
        {
            "question": "How many bones are there in the adult human body?",
            "options": ["A. 206", "B. 205", "C. 207", "D. 208"],
            "answer": "A"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "C"
        },
        {
            "question": "Which is the largest desert in the world?",
            "options": ["A. Sahara", "B. Arabian", "C. Gobi", "D. Antarctic"],
            "answer": "D"
        },
        {
            "question": "What is the capital of Italy?",
            "options": ["A. Venice", "B. Florence", "C. Rome", "D. Milan"],
            "answer": "C"
        },
    ]

    score = 0

    print("Welcome to the Quiz! Please answer the following questions:\n")

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!\n")
            score += 10
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is: {score} points.")

    # Grade the student
    if score == 200:
        grade = 'A'
    elif score >= 150:
        grade = 'B'
    elif score >= 100:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Your grade: {grade}")

