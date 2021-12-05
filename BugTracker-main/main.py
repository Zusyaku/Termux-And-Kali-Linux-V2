from flask import render_template, redirect, url_for, request, flash
from config import app
from models import db, bug_report
from sendmail import ReporterSendMail, AdminSendMail


@app.route('/')
def index():
    return render_template('index.html')


# Form proccessing
@app.route('/formproc', methods=["POST", "GET"])
def form_proc():
    # Checks if the request is a GET one and redirects back to index because the user isn't supposed to be here and to avoid the error message too
    if request.method == "GET":
        return redirect(url_for('index'))
    r = request.form
    # Gets data from the forms in the html page
    name = r.get('name')
    email = r.get('email')
    phone = r.get('phone')
    system = r.get('system')
    severity = r.get('severity')
    steps = r.get('steps')
    msg = r.get('message')
    # Adds the data to the database
    data = bug_report(name, email, phone, system,
                      severity, steps, msg)
    db.session.add(data)
    db.session.commit()
    # Sends the email to the reporter's email address
    ReporterSendMail(email, system, severity, steps, msg)
    # Sends the email to the reporter's email address
    AdminSendMail(system, severity, steps, msg)
    # Notifies the user on the page that their report has been sent with no problems
    flash('Your report has been sent successfully.')
    # finally redirects back to index
    return redirect(url_for('index'))


if __name__ == "__main__":
    # Creating the database tables if needed then running the app
    db.create_all()
    app.run(debug=True)
