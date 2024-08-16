from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Scrape data from URL
def scrape_noun(url):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get(url)

    bid_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/h2")))

    bid_value = bid_element.text.strip() if bid_element else "Bid data not found"

    driver.quit()

    return bid_value

# Main loop
def main():
    base_url = "https://nouns.wtf/noun/"
    start_num = 10
    end_num = 1110

    with open("output.txt", "w", encoding="utf-8") as f:
        for i in range(start_num, end_num + 1):
            url = f"{base_url}{str(i).zfill(4)}"
            bid_data = scrape_noun(url)
            output_notif = f"Bid value from {url}: {bid_data}\n"
            print(output_notif)
            f.write(output_notif)


if __name__ == "__main__":
    main()
