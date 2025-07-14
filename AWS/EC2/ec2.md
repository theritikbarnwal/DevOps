```markdown
# 🌐 EC2-Hosted Flask App – User Auth Prototype

This is a simple, secure **Flask-based user authentication system** hosted on an **Amazon Linux EC2 instance**. It supports registration, login, session-based access control, and MongoDB integration for credential storage.

---

## 🚀 Features

- 🔐 **User Registration & Login**
- 📂 **Dashboard access** restricted to logged-in users only
- 🔄 **Session Management** with Flask
- 🧠 **MongoDB Integration** for storing user credentials
- 🔒 Passwords are **securely hashed using bcrypt**
- 🛠️ Manually deployed to **Amazon Linux EC2 instance**
- 📡 Access via public IP: `http://<EC2-Public-IP>`

---

## 🛠️ Technologies Used

| Tech         | Purpose                                  |
|--------------|------------------------------------------|
| **Flask**    | Web framework (Python)                   |
| **MongoDB**  | NoSQL database for user data             |
| **Bcrypt**   | Secure password hashing                  |
| **EC2**      | Cloud instance hosting (Amazon Linux 2)  |
| **Git**      | Repo cloning into EC2                    |
| **Python3**  | Runtime for Flask                        |

---

## 📦 Project Structure

```

project-root/
├── app.py                  # Main Flask app
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/
│   └── (optional assets)
├── requirements.txt
└── .env                   # MongoDB URI, Secret Key

````

---

## 📂 How to Deploy on EC2

### 1. Launch EC2 (Amazon Linux 2)
- Configure security group to allow ports:
  - `22` (SSH)
  - `5000` (Flask app)
  - `80` (optional for future Nginx or Apache)
  
### 2. SSH into Instance

```bash
ssh -i your-key.pem ec2-user@<EC2-PUBLIC-IP>
````

### 3. Install Dependencies

```bash
sudo yum update -y
sudo yum install git python3 -y
pip3 install flask pymongo bcrypt python-dotenv
```

### 4. Clone GitHub Repo

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 5. Add `.env` File

```env
MONGO_URI=mongodb+srv://your-mongodb-uri
SECRET_KEY=your-flask-secret-key
```

### 6. Run Flask App

```bash
sudo python3 app.py
```

Or for port 5000:

```bash
python3 app.py
```

Make sure `app.py` has:

```python
app.run(host="0.0.0.0", port=5000)
```

Then access it at:

```
http://<EC2-PUBLIC-IP>:5000
```

---

## 🔐 Security Note

* All user passwords are **hashed using bcrypt** before storing in MongoDB.
* No real user data or sensitive actions are present — this is a **prototype** only.

---

## 📈 Future Plans

* 🔄 Automate EC2 deployment using GitHub webhooks or CI/CD
* 📦 Add Docker for container-based deployment
* 🧪 Write tests and automate builds
* 🌍 Map custom domain to EC2 instance
* ⚙️ Add production-ready features (rate limiting, HTTPS, error logging)

---