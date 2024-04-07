
import json
import random


class QuizProcessor():

    # Constants
    QUESTIONS_PER_ATTEMPT = 5

    def __init__(self):
        pass

    def get_quiz_questions(self, course_num, week_num, quiz_num):
        with open(f"./courses/course{course_num}/week{week_num}/quiz{quiz_num}.json", 'r') as fp:
            all_questions = json.loads(fp.read())
        all_q_nums = list(all_questions.keys())
        selected_q = {}
        for _ in range(QuizProcessor.QUESTIONS_PER_ATTEMPT):
            if(len(all_q_nums) == 0):
                break
            next_q_num = random.choice(all_q_nums)
            selected_q[next_q_num] = all_questions[next_q_num]
            all_q_nums.remove(next_q_num)
        return selected_q

    def get_all_quiz_questions(self, course_num, week_num, quiz_num):
        with open(f"./courses/course{course_num}/week{week_num}/quiz{quiz_num}.json", 'r') as fp:
            all_questions = json.loads(fp.read())
        return all_questions


    def evaluate_answers(self, form_content, course, week, quiz_no):
        quiz_data = self.get_all_quiz_questions(course, week, quiz_no)

        # Collected responses from the form
        collected_responses = {}
        for key, value in form_content.items():
            if key.startswith('Q'):
                collected_responses[key] = value

        # Compare collected responses with correct answers and calculate score
        correct_count = 0
        total_questions = len(collected_responses)
        for question_key, response in collected_responses.items():
            if response == quiz_data[question_key][2]:              # Checking if response matches correct answer
                correct_count += 1

        # Calculate score percentage
        score = round((correct_count / total_questions) * 100)

        # Define result based on score
        if score == 100:
            result = "Great! You have got all the questions right."
        elif score >= 50:
            result = "Congratulations! You have completed the Assessment."
        else:
            result = "Sorry! Better Luck next time."

        return score, result


if __name__ == "__main__":
    obj = QuizProcessor()
    print(obj.get_quiz_questions(1, 1))
