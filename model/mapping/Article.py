from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class Article(Base):
    __tablename__ = 'Article'
    __table_args__ = (UniqueConstraint('name', 'price'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    name = Column(String(50), nullable=False)
    price = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Article(%s %s)>" % (self.firstname, self.lastname.upper())
