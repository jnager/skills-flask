from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show the homepage."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def application_form_page():
    """Gathers info from applicant"""

    return render_template("application-form.html")


@app.route("/application-response", methods=["POST", "GET"])
def application_response_page():
    """Thanks user for their application."""

    # Handles POST method, which should be the most common scenario.
    if request.method == "POST":
        fname = request.form.get("firstname")
        lname = request.form.get("lastname")
        role = request.form.get("role")
        salary = int(request.form.get("salary"))

        return render_template("application-response.html",
                               firstname=fname,
                               lastname=lname,
                               role=role,
                               salaryreq=salary)
    # Handles GET method and redirects to application form page.
    # Mostly handling the scenario where someone tries to load page directly.
    else:
        return redirect("/application-form")


if __name__ == "__main__":
    app.run(debug=True)
