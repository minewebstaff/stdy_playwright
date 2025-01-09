# 賢者 スクレイプ用

from playwright.sync_api import sync_playwright


class KenjaAdmin():
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def close(self):
        self.browser.close()
        self.playwright.stop()

    def login(self, id:str, passwd:str):
        self.page.goto("http://kjsv01.hg.local/hagoromo/X/KNJXMENU/index.php")
        self.page.get_by_placeholder("ログインID").fill(value=id)
        self.page.get_by_placeholder('パスワード').fill(passwd)
        self.page.get_by_role('button',).click()

    def goto_application(self):
        self.page.get_by_text("出願").get_by_text("出願確認").get_by_text("02．申込別志願者更新").click()

    def goto(self, url):
        self.page.goto(url)

