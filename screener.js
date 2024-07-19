const puppeteer = require('puppeteer');

async function takeScreenshot(url, imagePath) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);
    await page.screenshot({ path: imagePath });
    await browser.close();
}

takeScreenshot('https://www.tradingview.com/chart/oKlN94up/?symbol=BINANCE%3ABTCUSDT', 'BTC.png');
