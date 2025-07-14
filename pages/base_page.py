from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_link(self, link):
        self.driver.get(link)

    def find(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def another_click(self, locator):
        return self.driver.execute_script("arguments[0].click();", self.find(locator))

    def add_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_page(self):
        return self.driver.current_url

    def wait_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def clickable_elem(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def visibility_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def check_no_text_in_element(self, locator, text):
        return self.wait.until_not(EC.text_to_be_present_in_element(locator, text))

    def check_text_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def wait_invis(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        self.driver.execute_script(script, source_element, target_element)
