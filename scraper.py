import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# The Main Scraping Function
def initiate(url):
    
    # Define path and install Chromedriver
    chromedriver_path = ChromeDriverManager().install()
    if not chromedriver_path.endswith("chromedriver.exe"):
        chromedriver_dir = os.path.dirname(chromedriver_path)
        chromedriver_path = os.path.join(chromedriver_dir, "chromedriver.exe")

    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--headless=new")

    # Begin the driver
    driver = webdriver.Chrome(service=service, options=options)
    actions = ActionChains(driver)
    driver.maximize_window()
    driver.get(url)

    wait=WebDriverWait(driver,10)
    time.sleep(3)

    # Define and display the main raiting of the restaurant
    rating1 = driver.find_elements(By.XPATH, '//div[@class="sc-1q7bklc-5 kHxpSk"]//div[@class="sc-1q7bklc-1 cILgox"]')
    Dinerating = rating1[0].text.strip()
    Delirating = rating1[1].text.strip()
    print("Dining Ratings: ", Dinerating, " Stars")
    print("Delivery Ratings: ", Delirating, " Stars")
    review = driver.find_elements(By.XPATH, '//p[@class="sc-1hez2tp-0 sc-eCXBzT iIAoyK"]')
    name = driver.find_elements(By.XPATH, '//p[@class="sc-1hez2tp-0 sc-gSbCxx gfIQBW"]')
    flag = False
    for count in range(100):
        try:
            time.sleep(0.5)
            # Locate the elements and display them
            review = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//p[@class="sc-1hez2tp-0 sc-hfLElm hreYiP"]')))
            name = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//p[@class="sc-1hez2tp-0 sc-lenlpJ dCAQIv"]')))
            rating = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="sc-1q7bklc-1 cILgox"]')))
            
            # Locate and display the 5 comments
            for i in range(2,7):
                try:
                    reviewpara = review[i-2].text.strip()
                    reviewrating = rating[i].text.strip()
                    reviewname = name[i-2].text.strip()
                    if not reviewpara:
                        reviewpara = "No Review Written"
                    print(f"\n\nReview {i-1 + count*5}: ", reviewrating, "Stars Rated\nFrom", reviewname, ":\n", reviewpara, "\n")
                except IndexError:
                    print("Reached end of reviews")

            # Scroll to make sure that next page button is visible
            driver.execute_script("window.scrollTo(0, 1500);")
            time.sleep(0.5)

            # Try multiple button location strategies
            try:
                # First try:
                next_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@href]//div[text()="{count+2}"]')))
                next_button.click()
            except:
                print("End of Pages")
                flag = True

            # Last Resort
            # try:
            #     next_button.click()
            #     print("third try")
            # except:
            #     driver.execute_script("arguments[0].click();", next_button)
            #     print("fourth try")

        except Exception as e:
            print(f"Error during pagination: {str(e)}")
            break
        if flag==True:
            break

    driver.quit()
    print("Driver Stopped")


# Define the review url here
# Example: 
url = "https://www.zomato.com/mumbai/persian-darbar-3-kurla/reviews"
initiate(url)