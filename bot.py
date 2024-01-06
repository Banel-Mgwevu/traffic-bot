from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup
import random
import time

# Function to get a list of free proxies from free-proxy-list.net
def get_proxies():
    proxies = []
    try:
        response = requests.get('https://www.free-proxy-list.net/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='table-striped')
            rows = table.find_all('tr')
            for row in rows[1:]:
                columns = row.find_all('td')
                ip = columns[0].get_text()
                port = columns[1].get_text()
                proxy = f'{ip}:{port}'
                proxies.append(proxy)
    except Exception as e:
        print(f"An error occurred while retrieving proxies: {e}")
    return proxies

# URL of the website
url = 'https://example.com'  # Replace with the correct URL

# List of devices to simulate
devices = [
    {"deviceName": "iPhone X"},
    {"deviceName": "Laptop with HiDPI screen"},
    # Add or replace with more devices as needed
]

# Fetch proxies
proxies = get_proxies()

for device in devices:
    driver = None
    try:
        proxy = random.choice(proxies)
        print(f"Using proxy: {proxy}")  # Print selected proxy details

        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server=http://{proxy}')
        chrome_options.add_argument(f'--user-agent={device["deviceName"]}')

        service = Service(executable_path='C:/Users/X/Desktop/Python/chrome/chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.set_page_load_timeout(60)  # Set page load timeout to 60 seconds
        driver.set_script_timeout(30)     # Set script timeout to 30 seconds

        # Open the website
        driver.get(url)

        # Wait for the page to load completely (waiting for title presence)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))

        # Wait for 5 seconds (example wait)
        time.sleep(5)

        # Scroll down (Example: scrolling down 500 pixels)
        driver.execute_script("window.scrollTo(0, 500);")

        # Rest of your code for interacting with the website...

    except requests.exceptions.ProxyError as pe:
        print(f"Proxy error occurred while simulating {device['deviceName']}: {pe}")
        # Handle proxy error, e.g., skip or retry with a different proxy

    except TimeoutException as te:
        print(f"Timeout occurred while simulating {device['deviceName']}: {te}")
        # Handle timeout error

    except Exception as e:
        print(f"An error occurred while simulating {device['deviceName']}: {e}")

    finally:
        if driver is not None:
            driver.quit()
