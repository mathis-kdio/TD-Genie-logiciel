from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.Article import Article
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class ArticleDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Article).filter_by(id=id).order_by(Article.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Article).order_by(Article.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str):
        try:
            return self._database_session.query(Article).filter_by(firstname=name)\
                .order_by(Article.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            member = Article(-1, data.get('name'), data.get('price'))
            self._database_session.add(Article)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Article already exists")
        return member

    def update(self, member: Article, data: dict):
        if 'name' in data:
            member.firstname = data['name']
        if 'price' in data:
            member.lastname = data['price']

            self._database_session.merge(Article)
            self._database_session.flush()
        

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))