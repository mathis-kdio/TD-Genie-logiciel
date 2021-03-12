from vue.common import Common


class ArticleVue:
    """
    Article Vue
    Articles interface features
    """

    def __init__(self, Article_controller):
        self._common = Common()
        self._Article_controller = Article_controller

    def add_Article(self):
        data = {}
        data['name'] = self._common.ask_name(key_name="name")
        data['price'] = self._common.ask_name(key_name="price")
        return self._Article_controller.create_article(data)
