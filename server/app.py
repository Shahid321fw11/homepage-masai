from flask_cors import CORS
import flask_bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, session
import re
import secrets

app = Flask(__name__)
app.secret_key = 'masai'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://raj74434:rootroot@raj74434.mysql.pythonanywhere-services.com/raj74434$user1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


class Users(db.Model):
    __tablename__="user2"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(20), unique=True)
    referral_code = db.Column(db.String(20))
    password = db.Column(db.String(128))
    token = db.Column(db.String(32))

    def __init__(self, full_name, email, phone_number, referral_code, password):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.referral_code = referral_code
        self.password = password
        self.token = None


def init_db():
    with app.app_context():
        db.create_all()


@app.route('/', methods=['GET'])
def home():
    return "hello welcome to masai homepage"


@app.route('/signUp', methods=['POST'])
def signUp():
    if request.method == 'POST':
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        referral_code = data.get('referral_code')
        password = data.get('password')

        if not (email and phone_number) or not password:
            return jsonify({"error": "Email/Phone and password are required"}), 400

        if email and not validate_email_format(email):
            return jsonify({"error": "Invalid email format"}), 400
        if phone_number and not validate_phone_number_format(phone_number):
            return jsonify({"error": "Invalid phone number format"}), 400

        user = Users.query.filter((Users.email == email) | (Users.phone_number == phone_number)).first()
        if user:
            return jsonify({"error": "Email/Phone already exists"}), 400

        hashed_password = flask_bcrypt.generate_password_hash(
            data['password']).decode('utf-8')

        new_user = Users(full_name=full_name, email=email, phone_number=phone_number, referral_code=referral_code,
                         password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "Registration successful",
            }), 201


@app.route('/signIn', methods=['POST'])
def signIn():
    identifier = request.json.get('identifier')
    password = request.json.get('password')

    user = Users.query.filter((Users.email == identifier) | (Users.phone_number == identifier)).first()

    if user and flask_bcrypt.check_password_hash(user.password, password):
        token = secrets.token_hex(16)
        user.token = token
        db.session.commit()
        return jsonify({"message": "Login successful",
                        "email" : user.email,
                        "full_name" : user.full_name,
                        "phone_number" : user.phone_number,
                        }), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/signOut', methods=['POST'])
def signOut():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Token is missing"}), 401

    user = Users.query.filter_by(token=token).first()
    if user:
        user.token = None
        db.session.commit()
        return jsonify({"message": "Logout successful"}), 200
    else:
        return jsonify({"error": "Invalid token"}), 401



def validate_phone_number_format(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if len(cleaned_number) == 10:
        return True
    else:
        return False
    
def validate_email_format(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+'
    if re.match(email_pattern, email):
        return True
    else:
        return False



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
