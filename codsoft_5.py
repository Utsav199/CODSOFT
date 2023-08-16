import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Madrid", "Berlin", "London"],
                "correct_answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "Which famous scientist developed the theory of relativity?",
                "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Nikola Tesla"],
                "correct_answer": "Albert Einstein"
            },
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "correct_answer": "Tokyo"
            },
            {
                "question": "Who wrote the play 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
                "correct_answer": "William Shakespeare"
            }
        ]
        
        self.current_question_index = 0
        self.score = 0
        
        self.label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 14), command=self.start_quiz)
        self.start_button.pack(pady=10)
        
        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.feedback_label.pack(pady=10)
        
    def start_quiz(self):
        self.label.config(text="Question:")
        self.start_button.config(state=tk.DISABLED)
        self.feedback_label.config(text="")
        self.display_question()
        
    def display_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label = tk.Label(root, text=question_data["question"], font=("Helvetica", 14), wraplength=300)
        self.question_label.pack(pady=10)
        
        self.user_answer = tk.StringVar()
        
        for option in question_data["options"]:
            tk.Radiobutton(root, text=option, variable=self.user_answer, value=option, font=("Helvetica", 12)).pack(anchor=tk.W)
        
        self.submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=self.check_answer)
        self.submit_button.pack(pady=10)
        
    def check_answer(self):
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["correct_answer"]
        user_choice = self.user_answer.get()
        
        if user_choice == correct_answer:
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect. The correct answer is {correct_answer}."
        
        self.feedback_label.config(text=feedback)
        
        self.current_question_index += 1
        self.clear_question_ui()
        
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.show_final_results()
        
    def clear_question_ui(self):
        self.question_label.pack_forget()
        self.submit_button.pack_forget()
        for widget in root.winfo_children():
            widget.pack_forget()
        
    def show_final_results(self):
        result_text = f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}"
        if self.score == len(self.questions):
            result_text += "\nCongratulations! You got all questions correct."
        
        self.result_label = tk.Label(root, text=result_text, font=("Helvetica", 14))
        self.result_label.pack(pady=10)
        
        self.play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 14), command=self.restart_game)
        self.play_again_button.pack(pady=10)
        
    def restart_game(self):
        self.current_question_index = 0
        self.score = 0
        self.result_label.pack_forget()
        self.play_again_button.pack_forget()
        self.feedback_label.config(text="")
        self.start_quiz()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("390x640")  # Set the window size suitable for mobile display
    game = QuizGame(root)
    root.mainloop()
