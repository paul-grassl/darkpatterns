from website import db


# model for database structure
class participantData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    trial = db.Column(db.Integer, nullable=False)
    default= db.Column(db.Integer, nullable=False)
    aesthetic = db.Column(db.Integer, nullable=False)
    obstruction = db.Column(db.Integer, nullable=False)
    decision = db.Column(db.Integer, nullable=False)
    privatt = db.Column(db.Integer, nullable=False)
    percontrol = db.Column(db.Integer, nullable=False)
    deliberation = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Participant('{self.id}', '{self.gender}', '{self.nationality}', '{self.age}', '{self.trial}', '{self.default}', '{self.aesthetic}', '{self.obstruction}', '{self.decision}', '{self.privatt}', '{self.percontrol}', '{self.deliberation}')"
