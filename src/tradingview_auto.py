import pyautogui
import time

def open_tradingview():
    pyautogui.press('win')  # press windows button
    time.sleep(1)
    pyautogui.write('TradingView')  # typing "TradingView"
    time.sleep(1)
    pyautogui.press('enter')  # press enter
    time.sleep(10)  # wait 10s for makesure the app was done loading

def take_chart_snapshot():
    pyautogui.hotkey('ctrl', 'alt', 's')
    time.sleep(2)

def switch_to_next_chart():
    pyautogui.press('space')
    time.sleep(3)

def main():
    open_tradingview()

    for i in range(15):
        take_chart_snapshot()
        print(f"Snapshot {i+1} taken.")
        switch_to_next_chart()
        print(f"Switched to next chart {i+1}.")

if __name__ == '__main__':
    main()
