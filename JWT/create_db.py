from app import db, create_app

def create_database():
    app = create_app()
    with app.app_context():
        result = db.create_all()
        print(result)

if __name__ == "__main__":
    create_database()

