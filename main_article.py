from model.database import DatabaseEngine
from controller.Article_controller import ArticleController
from exceptions import Error


def main():
    print("Welcome to the Shop")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    Article_controller = ArticleController(database_engine)

if __name__ == "__main__":
    main()