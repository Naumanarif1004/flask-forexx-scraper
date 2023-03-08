from flask import Flask, render_template
import base64
import os
import sys
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
# download = str(os.getcwd())
# File = download + '\\' + 'Pdf_File'
# if not os.path.exists(File):
#     os.makedirs(File)
options.add_experimental_option("detach", True)
options.add_experimental_option('prefs', {
    # "download.default_directory": File,
    #     "savefile.default_directory": File,
    "profile.managed_default_content_settings.images": 2,
    "profile.managed_default_content_settings.ads": 1,
    "excludeSwitches": ["enable-logging"],
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False,
    "plugins.always_open_pdf_externally": True})
options.add_argument('--kiosk-printing')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--disable-infobars')
options.add_argument("--enable-webgl-developer-extensions")
options.add_argument("--enable-webgl-draft-extensions")
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-plugins-discovery')
options.add_argument('--start-maximized')



app = Flask(__name__)


def scroll_to_element_by_xpath(browser, xpath):
    element = browser.find_element(By.XPATH, xpath)
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()


@app.route('/')
def main():
    try:
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        browser.get('https://www.myfxbook.com/members/KP100/c-5000/9153311')
        browser.implicitly_wait(5)
        browser.maximize_window()
        # ---------------------------------------------------------------
        # clearing path
        for x in range(5):
            try:
                browser.find_element(By.XPATH, '//*[@id="popupAdContainer"]/div/div/div[2]/a').click()
                break
            except:
                pass

        for x in range(5):
            try:
                browser.find_element(By.XPATH, '//*[@id="blockWebNotification"]').click()
                break
            except:
                pass

        for x in range(5):
            try:
                browser.find_element(By.XPATH, '//*[@id="hideToolbarBtn"]').click()
                break
            except:
                pass

        # -------------------------------------------------
        # summary
        now = datetime.now()
        print('FOREX RESULTS\n')
        print('Current Date/Time: ', now)
        print('\nSUMMARY:')

        for x in range(10):
            try:
                gain = browser.find_element(By.XPATH,
                                            '//*[@id="infoStats"]/div/table[1]/tbody/tr[1]/td[2]/span/b/span').text
                if gain is None:
                    gain = ''
                break
            except:
                if x == 9:
                    gain = ''
                pass

        for x in range(10):
            try:
                abs_gain = browser.find_element(By.XPATH,
                                                '//*[@id="infoStats"]/div/table[1]/tbody/tr[2]/td[2]/span/span').text
                if abs_gain is None:
                    abs_gain = ''
                break
            except:
                if x == 9:
                    abs_gain = ''
                pass

        for x in range(10):
            try:
                daily_profit = browser.find_element(By.XPATH,
                                                    '//*[@id="infoStats"]/div/table[2]/tbody/tr[1]/td[2]/span').text
                if daily_profit is None:
                    daily_profit = ''
                break
            except:
                if x == 9:
                    daily_profit = ''
                pass

        for x in range(10):
            try:
                monthly_profit = browser.find_element(By.XPATH,
                                                      '//*[@id="infoStats"]/div/table[2]/tbody/tr[2]/td[2]/span').text
                if monthly_profit is None:
                    monthly_profit = ''
                break
            except:
                if x == 9:
                    monthly_profit = ''
                pass

        for x in range(5):
            try:
                drawdown = browser.find_element(By.XPATH,
                                                '//*[@id="infoStats"]/div/table[2]/tbody/tr[3]/td[2]/span').text
                if drawdown is None:
                    drawdown = ''
                break
            except:
                if x == 4:
                    drawdown = ''
                pass

        for x in range(10):
            try:
                equity = browser.find_element(By.XPATH,
                                              '//*[@id="infoStats"]/div/table[3]/tbody/tr[2]/td[2]/span/span').text
                if equity is None:
                    equity = ''
                break
            except:
                if x == 9:
                    equity = ''
                pass

        for x in range(10):
            try:
                last_update = browser.find_element(By.XPATH, '//*[@id="lastUpdatedTime"]').text
                if last_update is None:
                    last_update = ''
                break
            except:
                if x == 9:
                    last_update = ''
                pass

        print('Total gain: ', gain)
        print('Absolute gain: ', abs_gain)
        print('Daily Profit: ', daily_profit)
        print('Monthly Profit: ', monthly_profit)
        print('Drawdown: ', drawdown)
        print('Equity: ', equity)
        print('Last Update: ', last_update)

        # ------------------------------------------------------

        print('\nTODAY:')

        for x in range(5):
            try:
                today_gain = browser.find_element(By.XPATH,
                                                  '//*[@id="tradingPeriodsTable"]/tbody/tr[1]/td[2]/span[1]').text
                if today_gain is None:
                    today_gain = ''
                break
            except:
                if x == 4:
                    today_gain = ''
                pass

        for x in range(5):
            try:
                today_gain_dif = browser.find_element(By.XPATH,
                                                      '//*[@id="tradingPeriodsTable"]/tbody/tr[1]/td[2]/span[2]').text
                if today_gain_dif is None:
                    today_gain_dif = ''
                break
            except:
                if x == 4:
                    today_gain_dif = ''
                pass

        for x in range(5):
            try:
                today_pips = browser.find_element(By.XPATH,
                                                  '//*[@id="tradingPeriodsTable"]/tbody/tr[1]/td[4]/span[1]').text
                if today_pips is None:
                    today_pips = ''
                break
            except:
                if x == 4:
                    today_pips = ''
                pass

        for x in range(5):
            try:
                today_pips_dif = browser.find_element(By.XPATH,
                                                      '//*[@id="tradingPeriodsTable"]/tbody/tr[1]/td[4]/span[2]').text
                if today_pips_dif is None:
                    today_pips_dif = ''
                break
            except:
                if x == 4:
                    today_pips_dif = ''
                pass

        for x in range(5):
            try:
                today_win = browser.find_element(By.XPATH, '//*[@id="tradingPeriodsTable"]/tbody/tr[1]/td[5]').text
                if today_win is None:
                    today_win = ''
                break
            except:
                if x == 4:
                    today_win = ''
                pass

        for x in range(5):
            try:
                today_trades = browser.find_element(By.XPATH, '//*[@id="tradingPeriodsTable"]/tbody/tr[1]/td[6]').text
                if today_trades is None:
                    today_trades = ''
                break
            except:
                if x == 4:
                    today_trades = ''
                pass

        print('Gain: ', today_gain)
        print('Gain Difference: ', today_gain_dif)
        print('Pips: ', today_pips)
        print('Pips Difference: ', today_pips_dif)
        print('Win (difference): ', today_win)
        print('Trades (Difference): ', today_trades)
        # ------------------------------------------------------------------------------

        print('\nTHIS WEEK:')

        for x in range(5):
            try:
                this_Week_gain = browser.find_element(By.XPATH,
                                                      '//*[@id="tradingPeriodsTable"]/tbody/tr[2]/td[2]/span[1]').text
                if this_Week_gain is None:
                    this_Week_gain = ''
                break
            except:
                if x == 4:
                    this_Week_gain = ''
                pass

        for x in range(5):
            try:
                this_Week_gain_dif = browser.find_element(By.XPATH,
                                                          '//*[@id="tradingPeriodsTable"]/tbody/tr[2]/td[2]/span[2]').text
                if this_Week_gain_dif is None:
                    this_Week_gain_dif = ''
                break
            except:
                if x == 4:
                    this_Week_gain_dif = ''
                pass

        for x in range(5):
            try:
                this_Week_pips = browser.find_element(By.XPATH,
                                                      '//*[@id="tradingPeriodsTable"]/tbody/tr[2]/td[4]/span[1]').text
                if this_Week_pips is None:
                    this_Week_pips = ''
                break
            except:
                if x == 4:
                    this_Week_pips = ''
                pass

        for x in range(5):
            try:
                this_Week_pips_dif = browser.find_element(By.XPATH,
                                                          '//*[@id="tradingPeriodsTable"]/tbody/tr[2]/td[4]/span[2]').text
                if this_Week_pips_dif is None:
                    this_Week_pips_dif = ''
                break
            except:
                if x == 4:
                    this_Week_pips_dif = ''
                pass

        for x in range(5):
            try:
                this_Week_win = browser.find_element(By.XPATH, '//*[@id="tradingPeriodsTable"]/tbody/tr[2]/td[5]').text
                if this_Week_win is None:
                    this_Week_win = ''
                break
            except:
                if x == 4:
                    this_Week_win = ''
                pass

        for x in range(5):
            try:
                this_Week_trades = browser.find_element(By.XPATH,
                                                        '//*[@id="tradingPeriodsTable"]/tbody/tr[2]/td[6]').text
                if this_Week_trades is None:
                    this_Week_trades = ''
                break
            except:
                if x == 4:
                    this_Week_trades = ''
                pass

        print('Gain: ', this_Week_gain)
        print('Gain Difference: ', this_Week_gain_dif)
        print('Pips: ', this_Week_pips)
        print('Pips Difference: ', this_Week_pips_dif)
        print('Win (difference): ', this_Week_win)
        print('Trades (Difference): ', this_Week_trades)
        # ------------------------------------------------------------------------------

        print('\nTHIS MONTH:')

        for x in range(5):
            try:
                this_Month_gain = browser.find_element(By.XPATH,
                                                       '//*[@id="tradingPeriodsTable"]/tbody/tr[3]/td[2]/span[1]').text
                if this_Week_gain is None:
                    this_Week_gain = ''
                break
            except:
                if x == 4:
                    this_Week_gain = ''
                pass

        for x in range(5):
            try:
                this_Month_gain_dif = browser.find_element(By.XPATH,
                                                           '//*[@id="tradingPeriodsTable"]/tbody/tr[3]/td[2]/span[2]').text
                if this_Month_gain_dif is None:
                    this_Month_gain_dif = ''
                break
            except:
                if x == 4:
                    this_Month_gain_dif = ''
                pass

        for x in range(5):
            try:
                this_Month_pips = browser.find_element(By.XPATH,
                                                       '//*[@id="tradingPeriodsTable"]/tbody/tr[3]/td[4]/span[1]').text
                if this_Month_pips is None:
                    this_Month_pips = ''
                break
            except:
                if x == 4:
                    this_Month_pips = ''
                pass

        for x in range(5):
            try:
                this_Month_pips_dif = browser.find_element(By.XPATH,
                                                           '//*[@id="tradingPeriodsTable"]/tbody/tr[3]/td[4]/span[2]').text
                if this_Month_pips_dif is None:
                    this_Month_pips_dif = ''
                break
            except:
                if x == 4:
                    this_Month_pips_dif = ''
                pass

        for x in range(5):
            try:
                this_Month_win = browser.find_element(By.XPATH, '//*[@id="tradingPeriodsTable"]/tbody/tr[3]/td[5]').text
                if this_Month_win is None:
                    this_Month_win = ''
                break
            except:
                if x == 4:
                    this_Month_win = ''
                pass

        for x in range(5):
            try:
                this_Month_trades = browser.find_element(By.XPATH,
                                                         '//*[@id="tradingPeriodsTable"]/tbody/tr[3]/td[6]').text
                if this_Month_trades is None:
                    this_Month_trades = ''
                break
            except:
                if x == 4:
                    this_Month_trades = ''
                pass

        print('Gain: ', this_Month_gain)
        print('Gain Difference: ', this_Month_gain_dif)
        print('Pips: ', this_Month_pips)
        print('Pips Difference: ', this_Month_pips_dif)
        print('Win (difference): ', this_Month_win)
        print('Trades (Difference): ', this_Month_trades)
        # ------------------------------------------------------------------------------
        print('\nTHIS YEAR:')

        for x in range(5):
            try:
                this_Year_gain = browser.find_element(By.XPATH,
                                                      '//*[@id="tradingPeriodsTable"]/tbody/tr[4]/td[2]/span[1]').text
                if this_Year_gain is None:
                    this_Year_gain = ''
                break
            except:
                if x == 4:
                    this_Year_gain = ''
                pass

        for x in range(5):
            try:
                this_Year_gain_dif = browser.find_element(By.XPATH,
                                                          '//*[@id="tradingPeriodsTable"]/tbody/tr[4]/td[2]/span[2]').text
                if this_Year_gain_dif is None:
                    this_Year_gain_dif = ''
                break
            except:
                if x == 4:
                    this_Year_gain_dif = ''
                pass

        for x in range(5):
            try:
                this_Year_pips = browser.find_element(By.XPATH,
                                                      '//*[@id="tradingPeriodsTable"]/tbody/tr[4]/td[4]/span[1]').text
                if this_Year_pips is None:
                    this_Year_pips = ''
                break
            except:
                if x == 4:
                    this_Year_pips = ''
                pass

        for x in range(5):
            try:
                this_Year_pips_dif = browser.find_element(By.XPATH,
                                                          '//*[@id="tradingPeriodsTable"]/tbody/tr[4]/td[4]/span[2]').text
                if this_Year_pips_dif is None:
                    this_Year_pips_dif = ''
                break
            except:
                if x == 4:
                    this_Year_pips_dif = ''
                pass

        for x in range(5):
            try:
                this_Year_win = browser.find_element(By.XPATH, '//*[@id="tradingPeriodsTable"]/tbody/tr[4]/td[5]').text
                if this_Year_win is None:
                    this_Year_win = ''
                break
            except:
                if x == 4:
                    this_Year_win = ''
                pass

        for x in range(5):
            try:
                this_Year_trades = browser.find_element(By.XPATH,
                                                        '//*[@id="tradingPeriodsTable"]/tbody/tr[4]/td[6]').text
                if this_Year_trades is None:
                    this_Year_trades = ''
                break
            except:
                if x == 4:
                    this_Year_trades = ''
                pass

        print('Gain: ', this_Year_gain)
        print('Gain Difference: ', this_Year_gain_dif)
        print('Pips: ', this_Year_pips)
        print('Pips Difference: ', this_Year_pips_dif)
        print('Win (difference): ', this_Year_win)
        print('Trades (Difference): ', this_Year_trades)
        # ------------------------------------------------------------------------------

        print('\n********ADVANCE STATISTICS********')

        for x in range(5):
            try:
                Trades = browser.find_element(By.XPATH,
                                              '//*[@id="tradesListData"]/div/div/div[1]/table/tbody/tr[1]/td[2]').text
                if Trades is None:
                    Trades = ''
                break
            except:
                if x == 4:
                    Trades = ''
                pass

        for x in range(5):
            try:
                Pips = browser.find_element(By.XPATH,
                                            '//*[@id="tradesListData"]/div/div/div[1]/table/tbody/tr[3]/td[2]').text
                if Pips is None:
                    Pips = ''
                break
            except:
                if x == 4:
                    Pips = ''
                pass

        for x in range(5):
            try:
                avg_win = browser.find_element(By.XPATH,
                                               '//*[@id="tradesListData"]/div/div/div[1]/table/tbody/tr[4]/td[2]').text
                if avg_win is None:
                    avg_win = ''
                break
            except:
                if x == 4:
                    avg_win = ''
                pass

        for x in range(5):
            try:
                avg_loss = browser.find_element(By.XPATH,
                                                '//*[@id="tradesListData"]/div/div/div[1]/table/tbody/tr[5]/td[2]').text
                if avg_loss is None:
                    avg_loss = ''
                break
            except:
                if x == 4:
                    avg_loss = ''
                pass

        for x in range(5):
            try:
                longs_won = browser.find_element(By.XPATH,
                                                 '//*[@id="tradesListData"]/div/div/div[2]/table/tbody/tr[1]/td[2]').text
                if longs_won is None:
                    longs_won = ''
                break
            except:
                if x == 4:
                    longs_won = ''
                pass

        for x in range(5):
            try:
                shorts_won = browser.find_element(By.XPATH,
                                                  '//*[@id="tradesListData"]/div/div/div[2]/table/tbody/tr[2]/td[2]').text
                if shorts_won is None:
                    shorts_won = ''
                break
            except:
                if x == 4:
                    shorts_won = ''
                pass

        for x in range(5):
            try:
                best_trade = browser.find_element(By.XPATH,
                                                  '//*[@id="tradesListData"]/div/div/div[2]/table/tbody/tr[5]/td[2]').text
                if best_trade is None:
                    best_trade = ''
                break
            except:
                if x == 4:
                    best_trade = ''
                pass

        for x in range(5):
            try:
                worst_trades = browser.find_element(By.XPATH,
                                                    '//*[@id="tradesListData"]/div/div/div[2]/table/tbody/tr[6]/td[2]').text
                if worst_trades is None:
                    worst_trades = ''
                break
            except:
                if x == 4:
                    worst_trades = ''
                pass

        for x in range(5):
            try:
                avg_trade_length = browser.find_element(By.XPATH,
                                                        '//*[@id="tradesListData"]/div/div/div[2]/table/tbody/tr[7]/td[2]').text
                if avg_trade_length is None:
                    avg_trade_length = ''
                break
            except:
                if x == 4:
                    avg_trade_length = ''
                pass

        for x in range(5):
            try:
                profit_factor = browser.find_element(By.XPATH,
                                                     '//*[@id="tradesListData"]/div/div/div[3]/table/tbody/tr[1]/td[2]').text
                if profit_factor is None:
                    profit_factor = ''
                break
            except:
                if x == 4:
                    profit_factor = ''
                pass

        for x in range(5):
            try:
                sharpe_ratio = browser.find_element(By.XPATH,
                                                    '//*[@id="tradesListData"]/div/div/div[3]/table/tbody/tr[3]/td[2]').text
                if sharpe_ratio is None:
                    sharpe_ratio = ''
                break
            except:
                if x == 4:
                    sharpe_ratio = ''
                pass

        for x in range(5):
            try:
                Z_score = browser.find_element(By.XPATH,
                                               '//*[@id="tradesListData"]/div/div/div[3]/table/tbody/tr[4]/td[2]').text
                if Z_score is None:
                    Z_score = ''
                break
            except:
                if x == 4:
                    Z_score = ''
                pass

        for x in range(5):
            try:
                expectancy = browser.find_element(By.XPATH,
                                                  '//*[@id="tradesListData"]/div/div/div[3]/table/tbody/tr[5]/td[2]').text
                if expectancy is None:
                    expectancy = ''
                break
            except:
                if x == 4:
                    expectancy = ''
                pass

        for x in range(5):
            try:
                ahpr = browser.find_element(By.XPATH,
                                            '//*[@id="tradesListData"]/div/div/div[3]/table/tbody/tr[6]/td[2]').text
                if ahpr is None:
                    ahpr = ''
                break
            except:
                if x == 4:
                    ahpr = ''
                pass

        for x in range(5):
            try:
                ghpr = browser.find_element(By.XPATH,
                                            '//*[@id="tradesListData"]/div/div/div[3]/table/tbody/tr[7]/td[2]').text
                if ghpr is None:
                    ghpr = ''
                break
            except:
                if x == 4:
                    ghpr = ''
                pass

        print('\nTRADES:')
        print('Trades: ', Trades)
        print('Pips: ', Pips)
        print('Average Win: ', avg_win)
        print('Average Loss: ', avg_loss)
        print('Longs Won: ', longs_won)
        print('Shorts Won: ', shorts_won)
        print('Best Trades: ', best_trade)
        print('Worst Trades: ', worst_trades)
        print('Average Trade Length: ', avg_trade_length)
        print('Profit Factor: ', profit_factor)
        print('Sharpe Ratio: ', sharpe_ratio)
        print('Z-Score: ', Z_score)
        print('Expectance: ', expectancy)
        print('AHPR: ', ahpr)
        print('GHPR: ', ghpr)
        # ------------------------------------------------------------------------------------

        for x in range(5):
            try:
                scroll_to_element_by_xpath(browser, '//*[@id="summaryListDataTab"]')
                browser.execute_script("window.scrollBy(0, 100)")
                browser.find_element(By.XPATH, '//*[@id="summaryListDataTab"]').click()
                break
            except:
                pass

        print('\nSUMMARY:')

        for x in range(5):
            try:
                l_trades = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[2]').text
                if l_trades is None:
                    l_trades = ''
                break
            except:
                if x == 4:
                    l_trades = ''
                pass

        for x in range(5):
            try:
                l_pips = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[3]/span').text
                if l_pips is None:
                    l_pips = ''
                break
            except:
                if x == 4:
                    l_pips = ''
                pass

        print(f'\nLongs: Trades = {l_trades}  Pips = {l_pips}')

        for x in range(5):
            try:
                s_trades = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[5]').text
                if s_trades is None:
                    s_trades = ''
                break
            except:
                if x == 4:
                    s_trades = ''
                pass

        for x in range(5):
            try:
                s_pips = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[6]/span').text
                if s_pips is None:
                    s_pips = ''
                break
            except:
                if x == 4:
                    s_pips = ''
                pass

        print(f'\nShorts: Trades = {s_trades}  Pips = {s_pips}')

        for x in range(5):
            try:
                total_trades = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[8]').text
                if total_trades is None:
                    total_trades = ''
                break
            except:
                if x == 4:
                    total_trades = ''
                pass

        for x in range(5):
            try:
                total_pips = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[9]/span').text
                if total_pips is None:
                    total_pips = ''
                break
            except:
                if x == 4:
                    total_pips = ''
                pass

        for x in range(5):
            try:
                total_won = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[11]').text
                if total_won is None:
                    total_won = ''
                break
            except:
                if x == 4:
                    total_won = ''
                pass

        for x in range(5):
            try:
                total_lost = browser.find_element(By.XPATH, '//*[@id="rowNum1"]/td[12]').text
                if total_lost is None:
                    total_lost = ''
                break
            except:
                if x == 4:
                    total_lost = ''
                pass

        print(f'\nTotal: Trades = {total_trades}  Pips = {total_pips}  Won = {total_won} Lost = {total_lost} ')
        # ---------------------------------------------------------------

        print('\n********MONTHLY ANALYTICS Gain(Change)********')
        print('\n2023:')

        for x in range(5):
            try:
                scroll_to_element_by_xpath(browser, '//*[@id="monthlyChartTabs"]/li[4]/a')
                browser.execute_script("window.scrollBy(0, 100)")
                browser.execute_script("window.scrollBy(0, 200)")
                break
            except:
                pass

        for x in range(5):
            try:
                m1 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-0 ']//*[name()='tspan']").text
                if m1 is None:
                    m1 = ''
                break
            except:
                if x == 4:
                    m1 = ''
                pass

        for x in range(5):
            try:
                m2 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-1 ']//*[name()='tspan']").text
                if m2 is None:
                    m2 = ''
                break
            except:
                if x == 4:
                    m2 = ''
                pass

        for x in range(5):
            try:
                m3 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-2 ']//*[name()='tspan']").text
                if m3 is None:
                    m3 = ''
                break
            except:
                if x == 4:
                    m3 = ''
                pass

        print(f'January : {m1}')
        print(f'February : {m2}')
        print(f'March : {m3}')
        # ------------------------------------------------------------------

        print('\n2022:')

        for x in range(5):
            try:
                browser.find_element(By.XPATH, '//*[@id="monthlyChartTabs"]/li[4]/a').click()
                break
            except:
                pass

        time.sleep(10)

        for x in range(5):
            try:
                m12 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-0 ']//*[name()='tspan']").text
                if m12 is None:
                    m12 = ''
                break
            except:
                if x == 4:
                    m11 = ''
                pass

        for x in range(5):
            try:
                m22 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-1 ']//*[name()='tspan']").text
                if m22 is None:
                    m22 = ''
                break
            except:
                if x == 4:
                    m22 = ''
                pass

        for x in range(5):
            try:
                m32 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-2 ']//*[name()='tspan']").text
                if m32 is None:
                    m32 = ''
                break
            except:
                if x == 4:
                    m32 = ''
                pass

        for x in range(5):
            try:
                m42 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-3 ']//*[name()='tspan']").text
                if m42 is None:
                    m42 = ''
                break
            except:
                if x == 4:
                    m42 = ''
                pass

        for x in range(5):
            try:
                m52 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-4 ']//*[name()='tspan']").text
                if m52 is None:
                    m52 = ''
                break
            except:
                if x == 4:
                    m52 = ''
                pass

        for x in range(5):
            try:
                m62 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-5 ']//*[name()='tspan']").text
                if m62 is None:
                    m62 = ''
                break
            except:
                if x == 4:
                    m62 = ''
                pass

        for x in range(5):
            try:
                m72 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-6 ']//*[name()='tspan']").text
                if m72 is None:
                    m72 = ''
                break
            except:
                if x == 4:
                    m72 = ''
                pass

        for x in range(5):
            try:
                m82 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-7 ']//*[name()='tspan']").text
                if m82 is None:
                    m82 = ''
                break
            except:
                if x == 4:
                    m82 = ''
                pass

        for x in range(5):
            try:
                m92 = browser.find_element(By.XPATH,
                                        "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-8 ']//*[name()='tspan']").text
                if m92 is None:
                    m92 = ''
                break
            except:
                if x == 4:
                    m92 = ''
                pass

        for x in range(5):
            try:
                m102 = browser.find_element(By.XPATH,
                                            "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-9 ']//*[name()='tspan']").text
                if m102 is None:
                    m102 = ''
                break
            except:
                if x == 4:
                    m102 = ''
                pass

        for x in range(5):
            try:
                m112 = browser.find_element(By.XPATH,
                                            "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-10 ']//*[name()='tspan']").text
                if m112 is None:
                    m112 = ''
                break
            except:
                if x == 4:
                    m112 = ''
                pass

        for x in range(5):
            try:
                m122 = browser.find_element(By.XPATH,
                                            "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-11 ']//*[name()='tspan']").text
                if m122 is None:
                    m122 = ''
                break
            except:
                if x == 4:
                    m122 = ''
                pass

        print(f'January : {m12}')
        print(f'February : {m22}')
        print(f'March : {m32}')
        print(f'April : {m42}')
        print(f'May : {m52}')
        print(f'June : {m62}')
        print(f'July : {m72}')
        print(f'August : {m82}')
        print(f'September : {m92}')
        print(f'October : {m102}')
        print(f'November : {m112}')
        print(f'December : {m122}')
        # ---------------------------------------------------------------------

        print('\n2021:')

        for x in range(5):
            try:
                browser.find_element(By.XPATH, '//*[@id="monthlyChartTabs"]/li[3]/a').click()
                break
            except:
                pass

        time.sleep(5)

        for x in range(5):
            try:
                m103 = browser.find_element(By.XPATH,
                                            "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-0 ']//*[name()='tspan']").text
                if m103 is None:
                    m103 = ''
                break
            except:
                if x == 4:
                    m103 = ''
                pass

        for x in range(5):
            try:
                m113 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-1 ']//*[name()='tspan']").text
                if m113 is None:
                    m113 = ''
                break
            except:
                if x == 4:
                    m113 = ''
                pass

        for x in range(5):
            try:
                m123 = browser.find_element(By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-data-label highcharts-data-label-color-2 ']//*[name()='tspan']").text
                if m123 is None:
                    m123 = ''
                break
            except:
                if x == 4:
                    m123 = ''
                pass

        print(f'October : {m103}')
        print(f'November : {m113}')
        print(f'December : {m123}')

        # paramss = {'landscape': False,
        #            'paperWidth': 8.27,
        #            'paperHeight': 11.69}
        # for x in range(10):
        #     try:
        #         data = browser.execute_cdp_cmd("Page.printToPDF", paramss)
        #         with open(f"{File}/Forex.pdf", 'wb') as file1:
        #             file1.write(base64.b64decode(data['data']))
        #         break
        #     except Exception as e:
        #         if x == 58:
        #             print(e)

        browser.quit()
        return render_template('index.html', now=now, gain=gain, abs_gain=abs_gain, daily_profit=daily_profit,
                               monthly_profit=monthly_profit, drawdown=drawdown, equity=equity, last_update=last_update,
                               today_gain=today_gain, today_gain_dif=today_gain_dif, today_pips=today_pips,
                               today_pips_dif=today_pips_dif, today_win=today_win, today_trades=today_trades,
                               this_Week_gain=this_Week_gain, this_Week_gain_dif=this_Week_gain_dif,
                               this_Week_pips_dif=this_Week_pips_dif, this_Week_win=this_Week_win,
                               this_Week_trades=this_Week_trades, this_Month_gain=this_Month_gain,
                               this_Month_gain_dif=this_Month_gain_dif, this_Month_pips=this_Month_pips,
                               this_Month_pips_dif=this_Month_pips_dif, this_Month_win=this_Month_win,
                               this_Month_trades=this_Month_trades, this_Year_gain=this_Year_gain,
                               this_Year_gain_dif=this_Year_gain_dif, this_Year_pips=this_Year_pips,
                               this_Year_pips_dif=this_Year_pips_dif, this_Year_win=this_Year_win,
                               this_Year_trades=this_Year_trades, Trades=Trades, Pips=Pips, avg_win=avg_win,
                               avg_loss=avg_loss, longs_won=longs_won, shorts_won=shorts_won, best_trade=best_trade,
                               worst_trades=worst_trades, avg_trade_length=avg_trade_length,
                               profit_factor=profit_factor, sharpe_ratio=sharpe_ratio, Z_score=Z_score,
                               expectancy=expectancy, ahpr=ahpr, ghpr=ghpr, l_trades=l_trades, l_pips=l_pips,
                               s_trades=s_trades, s_pips=s_pips, total_trades=total_trades, total_pips=total_pips,
                               total_won=total_won, total_lost=total_lost, this_Week_pips=this_Week_pips, m1=m1, m2=m2,
                               m3=m3, m12=m12, m22=m22, m32=m32, m42=m42, m52=m52, m62=m62, m72=m72, m82=m82, m92=m92,
                               m102=m102, m112=m112, m122=m122, m103=m103, m113=m113, m123=m123)
    except Exception as e:
        _, _, line_tb = sys.exc_info()
        line_num = line_tb.tb_lineno
        print(str(line_num), e)




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

