# from app import request_info
from models.base_model import Feedback, engine, User, Solution
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


def solution_submission(text, id):
    try:
        solution = Solution(solution_text=text, request_id=id)
        session.add(solution)
        session.commit()
        return "Solution Given"
    except BaseException:
        session.rollback()
        raise


def get_solutions(id):
    info = session.query(Solution).filter(Solution.request_id==id).all()
    return info


def get_users():
    users =session.query(User).all()
    return users


def log_in(mannumber):
    try:
        user = session.query(User).filter(User.mannumber==mannumber).first()

        if user is not None:
            print("=>\n{} this is it".format(user.password))
            return user.password
        else:
            return None
    except:
        raise


def delete_request(id):
    user_request = session.query(Feedback).get(id)
    session.delete(user_request)
    session.commit()
    return "Deleted"

def get_request(id):
    # user_request = session.query(Feedback).get(id)
    my_user_request = session.query(Feedback).filter(Feedback.request_id==id).first()
    return my_user_request


def feedback_edit(title, info, id):
    try:
        fuser_request = session.query(Feedback).get(id)
        # feedback = Feedback(request_title=title, request_info=info)
        # session.update(fuser_request)
        fuser_request.request_title = title
        fuser_request.request_info = info
        session.commit()
        return 'Feedback updated'
    except BaseException:
        session.rollback()
        raise
