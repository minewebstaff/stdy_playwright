from playwright.sync_api import sync_playwright


class MiraiAdmin():
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()

    def login(self, id:str, passwd:str):
        self.page.goto("https://mirai-compass.net/adm/schAdmin/login.jsf")
        self.page.get_by_role('textbox').locator('nth=0').fill(id)
        self.page.get_by_role('textbox').locator('nth=1').fill(passwd)
        self.page.get_by_role('button').click()

    def goto_application(self):
        self.page.get_by_text("出願").get_by_text("出願確認").get_by_text("02．申込別志願者更新").click()

    def goto(self, url):
        self.page.goto(url)

