import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Set up Chrome WebDriver using a context manager
with webdriver.Firefox() as driver:

    # Navigate to the URL
    driver.get("https://jqueryui.com/droppable/")

    time.sleep(5)

    # Locate the frame and switch to the frame where drag and drop elements are located
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))

    # Locate draggable and droppable elements
    draggable_element = driver.find_element(By.ID, "draggable")
    droppable_element = driver.find_element(By.ID, "droppable")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Perform drag and drop
    actions.drag_and_drop(draggable_element, droppable_element).perform()
    time.sleep(5)

    driver.quit()
