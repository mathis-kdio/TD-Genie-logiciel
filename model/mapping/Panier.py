from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint

class Panier:
    __tablename__ = 'Panier'
    __table_args__ = (UniqueConstraint('Articles'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    Articles = Column(String(50), nullable=False)


    email = Column(String(256), nullable=False)
    type = Column(String(10), nullable=False)

    def __init__(self, ListeArticle):
        self.ListeArticle = ListeArticle();

    def addArticles(self, NewArticle):
        self.ListeArticle.append(NewArticle)