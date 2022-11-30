from email import message
from flask import Flask, Blueprint, render_template, request, abort, session, url_for, redirect
from datetime import datetime
from jinja2 import TemplateNotFound
from models.myforms import LoginForm, RequestForm, RegisterForm, SolutionForm
from models.base_model import Base, engine
from models.model_functions import delete_request, feedback_submission, requests_made, register, get_users, log_in, get_request, feedback_edit, solution_submission
from routes.req import my_req, display
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'ef2287ceaf05dada6c29bfb77a9f8f14'

app.register_blueprint(my_req)

@app.errorhandler(404)
def error(error):
    name = "page"
    return render_template('404.html', name=name), 404


@app.before_first_request
def create_db():
    Base.metadata.create_all(bind=engine)

@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm()

    if form.validate_on_submit():
        mannumber = form.mannumber.data
        password = form.password.data

        pwd = log_in(mannumber)

        if pwd is check_password_hash(pwd, password):
            # if check_password_hash(pwd, form.password.data):
            #     message = "It has accepted"
            #     # return render_template('index.html', form=form, message=message)
            #     return redirect(url_for('request_info'))
            # return render_template('index.html', form=form, message=f"{pwd} : hash")
            return render_template('index.html', form=form, message="logged in")
        return render_template('index.html', form=form, message=f"{pwd.first_name} : pwd")

    return render_template('index.html', form=form)


@app.route("/request_info", methods=['GET', 'POST'])
def request_info():
    form = RequestForm()

    info_f = requests_made()

    if form.validate_on_submit():
        request_info = form.request_info.data
        request_title = form.request_title.data

        retrieve = feedback_submission(request_title, request_info)
        if retrieve:
            form.request_info.data = ''
            form.request_title.data = ''
        return render_template('requests.html', form=form, retrieve=retrieve, info_f=info_f, deletion=delete_request)       

    return render_template('requests.html', form=form, info_f=info_f)


@app.route("/delete_request/<id>", methods=['GET', 'POST'])
def delete_req(id):
    form = RequestForm()

    delete = delete_request(id)
    
    return redirect(url_for("request_info"))


@app.route("/update_request/<id>", methods=["GET", "POST"])
def update_req(id):
    form = RequestForm()

    req = get_request(id)

    info_f = requests_made()

    form.request_info.data = req.request_info
    form.request_title.data = req.request_title

    message = req.request_info

    if form.validate_on_submit():
        request_info = form.request_info.data
        request_title = form.request_title.data

        retrieve = feedback_edit(request_title, request_info, req.request_id)
        if retrieve:
            form.request_info.data = ''
            form.request_title.data = ''

            return redirect(url_for("request_info", retrieve=retrieve))
        return redirect(url_for("request_info"))
    # return redirect(url_for("request_info"))
    return render_template("request_edit.html", form=form, info_f=info_f, id=id)


@app.route("/register_info", methods=['GET','POST'])
def register_info():
    form = RegisterForm()

    
    if form.validate_on_submit():
        mannumber= form.mannumber.data
        firstname= form.firstname.data
        secondname= form.secondname.data
        email= form.email.data
        role= form.role.data
        password= form.password.data


        # retrieve = register(mannumber,firstname,secondname,email,role, generate_password_hash(password))
        retrieve = register(mannumber,firstname,secondname,email,role, generate_password_hash(password))

        if retrieve:
            form.mannumber.data=''
            form.firstname.data=''
            form.secondname.data=''
            form.email.data=''
            form.role.data=''
            form.password.data=''

        # return render_template('register.html', form=form, retrieve=retrieve)
        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route("/get_users", methods=['GET','POST'])
def users():
    persons = get_users()
    return render_template('users.html', persons=persons)


@app.route("/solution/<id>", methods=['GET', 'POST'])
def sol(id):
    form = SolutionForm()
    
    if form.validate_on_submit():
        solution = form.solution.data
        print("=============>id", id)

        info = solution_submission(solution, id )
        
        request_details = get_request(id)


        return redirect("/request/"+id)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)