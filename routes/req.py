from flask import Blueprint, render_template
from models.model_functions import get_request
from models.myforms import SolutionForm

my_req = Blueprint("requests", __name__)

@my_req.get("/request/<id>")
def display(id):
    # slugg = slugg.replace()

    form = SolutionForm()

    request_details = get_request(id)
    form.request.data = id

    if form.validate_on_submit():
        solution = form.solution.data

        pass


    if request_details:
        return render_template("request_page.html", request_details=request_details, form=form, id=id)
    return render_template("404.html")
