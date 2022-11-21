from models.base_model import Feedback, engine, User
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def feedback_submission(title, info):
    try:
        feedback = Feedback(request_title=title, request_info=info)
        session.add(feedback)
        session.commit()
        return 'Feedback added'
    except BaseException:
        session.rollback()
        raise


def requests_made():
    info = session.query(Feedback).all()
    return info


def register(mannumber, firstname, secondname, email, role, password):
    try:
        user = User(mannumber=mannumber, first_name=firstname, second_name=secondname, email=email, role=role, password=password)
        session.add(user)
        session.commit()
        return 'user added'
    
    except BaseException:
        session.rollback()
        raise

def get_users():
    users =session.query(User).all()
    return users

def log_in(mannumber):
    try:
        user = session.query(User).filter(User.mannumber==mannumber).first()

        if user is not None:
            print("==================>\n{} this is it".format(user.password))
            return user
        else:
            return None
    except:
        raise

