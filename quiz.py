class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
            {"question": "What is the largest mammal in the world?", "answer": "Blue whale"},
        ]
        self.score = 0

    def ask_question(self, question_dict):
        print(question_dict["question"])
        user_answer = input("Your answer: ").strip().capitalize()

        if user_answer == question_dict["answer"]:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {question_dict['answer']}\n")

    def run_quiz(self):
        print("Welcome to the Quiz Game!\n")
        
        for question in self.questions:
            self.ask_question(question)

        print(f"Quiz complete! Your final score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
