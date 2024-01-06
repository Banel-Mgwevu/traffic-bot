
# Web Interaction Script with Proxies and Selenium

This Python script utilizes Selenium WebDriver and proxies to simulate different devices and interact with a specified website. The script cycles through a list of devices, sets up a Chrome WebDriver instance with a randomly selected proxy, and performs various actions on the specified URL.

## Prerequisites

- Python 3.x
- Required Python libraries: `selenium`, `requests`, `beautifulsoup4`

## Setup

1. Install the required Python libraries:
   ```bash
   pip install selenium requests beautifulsoup4
   ```

2. Download the Chrome WebDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/) and set the path in the script:
   ```python
   service = Service(executable_path='C:/Users/X/Desktop/Python/chrome/chromedriver.exe')
   ```

## Usage

1. Customize the URL:
   ```python
   url = 'https://example.com'  # Replace with the correct URL
   ```

2. Define devices to simulate:
   ```python
   devices = [
       {"deviceName": "iPhone X"},
       {"deviceName": "Laptop with HiDPI screen"},
       # Add or replace with more devices as needed
   ]
   ```

3. Run the script:
   ```bash
   bot.py
   ```

## Functionality

- **Fetching Proxies**: The script retrieves a list of free proxies from 'https://www.free-proxy-list.net/'.
- **Device Simulation**: It cycles through each device, sets up a Chrome WebDriver instance with a random proxy and user agent, and interacts with the specified URL.
- **Error Handling**: The script includes error handling for proxy errors, timeouts, and other exceptions that may occur during execution.

## License

This script is provided under the [MIT License](LICENSE).

## Disclaimer

Please use this script responsibly and comply with the website's terms of service and legal requirements. Be mindful of web scraping or automated interactions with websites as they might violate policies.

---
