import time
import pyautogui

# 사용자가 한 번 터치한 좌표를 저장할 변수
touched_position = None

def get_touch_position():
    global touched_position
    if touched_position is None:
        print("터치한 위치가 아직 설정되지 않았습니다.")
        return None
    else:
        return touched_position

def set_touch_position():
    global touched_position
    print("화면에서 한 번 터치하세요.")
    time.sleep(2)  # 사용자가 클릭할 시간을 주기 위해 2초 대기
    touched_position = pyautogui.position()
    print(f"터치 위치가 설정되었습니다. (x={touched_position[0]}, y={touched_position[1]})")

def simulate_touch():
    position = get_touch_position()
    if position is not None:
        pyautogui.click(position[0], position[1])
        print(f"터치: x={position[0]}, y={position[1]}")

while True:
    action = input("터치 위치 설정 (s), 터치 수행 (t), 종료 (q): ").lower()

    if action == 's':
        set_touch_position()
    elif action == 't':
        simulate_touch()
        set_touch_position()
        while True:
            simulate_touch()
    elif action == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 명령을 입력하세요.")
