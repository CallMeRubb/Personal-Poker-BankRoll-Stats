from application import db
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    amount = db.Column(db.Float, nullable=False)

    def __str__(self):
        return str(self.id)
