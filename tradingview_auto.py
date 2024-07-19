import pyautogui
import time

def open_tradingview():
    """
    Fungsi untuk membuka aplikasi TradingView menggunakan shortcut keyboard Windows.
    """
    pyautogui.press('win')  # Tekan tombol Windows
    time.sleep(1)
    pyautogui.write('TradingView')  # Tulis 'TradingView' untuk mencari aplikasi
    time.sleep(1)
    pyautogui.press('enter')  # Tekan Enter untuk membuka aplikasi
    time.sleep(10)  # Tunggu hingga aplikasi terbuka

def take_chart_snapshot():
    """
    Fungsi untuk mengambil snapshot dari chart menggunakan shortcut keyboard.
    """
    pyautogui.hotkey('ctrl', 'alt', 's')
    time.sleep(5)  # Tunggu beberapa detik untuk memastikan snapshot selesai

def switch_to_next_chart():
    """
    Fungsi untuk berpindah ke chart berikutnya dengan menekan tombol 'space'.
    """
    pyautogui.press('space')
    time.sleep(5)  # Tunggu beberapa detik untuk memastikan chart berubah

def main():
    open_tradingview()

    for i in range(15):
        take_chart_snapshot()  # Ambil snapshot dari chart saat ini
        print(f"Snapshot {i+1} taken.")
        switch_to_next_chart()  # Pindah ke chart berikutnya
        print(f"Switched to next chart {i+1}.")

if __name__ == '__main__':
    main()
