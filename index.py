from dataclasses import dataclass
from flask import Flask, jsonify, request
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
        return f'<Player {self.username}>'
    
    def check_password(self,password):
        return self.password == password


@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/signup_menu')
def signup_menu():
    return render_template('signup.html')

@app.route('/login_menu')
def login_menu():
    return render_template('login.html')

@app.route('/game')
def game_tab():
    return '???'

@app.route('/players', methods=['GET'])
def route_get_players():
    return get_players()


@app.route('/players/<player_id>', methods=['GET'])
def route_get_player(player_id):
    return get_player_by_id(player_id)


@app.route('/players/add', methods=['POST'])
def route_add_player():
    player = request.get_json()
    return insert_player(player)


@app.route('/players/update', methods=['PUT'])
def route_update_player():
    player = request.get_json()
    return update_player(player)


@app.route('/players/delete/<player_id>', methods=['GET', 'DELETE'])
def route_delete_player(player_id):
    return delete_player(player_id)


def get_players():
    players = Player.query.all()
    return jsonify(players)


def get_player_by_id(player_id):
    # Player.query.filter_by(id=3).first()
    player = Player.query.get(player_id)
    return jsonify(player)
    # return


def insert_player(data):
    player = Player(firstname=data["firstname"], lastname=data["lastname"])
    db.session.add(player)
    db.session.commit()
    return jsonify(player)


def update_player(player):

    return 'TODO'


def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    return 'Success'