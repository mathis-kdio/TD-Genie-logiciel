from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class Member(Base):
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)

    email = Column(String(256), nullable=False)
    type = Column(String(10), nullable=False)

    def __repr__(self):
        return "<Member(%s %s %s)>" % (self.firstname, self.lastname.upper(), self.type)

    def __init__(self, id, firstname, lastname, email, typeMembre):
        #Si on ne créer pas
        if (id != -1):
            self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.type = typeMembre

    def to_dict(self):
        return Member(self.id, self.firstname, self.lastname, self.email, self.type)
