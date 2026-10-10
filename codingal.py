
from selenium import webdriver

class CodingalHelper:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def open_quiz(self):
        self.browser.get("https://www.codingal.com/")
        input("Log in, open your quiz, then press Enter...")

    def read_question(self):
        print("\n--- PAGE TEXT ---")
        text = self.browser.find_element(
            "tag name", "body"
        ).text
        print(text[:4000])

    def start(self):
        self.open_quiz()

        while True:
            command = input(
                "\nEnter = read page, Q = quit: "
            )

            if command.lower() == "q":
                break

            self.read_question()

        self.browser.quit()


bot = CodingalHelper()
bot.start()
