import pyautogui
import time
import winsound
import os
import shutil
import threading
import tkinter as tk
from tkinter import ttk

# Variabel untuk kontrol threading
running = False

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

def run_bot(num_coins):
    global running
    running = True
    image_directory = r"C:\Users\Novandra Anugrah\Desktop\Images"
    clear_directory(image_directory)
    open_tradingview()

    timeframes = ['4h', '15']

    for _ in range(num_coins):
        if not running:
            break  # Exit loop if stopped
        for timeframe in timeframes:
            set_timeframe(timeframe)
            take_chart_snapshot()
        switch_to_next_coin()

    winsound.Beep(1000, 500)
    winsound.Beep(1000, 500)

def stop_bot():
    global running
    running = False  # Stop the bot

def start_threaded_bot():
    num_coins = int(num_coins_var.get())  # Get number of coins from GUI input
    threading.Thread(target=run_bot, args=(num_coins,)).start()  # Run the bot in a separate thread

# Setup GUI
root = tk.Tk()
root.title("TradingView Snapshot Automation")

# Input field for num_coins
num_coins_var = tk.StringVar(value='15')
ttk.Label(root, text="Number of Coins:").grid(column=0, row=0, padx=10, pady=10)
num_coins_entry = ttk.Entry(root, textvariable=num_coins_var)
num_coins_entry.grid(column=1, row=0, padx=10, pady=10)

# Run button
run_button = ttk.Button(root, text="Run", command=start_threaded_bot)
run_button.grid(column=0, row=1, padx=10, pady=20)

# Stop button
stop_button = ttk.Button(root, text="Stop", command=stop_bot)
stop_button.grid(column=1, row=1, padx=10, pady=20)

root.mainloop()
