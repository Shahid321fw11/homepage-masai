import flask_bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import re
import secrets
# from flask_cors import CORS
import random
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'masai'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


app.config["MAIL_SERVER"]='smtp.office365.com'
app.config["MAIL_PORT"]="587"
app.config["MAIL_USERNAME"]=""  # enter your outlook email
app.config["MAIL_PASSWORD"]="" # enter here password of thta email
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False
mail=Mail(app)


# CORS(app)   # here we allowed cors so that client can contact to our server


class Users(db.Model):
    __tablename__="user1"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(20), unique=True)
    referral_code = db.Column(db.String(20))
    token = db.Column(db.String(32))

    def __init__(self, full_name, email, phone_number, referral_code):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.referral_code = referral_code
        self.token = None


def init_db():
    with app.app_context():
        db.create_all()



@app.route('/', methods=['GET'])
def home():
    return "hello"


@app.route('/signupverify', methods=['POST'])
def verify():
     if request.method == 'POST':
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        referral_code = data.get('referral_code')

        if not (email and phone_number) or not full_name:   # added here
            return jsonify({"error": "Email/Phone and password are required"}), 400

        if email and not validate_email_format(email):
            return jsonify({"error": "Invalid email format"}), 400
        if phone_number and not validate_phone_number_format(phone_number):
            return jsonify({"error": "Invalid phone number format"}), 400

        user = Users.query.filter((Users.email == email) | (Users.phone_number == phone_number)).first()
        if user:
            return jsonify({"error": "Email/Phone already exists"}), 400

        try:
         global signupOtp
         signupOtp=random.randint(100000,999999)
         signupOtp=str(signupOtp)
         msg=Message("Email verification",sender='EnterYourEmailHere@outlook.com',recipients=[email])
         msg.body="Hello "+full_name +" \n Verification OTP :- "+str(signupOtp)
         mail.send(msg)
         return jsonify({"success": "OTP sent"}), 200
        
        except Exception as e:
         print("An error occurred while sending the email:", str(e))
         return ({"message": "OTP veryfication faild", }), 400




@app.route('/signUp', methods=['POST'])
def signUp():
    if request.method == 'POST':
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        referral_code = data.get('referral_code')
        recivedOtp=data.get("otp")

        if not (email and phone_number) :
            return jsonify({"error": "Email/Phone and password are required"}), 400

        if email and not validate_email_format(email):
            return jsonify({"error": "Invalid email format"}), 400
        if phone_number and not validate_phone_number_format(phone_number):
            return jsonify({"error": "Invalid phone number format"}), 400

        user = Users.query.filter((Users.email == email) | (Users.phone_number == phone_number)).first()
        if user:
            return jsonify({"error": "Email/Phone already exists"}), 400
        

        if recivedOtp != signupOtp:
          return jsonify({"error": "Wrong OTP"}), 400

        hashed_password = flask_bcrypt.generate_password_hash(
            data['password']).decode('utf-8')

        new_user = Users(full_name=full_name, email=email, phone_number=phone_number, referral_code=referral_code,
                         password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "Registration successful",

            }), 201


@app.route('/signinverify', methods=['POST'])
def signinVerify():
    email = request.json.get('email')

    user = Users.query.filter((Users.email == email) | (Users.phone_number == email)).first()

    if user :
        try:
          global signinOtpcreated
          signinOtpcreated=random.randint(100000,999999)
          signinOtpcreated=str(signinOtpcreated)
          msg=Message("Email verification",sender='masaiTest@outlook.com',recipients=[user.email])
          msg.body="Hello "+user.full_name +" \n Verification OTP :- "+str(signinOtpcreated)
          mail.send(msg)
          return jsonify({"success": "OTP sent"}), 200
        
        except Exception as e:
          print("An error occurred while sending the email:", str(e))
          return ({"message": "OTP veryfication faild", }), 400

    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/signIn', methods=['POST'])
def signIn():
    email = request.json.get('email')
    signinOtp = request.json.get('otp')

    user = Users.query.filter((Users.email == email) | (Users.phone_number == email)).first()

    if user:

        if signinOtp != signinOtpcreated:
          return jsonify({"error": "Wrong OTP"}), 400

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


def validate_email_format(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+'
    if re.match(email_pattern, email):
        return True
    else:
        return False


def validate_phone_number_format(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if len(cleaned_number) == 10:
        return True
    else:
        return False


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
