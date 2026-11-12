class Quiz:
    """개별 퀴즈 항목을 표현하는 클래스"""

    def __init__(self, question: str, choices: list[str], answer: int) -> None:
        if len(choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")
        if not (1 <= answer <= 4):
            raise ValueError("정답 번호는 1에서 4 사이의 정수여야 합니다.")

        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, number: int | None = None) -> None:
        """문제와 4개의 선택지를 콘솔에 출력"""
        if number is not None:
            print(f"\n[문제 {number}]")
        print(self.question)
        print()
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")

    def check_answer(self, user_answer: int) -> bool:
        """사용자 입력 번호와 정답 일치 여부 반환"""
        return user_answer == self.answer

    def to_dict(self) -> dict:
        """JSON 저장을 위한 딕셔너리 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        """딕셔너리 데이터로부터 Quiz 인스턴스 생성"""
        return cls(
            question=str(data["question"]),
            choices=[str(c) for c in data["choices"]],
            answer=int(data["answer"]),
        )
