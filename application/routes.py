from flask import render_template, flash, redirect, url_for, abort
from application import app, db
from application.form import UserInputForm
from application.models import IncomeExpenses
from datetime import datetime
import json

@app.route("/")
def index():
    income_vs_expenses = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.type).group_by(
        IncomeExpenses.type).order_by(IncomeExpenses.type).all()

    dates = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.date).group_by(
        IncomeExpenses.date).order_by(IncomeExpenses.date).all()

    income_expense = []
    for total_amount, _ in income_vs_expenses:
        income_expense.append(total_amount)

    over_time_expenditure = []
    dates_labels = []
    for amount, date in dates:
        over_time_expenditure.append(amount)
        dates_labels.append(date.strftime("%m-%d-%Y"))

    return render_template("dashboard.html",
                           income_vs_expenses=json.dumps(income_expense),
                           over_time_expenditure=json.dumps(over_time_expenditure),
                           dates_label=json.dumps(dates_labels))


@app.route("/add", methods=["GET", "POST"])
def add_expenses():
    form = UserInputForm()

    if form.validate_on_submit():
        entry = IncomeExpenses(
            type=form.type.data,
            amount=form.amount.data,
            category=form.category.data,
            date=datetime.now()
        )

        db.session.add(entry)
        db.session.commit()

        flash("Successful Entry", 'success')
        return redirect(url_for('index'))

    return render_template("add.html", title="Add", form=form)

@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Deletion was success", 'success')
    return redirect(url_for("index"))

@app.route('/history')
def history():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template("index.html", title="Index", entries=entries)


