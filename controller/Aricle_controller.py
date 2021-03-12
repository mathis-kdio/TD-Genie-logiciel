from exceptions import Error, InvalidData


class ArticleController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_article(self):
        with self._database_engine.new_session() as session:
            article = MemberDAO(session).get_all()
            article_data = [member.to_dict() for member in members]
        return article_data

    def get_member(self, member_id):
        with self._database_engine.new_session() as session:
            member = MemberDAO(session).get(member_id)
            member_data = member.to_dict()
        return member_data

    def create_article(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                member = MemberDAO(session).create(data)
                member_data = member.to_dict()
                return member_data
        except Error as e:
            # log error
            raise e