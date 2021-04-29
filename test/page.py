from poium import Page, Element


class LoginPage(Page):
    search_input = Element(name='wd', describe="搜索框")

    def search(self):
        self.search_input.send_keys("poium")
