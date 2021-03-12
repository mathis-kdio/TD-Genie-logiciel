from model.dao.Article_dao import ArticleDAO
from exceptions import Error, InvalidData

class ArticleController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_article(self):
        with self._database_engine.new_session() as session:
            articles = ArticleDAO(session).get_all()
            articles_data = [article.to_dict() for article in articles]
        return articles_data

    def get_member(self, article_id):
        with self._database_engine.new_session() as session:
            article = ArticleDAO(session).get(article_id)
            article_data = article.to_dict()
        return article_data

    def create_article(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                article = ArticleDAO(session).create(data)
                article_data = article.to_dict()
                return article_data
        except Error as e:
            # log error
            raise e