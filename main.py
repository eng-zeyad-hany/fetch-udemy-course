# --------------------------------------------------
# AUTHOR BY | ZEYAD HANY 👌
# --------------------------------------------------

# CREATED IN 9/14/2023
# PYTHON CODE TO FETCH CONTENT FROM UDEMY WEBSITE.
# --------------------------------------------------
# Import necessary modules from the Selenium library
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a Service object for the Chrome WebDriver (This is used to configure Chrome options)
service = Service()  # This is the important line of code!

# Configure Chrome options
options = webdriver.ChromeOptions()
# You can add additional options here if needed, like running Chrome in headless mode.

# Create a WebDriver instance for Chrome with the specified service and options
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()  # Maximizes the browser window

# Navigate to the Udemy course page
driver.get("https://www.udemy.com/course/the-complete-javascript-course/")
driver.implicitly_wait(30)  # Implicitly wait for up to 30 seconds for elements to appear
time.sleep(4)  # Sleep for 4 seconds (useful for waiting after page load)

# Find the "Show more" button and click it
driver.find_element(By.XPATH, '//*[@id="main-content-anchor"]/div[5]/div/div[5]/div/button').click()

time.sleep(4)  # Sleep for 4 seconds (useful for waiting after the button click)

# Expand all sections of the course
driver.find_element(By.XPATH, '//*[@id="main-content-anchor"]/div[5]/div/div[5]/div/div[1]/button').click()
time.sleep(3)  # Sleep for 3 seconds (useful for waiting after the section expansion)

# Find all section titles and video titles using a CSS selector
section_title_and_videos_title = driver.find_elements(By.CSS_SELECTOR, '.accordion-panel-module--panel--3_kkG')

titles = []
for title in section_title_and_videos_title:
    titles.append(title.text)  # Extract text content of each title and append to the 'titles' list

print(titles)  # Print the list of section titles and video titles

# Quit the WebDriver, closing the opened browser
driver.quit()

# //////////////////////////////////////////////////////////////////////////////////
# YOU can copy the result from the fetching and replace it with [].
# titles = []


# FORMATTING THE RESULT
# Iterate through each section title in the 'titles' list
for section_titles in titles:
    # Split the section title by newline character and take the first line
    lines = section_titles.split('\n')[0]
    # Print the first line
    print(lines)

# Iterate through each section title in the 'titles' list again
for section in titles:
    # Split the section text into lines
    lines = section.split('\n')
    try:
        # Try to find the index of 'Preview' in the list of lines
        index = lines.index('Preview')
        # If found, remove 'Preview' from the list of lines
        lines.remove('Preview')
    except ValueError:
        # If 'Preview' is not found, print an empty line
        print('')

    # Print a separator line
    print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
    print('\n')

    # Extract relevant information from the lines
    course_title = lines[0]
    lecture_count, course_duration = lines[1].split(' • ')

    # Print the course title
    print(f"{course_title}")
    print('------')
    # Print lecture count and course duration
    print(f"Lecture Count: {lecture_count}")
    print(f"Course Duration: {course_duration}")
    print('-------')
    print('\n')

    # Extract and format lecture information
    lectures = lines[2:]
    for i in range(0, len(lectures), 2):
        lecture_title = lectures[i]
        lecture_duration = lectures[i - 1]
        # Print lecture title and duration
        print(f"{lecture_title} ({lecture_duration})")
