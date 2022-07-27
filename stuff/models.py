from stuff import app, db

class Bin(db.Model):
    __tablename__ = 'content'

    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.Text())
    content = db.Column(db.Text())
    password = db.Column(db.Text())
    hash = db.Column(db.Text())
    time = db.Column(db.String())

    def __init__(self, author, content, password, hash, time):
        self.author = author
        self.content = content
        self.password = password
        self.hash = hash
        self.time = time

    def __repr__(self):
        return '<id {}>'.format(self.id)