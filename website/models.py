from website import db


# models for database structure (each one represents a questionnaire)
class demographicData(db.Model):
    __tablename__ = 'demographic_data'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    # create relationships to the other models to link them to the demographicData
    questionnaire1 = db.relationship('controlAndDeliberationData', backref='participant', lazy=True)
    questionnaire2 = db.relationship('privacyConcernsData', backref='participant', lazy=True)

    def __repr__(self):
        return f"demographicData('{self.id}', '{self.gender}', '{self.age}', '{self.nationality}')"


class controlAndDeliberationData(db.Model):
    __tablename__ = 'control_and_deliberation_data'
    id = db.Column(db.Integer, primary_key=True)
    participantId = db.Column(db.Integer, db.ForeignKey('demographic_data.id'), nullable=False)
    perceivedControlQ1 = db.Column(db.Integer, nullable=False)
    perceivedControlQ2 = db.Column(db.Integer, nullable=False)
    perceivedControlQ3 = db.Column(db.Integer, nullable=False)
    perceivedControlQ4 = db.Column(db.Integer, nullable=False)
    perceivedControlQ5 = db.Column(db.Integer, nullable=False)
    manipulationCheck = db.Column(db.String(3), nullable=False)
    deliberation = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"controlAndDeliberationData('{self.participantId}', '{self.perceivedControlQ1}', '{self.perceivedControlQ2}', '{self.perceivedControlQ3}', '{self.perceivedControlQ4}', '{self.perceivedControlQ5}', '{self.manipulationCheck}', '{self.deliberation}')"


class privacyConcernsData(db.Model):
    __tablename__ = 'privacy_concerns_data'
    id = db.Column(db.Integer, primary_key=True)
    participantId = db.Column(db.Integer, db.ForeignKey('demographic_data.id'), nullable=False)
    privacyConcernsQ1 = db.Column(db.String(1), nullable=False)
    privacyConcernsQ2 = db.Column(db.String(1), nullable=False)
    privacyConcernsQ3 = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f"privacyConcernsData('{self.participantId}', '{self.privacyConcernsQ1}', '{self.privacyConcernsQ2}', '{self.privacyConcernsQ3}')"