from quiz import Quiz, get_default_quizzes


def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    """공백 제거, 빈 입력, 숫자 변환, 범위 검증을 수행하는 공통 입력 함수"""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
            continue
        try:
            value = int(raw)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
            continue

        if not (min_val <= value <= max_val):
            print(f"⚠️ 잘못된 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
            continue

        return value


def get_non_empty_str(prompt: str) -> str:
    """앞뒤 공백을 제거하고 빈 문자열 입력을 방지하는 공통 문자열 입력 함수"""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("⚠️ 입력이 비어 있습니다. 내용을 입력하세요.")
            continue
        return raw


def print_menu() -> None:
    print("\n========================================")
    print("        🎯 나만의 상식 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")


def play_quiz(quizzes: list[Quiz], best_score: int | None) -> int | None:
    """저장된 퀴즈를 출제하고 채점 및 최고 점수 갱신 결과 반환"""
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return best_score

    total = len(quizzes)
    correct_count = 0
    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

    for idx, quiz in enumerate(quizzes, start=1):
        print("\n----------------------------------------")
        quiz.display(idx)
        user_answer = get_valid_int("\n정답 입력: ", 1, 4)

        if quiz.check_answer(user_answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            correct_text = quiz.choices[quiz.answer - 1]
            print(f"❌ 오답입니다! 정답은 {quiz.answer}번 ({correct_text})입니다.")

    score = round((correct_count / total) * 100)
    print("\n========================================")
    print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

    if best_score is None or score > best_score:
        best_score = score
        print("🎉 새로운 최고 점수입니다!")

    print("========================================")
    return best_score


def add_quiz(quizzes: list[Quiz]) -> None:
    """사용자로부터 문제, 선택지 4개, 정답을 입력받아 새 퀴즈 등록"""
    print("\n📌 새로운 퀴즈를 추가합니다.\n")
    question = get_non_empty_str("문제를 입력하세요: ")
    choices = [
        get_non_empty_str(f"선택지 {i}: ")
        for i in range(1, 5)
    ]
    answer = get_valid_int("정답 번호 (1-4): ", 1, 4)

    quizzes.append(Quiz(question=question, choices=choices, answer=answer))
    print("\n✅ 퀴즈가 추가되었습니다!")


def show_quiz_list(quizzes: list[Quiz]) -> None:
    """등록된 모든 퀴즈 목록 출력"""
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다.")
        return

    print(f"\n📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("----------------------------------------")
    for idx, quiz in enumerate(quizzes, start=1):
        print(f"[{idx}] {quiz.question}")
    print("----------------------------------------")


def show_best_score(best_score: int | None) -> None:
    """현재까지 기록된 최고 점수 출력"""
    if best_score is None:
        print("\n⚠️ 아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어보세요!")
        return

    print(f"\n🏆 최고 점수: {best_score}점")


def main() -> None:
    quizzes = get_default_quizzes()
    best_score: int | None = None
    print(f"📚 기본 상식 퀴즈 {len(quizzes)}문제가 준비되었습니다.")

    try:
        while True:
            print_menu()
            choice = get_valid_int("선택: ", 1, 5)

            if choice == 1:
                best_score = play_quiz(quizzes, best_score)
            elif choice == 2:
                add_quiz(quizzes)
            elif choice == 3:
                show_quiz_list(quizzes)
            elif choice == 4:
                show_best_score(best_score)
            elif choice == 5:
                print("👋 퀴즈 게임을 종료합니다. 감사합니다!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 종료 신호가 감지되어 안전하게 프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
