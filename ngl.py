import uuid
import colorama
import cloudscraper


class NGLWrapper:
    def __init__(self):
        self.s = cloudscraper.create_scraper()
        self.submit_url = "https://ngl.link/api/submit"
        self.username = None
        self.counter = 0

    def error(self, message):
        print(colorama.Fore.RED + message + colorama.Style.RESET_ALL)

    def success(self, message):
        print(colorama.Fore.GREEN + message + colorama.Style.RESET_ALL)

    def info(self, message):
        print(colorama.Fore.BLUE + message + colorama.Style.RESET_ALL)

    def set_username(self,username):
        self.username = username

    def send_question(self,question):
        if self.username == None:
            self.error("You must set a username before sending a question.")
            return False
        device_id = str(uuid.uuid4())
        data = {
            "username": self.username,
            "question": question,
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""}
        r = self.s.post(self.submit_url, data=data)
        if r.status_code == 200:
            self.counter += 1
            self.success(f"[{self.counter}] Question sent! Question: "+question)
            return True
        else:
            self.error("Error sending question. Status code: "+str(r.status_code))
            self.error("Text: "+r.text)
            return False