from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

# Path to your ChromeDriver
chrome_driver_path = 'C:\\WebDrivers\\chromedriver.exe'  # Update this to your actual path

# List of crypto symbols and timeframes to screenshot
crypto_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']  # Add more as needed
timeframes = ['15', '60', '240']  # 15 minutes, 1 hour, 4 hours

# Initialize the WebDriver
try:
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
except Exception as e:
    print(f"Error initializing WebDriver: {e}")
    exit(1)

# Function to set up the indicators on TradingView
def setup_indicators():
    try:
        search_box = driver.find_element(By.XPATH, '//input[@data-name="search"]')
        indicators = ['MACD', 'RSI', 'Volume']
        for indicator in indicators:
            search_box.clear()
            search_box.send_keys(indicator + Keys.RETURN)
            time.sleep(2)

        # Add Moving Averages
        search_box.clear()
        search_box.send_keys('Moving Average' + Keys.RETURN)
        time.sleep(2)
        # Configure the Moving Averages if necessary
    except Exception as e:
        print(f"Error setting up indicators: {e}")

# Directory to save screenshots
screenshot_dir = 'tradingview_screenshots'
os.makedirs(screenshot_dir, exist_ok=True)

# Open TradingView and log in if necessary
try:
    driver.get('https://www.tradingview.com')
    time.sleep(10)  # Adjust as needed for the page to load
except Exception as e:
    print(f"Error loading TradingView: {e}")
    driver.quit()
    exit(1)

# Loop through each symbol and timeframe
for symbol in crypto_symbols:
    for timeframe in timeframes:
        try:
            # Navigate to the chart
            chart_url = f'https://www.tradingview.com/chart/?symbol=BINANCE:{symbol}'
            driver.get(chart_url)
            time.sleep(5)  # Wait for the chart to load

            # Set the timeframe
            timeframe_input = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/span[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/span')
            timeframe_input.click()
            time.sleep(1)
            timeframe_input.send_keys(timeframe + Keys.RETURN)
            time.sleep(3)  # Wait for the chart to update

            # Set up the indicators
            setup_indicators()

            # Use the "Take a Snapshot" feature
            snapshot_button = driver.find_element(By.XPATH, '//*[@title="Take a snapshot"]')
            snapshot_button.click()
            time.sleep(2)

            # Click on "Copy link" to get the snapshot URL
            copy_link_button = driver.find_element(By.XPATH, '//*[@class="tv-button tv-button--primary js-copy-url-button"]')
            copy_link_button.click()
            time.sleep(1)

            # Get the snapshot URL from the clipboard
            snapshot_url = driver.execute_script("return navigator.clipboard.readText();")
            print(f"Snapshot URL: {snapshot_url}")

            # Save the snapshot URL to a file
            with open(os.path.join(screenshot_dir, f'{symbol}_{timeframe}.txt'), 'w') as f:
                f.write(snapshot_url)

        except Exception as e:
            print(f"Error processing {symbol} on {timeframe} timeframe: {e}")

# Close the browser
driver.quit()
