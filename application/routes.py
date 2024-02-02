from flask import render_template, flash, redirect, url_for
from application import app, db
from application.form import UserInputForm
from application.models import IncomeExpenses
from datetime import datetime  # Import the datetime module

@app.route("/")
def index():
    return render_template("index.html", title="Index")

@app.route("/add", methods=["GET", "POST"])
def add_expenses():
    form = UserInputForm()

    if form.validate_on_submit():
        # Assuming 'date' is a column in your IncomeExpenses model
        entry = IncomeExpenses(
            type=form.type.data,
            amount=form.amount.data,
            category=form.category.data,
            date=datetime.now().strftime("%Y-%m-%d")  # Set the current date and time
        )

        db.session.add(entry)
        db.session.commit()

        flash("Successful Entry", 'success')
        return redirect(url_for('index'))

    return render_template("add.html", title="Add", form=form)
