import pyautogui
import time
import winsound
import os
import shutil

def clear_directory(directory_path):
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
        print(f"Directory {directory_path} is now clean.")
    else:
        print(f"Directory {directory_path} does not exist. Creating it.")
        os.makedirs(directory_path)

def open_tradingview():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('TradingView')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)  # wait for the app to load

def take_chart_snapshot():
    pyautogui.hotkey('ctrl', 'alt', 's')
    time.sleep(3)

def set_timeframe(timeframe):
    pyautogui.write(timeframe)
    pyautogui.press('enter')
    time.sleep(3)

def switch_to_next_coin():
    pyautogui.press('down')
    time.sleep(3)

def main():
    image_directory = r"C:\Users\Novandra Anugrah\Desktop\Images"
    clear_directory(image_directory)
    open_tradingview()

    timeframes = ['4h', '15']
    num_coins = 15

    for _ in range(num_coins):
        for timeframe in timeframes:
            set_timeframe(timeframe)
            take_chart_snapshot()
        switch_to_next_coin()

    winsound.Beep(1000, 500)
    winsound.Beep(1000, 500)

if __name__ == '__main__':
    main()
