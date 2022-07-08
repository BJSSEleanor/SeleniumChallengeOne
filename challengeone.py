from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
browser = webdriver.Chrome()



def obtain_urls(browser):
    urls =  ["https://econpy.pythonanywhere.com/ex/001.html"]
    browser.get(urls[0])
    pages = browser.find_elements(By.CSS_SELECTOR, "a")
    for page in pages:
        urls.append(page.get_attribute("href")) 
    return urls


def obtain_data(browser, urls):
    df = pd.DataFrame(columns=["Name", "Price"])
    for url in urls:
        browser.get(url)
        names = browser.find_elements(By.CSS_SELECTOR, "div[title = 'buyer-name']")
        prices = browser.find_elements(By.CSS_SELECTOR, "span[class = 'item-price']")
        for i in range(len(names)):
            temp_df = pd.DataFrame([[names[i].text,prices[i].text]], columns=["Name", "Price"])
            df = pd.concat([df, temp_df])
    return df


if __name__ == "__main__":
    urls = obtain_urls(browser)
    df = obtain_data(browser, urls)
    df.to_csv("names_and_prices.csv", encoding='utf-8', index=False)
