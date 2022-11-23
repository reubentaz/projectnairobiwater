from webbrowser import get
from flask import Blueprint, render_template
from models.model_functions import get_request, get_solutions, solution_submission
from models.myforms import SolutionForm

my_req = Blueprint("requests", __name__)

@my_req.get("/request/<id>")
def display(id):
    # slugg = slugg.replace()

    form = SolutionForm()

    sol = get_solutions(id)

    request_details = get_request(id)
    form.request.data = id

    if request_details:
        return render_template("request_page.html", request_details=request_details, form=form, id=id, sol=sol)
    return render_template("404.html")
