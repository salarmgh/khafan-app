import os

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

MYSQL_DATABASE_USER = os.getenv('MYSQL_DATABASE_USER', 'root')
MYSQL_DATABASE_DB = os.getenv('MYSQL_DATABASE_DB', 'khafan_app')
MYSQL_DATABASE_PASSWORD = os.getenv(
    'MYSQL_DATABASE_PASSWORD', 'root')
MYSQL_DATABASE_HOST = os.getenv(
    'MYSQL_DATABASE_HOST', '127.0.0.1')
MYSQL_DATABASE_PORT = os.getenv(
    'MYSQL_DATABASE_PORT', '3306')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', f'mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_DATABASE_PORT}/{MYSQL_DATABASE_DB}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


@app.route("/")
def hello_world():
    return jsonify({"status": "ok"})


@app.route('/users', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            if 'name' in data:
                user = User.query.filter_by(name=data['name']).first()

                if user:
                    result = {'status': f'User {data["name"]} already exists'}
                    return jsonify(result), 400
                else:
                    new_user = User()
                    new_user.name = data["name"]
                    db.session.add(new_user)
                    db.session.commit()
                    result = {
                        'status': f'User {data["name"]} successfully created'}
                    return jsonify(result), 200
            else:
                return jsonify({"status": "name is not provided"}), 400
        else:
            return jsonify({"status": "request is not json"}), 400

    if request.method == "GET":
        users = User.query.all()
        user_list = [{'id': user.id, 'name': user.name} for user in users]
        return jsonify(user_list), 200

    return jsonify({"status": "bad request"})


if __name__ == '__main__':
    db.create_all()
    db.init_app(app)
    migrate.init_app(app, db)
    app.run()
