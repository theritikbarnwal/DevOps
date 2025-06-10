from flask import Flask, request, render_template, url_for, redirect, session
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Load environment variables
load_dotenv()

# Flask Setup
app = Flask(__name__)
app.secret_key = "supersecretkey"
app.secret_key = os.getenv("FLASK_SECRET_KEY", "defaultsecret")


# MongoDB Setup
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_cluster = os.getenv("MONGO_CLUSTER")
mongo_database = os.getenv("MONGO_DATABASE")
mongo_collection = os.getenv("MONGO_COLLECTION")

uri = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}{mongo_database}?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client[mongo_database]
users_collection = db[mongo_collection]

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)


# Routes
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    category = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if not name or not email or not password:
            message = "All fields are required."
            category = "error"
        else:
            try:
                existing_user = users_collection.find_one({"email": email})
                if existing_user:
                    message = "Email already registered. Please log in."
                    category = "error"
                else:
                    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                    users_collection.insert_one({
                        "name": name,
                        "email": email,
                        "password": hashed_password
                    })
                    return redirect(url_for('welcome'))
            except PyMongoError as e:
                print(f"Register error: {type(e).__name__}: {e}")
                message = "Database error. Please try again later."
                category = "error"
    return render_template('register.html', message=message, category=category)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    category = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            message = "Email and password are required."
            category = "error"
        else:
            try:
                user = users_collection.find_one({"email": email})
                if user:
                    if check_password_hash(user.get('password'), password):
                        session['user'] = email
                        return redirect(url_for('welcome'))
                    else:
                        message = "Invalid email or password."
                        category = "error"
                else:
                    message = "Invalid email or password."
                    category = "error"
            except PyMongoError as e:
                print(f"Login error: {type(e).__name__}: {e}")
                message = "Database error. Please try again later."
                category = "error"
    return render_template('login.html', message=message, category=category)

@app.route('/welcome')
def welcome():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dash.html')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    message = None
    category = None
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            message = "Email is required."
            category = "error"
        else:
            try:
                user = users_collection.find_one({"email": email})
                if user:
                    session['reset_email'] = email
                    return redirect(url_for('reset'))
                else:
                    message = "Email not found."
                    category = "error"
            except PyMongoError as e:
                print(f"Forgot error: {type(e).__name__}: {e}")
                message = "Database error. Please try again later."
                category = "error"
    return render_template('forgot.html', message=message, category=category)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    message = None
    category = None
    if 'reset_email' not in session:
        return redirect(url_for('forgot'))
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        if not new_password:
            message = "New password is required."
            category = "error"
        elif len(new_password) < 6:
            message = "Password must be at least 6 characters."
            category = "error"
        else:
            try:
                hashed_password = generate_password_hash(new_password,  method='pbkdf2:sha256')
                result = users_collection.update_one(
                    {"email": session['reset_email']},
                    {"$set": {"password": hashed_password}}
                )
                if result.modified_count == 0:
                    message = "Failed to update password. Please try again."
                    category = "error"
                else:
                    session.pop('reset_email', None)
                    return redirect(url_for('login'))
            except PyMongoError as e:
                print(f"Reset error: {type(e).__name__}: {e}")
                message = "Database error. Please try again later."
                category = "error"
    return render_template('reset.html', message=message, category=category)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('user_id', None)
    session.pop('reset_email', None)
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(debug=True)    
