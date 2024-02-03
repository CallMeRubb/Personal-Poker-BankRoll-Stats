from application import db
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    game_type = db.Column(db.String(50), nullable=False)
    buy_in = db.Column(db.Integer, nullable=False)
    total_pot = db.Column(db.Integer, nullable=False)
    earnings = db.Column(db.Integer, nullable=True)  # New column for earnings

    def __str__(self):
        return str(self.id)
