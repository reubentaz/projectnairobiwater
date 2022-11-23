from flask import Blueprint, render_template
from models.model_functions import get_request

my_req = Blueprint("requests", __name__)

@my_req.get("/request/<id>")
def display(id):
    # slugg = slugg.replace()
    request_details = get_request(id)

    if request_details:
        return render_template("request_page.html", request_details=request_details)
    return render_template("404.html")
