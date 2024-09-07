# TradingView Snapshot Automation

This is a personal Python application designed to automate the process of taking chart snapshots from TradingView. The script uses `PyAutoGUI` to interact with the TradingView interface, `tkinter` for the graphical user interface (GUI), and it provides a configurable number of coins to process.


## How to Use

1. **Install TradingView App:**

- If you haven't installed the TradingView App on your local computer, you can download and install it first.
- You can download the TradingView App from the official website: [Download TradingView](https://www.tradingview.com/desktop/).
- Save your Stocks, Forex, and Crypto charts in the watchlist for easy access.
- You can change your TradingView download path by clicking on your profile, then navigating to **App Settings** -> **General** -> **Downloads**.  


2. **Run the Application:**
   - If you have the executable (`.exe`), simply double-click to run the program.
   - If you're running the script directly, use a Python environment to execute the script.

3. **Set Number of Coins:**
   - Use the input field in the GUI to specify the number of coins you want to process.

4. **Clear Directory**
   - If you want to clear the folder directory, check the checkbox labeled "Clear directory."
   - Set your directory path to the folder you want to clean.

5. **Set Timeframe**
   - Choose your desired timeframes from the dropdown menus provided.

6. **Start the Automation:**
   - Click the "Run" button to begin the automation process. The application will open TradingView, take snapshots for each coin at the specified timeframes, and save the images.

7. **Stop the Automation:**
   - If needed, click the "Stop" button to halt the process at any time.