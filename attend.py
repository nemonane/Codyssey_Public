import os

FILENAME = "attendance.txt"

def show_menu():
    print("\n--- 스터디 출석부 ---")
    print("1. 출석 체크 (날짜와 이름 입력)")
    print("2. 출석 명단 보기")
    print("3. 종료")
    return input("메뉴를 선택하세요: ")

def add_attendance():
    date = input("날짜를 입력하세요 (예: 2023-10-27): ")
    name = input("이름을 입력하세요: ")

    # 'a' 모드는 append(추가)입니다. 파일이 없으면 새로 만듭니다.
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"{date}, {name}\n")
    print(f"✅ {name}님의 출석이 기록되었습니다.")

def view_attendance():
    print("\n--- 현재 출석 명단 ---")
    if not os.path.exists(FILENAME):
        print("기록된 출석 명단이 없습니다.")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if not lines:
            print("기록된 출석 명단이 없습니다.")
        for line in lines:
            print(line.strip())

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            add_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
