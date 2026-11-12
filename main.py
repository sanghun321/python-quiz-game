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


def main() -> None:
    try:
        while True:
            print_menu()
            choice = get_valid_int("선택: ", 1, 5)

            if choice == 1:
                print("📝 [준비 중] 퀴즈 풀기 기능")
            elif choice == 2:
                print("📌 [준비 중] 퀴즈 추가 기능")
            elif choice == 3:
                print("📋 [준비 중] 퀴즈 목록 기능")
            elif choice == 4:
                print("🏆 [준비 중] 점수 확인 기능")
            elif choice == 5:
                print("👋 퀴즈 게임을 종료합니다. 감사합니다!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 종료 신호가 감지되어 안전하게 프로그램을 종료합니다.")


if __name__ == "__main__":
    main()
