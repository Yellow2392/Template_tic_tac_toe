from dataclasses import dataclass
from flask import Flask, jsonify,  request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@dataclass
class Player(db.Model):
    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    

    def __repr__(self):
        return f'<player {self.username}>'
    def check_password(self,password):
        return self.password == password

    

def test_connection():
    with app.app_context():
        db.create_all()
        player_test = Player(username='john', password='doe')

        db.session.add(player_test)
        db.session.commit()

        students = Player.query.all()

        print(students)
        print(jsonify(students))

test_connection()

