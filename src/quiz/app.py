"""
Interactive Constitution Quiz Application
Интерактивное приложение для проверки знаний о Конституции
"""

import random
import time
from questions import QUIZ_QUESTIONS, DIFFICULTY_LEVELS


class ConstitutionQuiz:
    """Main quiz application class"""

    def __init__(self):
        self.score = 0
        self.answered_questions = 0
        self.start_time = None
        self.end_time = None
        self.results = []

    def display_header(self):
        """Display application header"""
        print("\n" + "=" * 70)
        print(" " * 15 + "ИНТЕРАКТИВНАЯ ВИКТОРИНА")
        print(" " * 10 + "Проверка знаний о Конституции РФ")
        print("=" * 70 + "\n")

    def display_menu(self):
        """Display main menu"""
        print("\n📚 ГЛАВНОЕ МЕНЮ")
        print("-" * 50)
        print("1️⃣  Начать викторину (все вопросы)")
        print("2️⃣  Викторина по уровню сложности")
        print("3️⃣  Случайные вопросы (N вопросов)")
        print("4️⃣  Справка о Конституции")
        print("5️⃣  Выход")
        print("-" * 50)

    def get_choice(self, prompt, valid_options):
        """Get and validate user choice"""
        while True:
            try:
                choice = input(f"\n{prompt}: ").strip()
                if choice in valid_options:
                    return choice
                print(f"❌ Пожалуйста, выберите один из вариантов: {', '.join(valid_options)}")
            except KeyboardInterrupt:
                print("\n\nВикторина прервана пользователем.")
                exit(0)

    def ask_question(self, question):
        """Ask a single question and get answer"""
        print(f"\n📝 Вопрос {self.answered_questions + 1}: {question['question']}")
        print("-" * 50)

        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

        print()
        while True:
            choice = input("Ваш ответ (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return int(choice) - 1
            print("❌ Пожалуйста, введите цифру от 1 до 4")

    def show_question_result(self, question, user_answer):
        """Display result for a single question"""
        correct = user_answer == question['correct_answer']

        if correct:
            print("✅ Правильно!")
            self.score += 1
        else:
            print(f"❌ Неправильно! Правильный ответ: {question['options'][question['correct_answer']]}")

        print(f"\n💡 Объяснение: {question['explanation']}")

        self.results.append({
            'question_id': question['id'],
            'user_answer': user_answer,
            'correct_answer': question['correct_answer'],
            'is_correct': correct
        })

        input("\nНажмите Enter для продолжения...")

    def run_quiz(self, questions_to_ask):
        """Run the quiz with given questions"""
        self.score = 0
        self.answered_questions = 0
        self.results = []
        self.start_time = time.time()

        print("\n" + "=" * 70)
        print(f"🎯 Начинается викторина! Всего вопросов: {len(questions_to_ask)}")
        print("=" * 70)

        for question in questions_to_ask:
            self.answered_questions += 1
            user_answer = self.ask_question(question)
            self.show_question_result(question, user_answer)
            print("\n" + "-" * 70)

        self.end_time = time.time()
        self.show_results()

    def show_results(self):
        """Display quiz results"""
        elapsed_time = int(self.end_time - self.start_time)
        percentage = (self.score / self.answered_questions * 100) if self.answered_questions > 0 else 0

        print("\n" + "=" * 70)
        print(" " * 20 + "📊 РЕЗУЛЬТАТЫ ВИКТОРИНЫ")
        print("=" * 70)
        print(f"✅ Правильных ответов: {self.score}/{self.answered_questions}")
        print(f"📈 Процент правильных ответов: {percentage:.1f}%")
        print(f"⏱️  Время прохождения: {elapsed_time} сек")

        # Show assessment
        if percentage >= 90:
            print("🌟 ОТЛИЧНО! Вы отлично знаете Конституцию!")
        elif percentage >= 75:
            print("👍 ХОРОШО! Ваши знания на хорошем уровне.")
        elif percentage >= 60:
            print("📚 УДОВЛЕТВОРИТЕЛЬНО. Рекомендуем повторить материал.")
        else:
            print("❌ НЕУДОВЛЕТВОРИТЕЛЬНО. Советуем внимательнее изучить Конституцию.")

        print("=" * 70)

        # Show detailed results
        self.show_detailed_results()

    def show_detailed_results(self):
        """Show detailed results for each question"""
        print("\n📋 ПОДРОБНЫЕ РЕЗУЛЬТАТЫ:")
        print("-" * 70)

        for result in self.results:
            question = next(q for q in QUIZ_QUESTIONS if q['id'] == result['question_id'])
            status = "✅" if result['is_correct'] else "❌"
            print(f"\n{status} Вопрос {result['question_id']}: {question['question']}")
            print(f"   Ваш ответ: {question['options'][result['user_answer']]}")
            if not result['is_correct']:
                print(f"   Правильный ответ: {question['options'][result['correct_answer']]}")

    def select_difficulty(self):
        """Let user select difficulty level"""
        print("\n🎯 ВЫБЕРИТЕ УРОВЕНЬ СЛОЖНОСТИ:")
        print("-" * 50)
        print("1. 🟢 Легкий (3 вопроса)")
        print("2. 🟡 Средний (4 вопроса)")
        print("3. 🔴 Сложный (5 вопросов)")
        print("-" * 50)

        choice = self.get_choice("Выберите уровень (1-3)", ['1', '2', '3'])

        level_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
        difficulty = level_map[choice]

        question_ids = DIFFICULTY_LEVELS[difficulty]
        questions_to_ask = [q for q in QUIZ_QUESTIONS if q['id'] in question_ids]
        random.shuffle(questions_to_ask)

        return questions_to_ask

    def random_questions(self):
        """Get random number of questions"""
        print("\n🎲 СЛУЧАЙНЫЕ ВОПРОСЫ")
        print("-" * 50)

        while True:
            try:
                count = int(input(f"Сколько вопросов? (1-{len(QUIZ_QUESTIONS)}): ").strip())
                if 1 <= count <= len(QUIZ_QUESTIONS):
                    break
                print(f"❌ Пожалуйста, введите число от 1 до {len(QUIZ_QUESTIONS)}")
            except ValueError:
                print("❌ Пожалуйста, введите корректное число")

        questions_to_ask = random.sample(QUIZ_QUESTIONS, count)
        return questions_to_ask

    def show_info(self):
        """Display information about the Constitution"""
        print("\n" + "=" * 70)
        print(" " * 15 + "📖 СПРАВКА О КОНСТИТУЦИИ РФ")
        print("=" * 70)
        print("""
Конституция Российской Федерации:

🔹 ДАТА ПРИНЯТИЯ: 12 декабря 1993 года
🔹 ФОРМА ПРИНЯТИЯ: Путём всенародного голосования (референдума)
🔹 КОЛИЧЕСТВО ГЛАВ: 8
🔹 КОЛИЧЕСТВО СТАТЕЙ: 137 (с учётом поправок)

СТРУКТУРА КОНСТИТУЦИИ:
1. Преамбула - декларирует принципы и цели государства
2. Глава 1 - Основы конституционного строя (1-16)
3. Глава 2 - Права и свободы человека и гражданина (17-64)
4. Глава 3 - Федеративное устройство (65-79)
5. Глава 4 - Президент Российской Федерации (80-91)
6. Глава 5 - Федеральное Собрание (92-140)
7. Глава 6 - Правительство Российской Федерации (130-135)
8. Глава 7 - Судебная власть (118-129)
9. Глава 8 - Местное самоуправление (130-133)
10. Глава 9 - Конституционные поправки и пересмотр Конституции (134-137)

ОСНОВНЫЕ ПРИНЦИПЫ:
✓ Демократия
✓ Федерализм
✓ Правовое государство
✓ Республиканская форма правления
✓ Разделение власти (законодательная, исполнительная, судебная)
✓ Защита прав и свобод человека
        """)
        print("=" * 70)
        input("\nНажмите Enter для возврата в меню...")

    def main(self):
        """Main application loop"""
        self.display_header()

        while True:
            self.display_menu()
            choice = self.get_choice("Выберите пункт меню (1-5)", ['1', '2', '3', '4', '5'])

            if choice == '1':
                # All questions
                questions_to_ask = QUIZ_QUESTIONS.copy()
                random.shuffle(questions_to_ask)
                self.run_quiz(questions_to_ask)

            elif choice == '2':
                # By difficulty
                questions_to_ask = self.select_difficulty()
                self.run_quiz(questions_to_ask)

            elif choice == '3':
                # Random questions
                questions_to_ask = self.random_questions()
                self.run_quiz(questions_to_ask)

            elif choice == '4':
                # Show info
                self.show_info()

            elif choice == '5':
                # Exit
                print("\n👋 Спасибо за прохождение викторины! До свидания!")
                break


def main():
    """Entry point"""
    quiz = ConstitutionQuiz()
    try:
        quiz.main()
    except KeyboardInterrupt:
        print("\n\n👋 Викторина прервана пользователем.")


if __name__ == "__main__":
    main()
