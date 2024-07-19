const puppeteer = require('puppeteer');

async function loginToTradingView(page) {
    await page.goto('https://www.tradingview.com');
    await page.waitForSelector('.tv-header__link.tv-header__link--signin');
    await page.click('.tv-header__link.tv-header__link--signin');
    await page.waitForSelector('input[name="username"]');
    await page.type('input[name="username"]', 'your_username'); // Ganti dengan username Anda
    await page.type('input[name="password"]', 'your_password'); // Ganti dengan password Anda
    await page.click('button[type="submit"]');
    await page.waitForNavigation({ waitUntil: 'networkidle0' });
}

async function takeScreenshot(symbol, imagePath) {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    try {
        await loginToTradingView(page);

        const url = `https://www.tradingview.com/chart/?symbol=BINANCE:${symbol}`;
        await page.goto(url, { waitUntil: 'networkidle2', timeout: 60000 }); // 60 detik

        // Logika untuk mengatur timeframe menjadi 1 jam
        await page.evaluate(() => {
            document.querySelector('.input-3lfOzLDc').value = '60'; // 1 jam
            document.querySelector('.input-3lfOzLDc').dispatchEvent(new Event('change'));
        });

        await page.waitForTimeout(3000); // Tunggu hingga grafik diperbarui

        // Logika untuk mengatur indikator
        const indicators = ['MACD', 'RSI', 'Volume'];
        for (const indicator of indicators) {
            await page.click('.search-1CZZ-W_j');
            await page.keyboard.type(indicator);
            await page.keyboard.press('Enter');
            await page.waitForTimeout(2000);
        }

        await page.screenshot({ path: imagePath });

        console.log(`Screenshot for ${symbol} saved to ${imagePath}`);
    } catch (error) {
        console.error(`Error taking screenshot for ${symbol}:`, error);
    } finally {
        await browser.close();
    }
}

const symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT'];

symbols.forEach(symbol => {
    const imagePath = `screenshots/${symbol}_60.png`; // File name includes the timeframe of 1 hour
    takeScreenshot(symbol, imagePath);
});
