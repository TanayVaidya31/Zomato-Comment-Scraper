# Zomato Comment Scraper

This Python script uses Selenium to scrape reviews, ratings, and reviewer names from a Zomato restaurant page. The script automatically scrolls and paginates through the reviews, bypassing bot detection mechanisms. It prints out the dining and delivery ratings, followed by individual reviews, ratings, and reviewer names.

## Features

- Scrapes dining and delivery ratings for a given Zomato restaurant.
- Extracts review text, ratings, and reviewer names.
- Automatically paginates through multiple pages of reviews.
- Bypasses bot detection by disabling the automation flags in Chrome.
- Runs in headless mode for faster execution.

## Requirements

- Python 3.x
- Selenium library
- WebDriver Manager for Chrome
- Chrome browser installed

## Installation

1. Install the required libraries:
   ```bash
   pip install selenium webdriver-manager
   ```

2. Make sure Chrome is installed on your system.

## Usage

1. Modify the URL in the `url` variable to target the desired Zomato restaurant's review page:
   ```python
   url = "https://www.zomato.com/mumbai/persian-darbar-3-kurla"
   ```

2. Run the script:
   ```bash
   python <script_name>.py
   ```