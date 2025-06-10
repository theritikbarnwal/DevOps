
```markdown
<h1 align="center">🔐 Flask Login System with MongoDB</h1>
<p align="center">
  A secure and clean authentication system using Flask and MongoDB.
</p>

---

## 🚀 Features

- ✅ User Registration with hashed passwords  
- ✅ Login with session support  
- ✅ Password Reset functionality  
- ✅ MongoDB integration via PyMongo  
- ✅ Environment variable-based secrets  
- ✅ Flask Templates for UI  
- ✅ Clean code structure  

---

## 📁 Project Structure

```

login\_db/
├── app.py
├── templates/
│   ├── landing.html
│   ├── login.html
│   ├── register.html
│   ├── reset.html
│   ├── forgot.html
│   └── welcome.html
├── .env               # Not tracked in Git
├── .gitignore
├── requirements.txt
└── login_db.md

```

---

## 🧪 Tech Stack

- **Flask** – Python web framework  
- **MongoDB** – NoSQL database  
- **PyMongo** – MongoDB connector  
- **Werkzeug** – Password hashing  
- **dotenv** – Load secrets from `.env` file  

---

## 🔐 Environment Variables

Create a `.env` file in the project root with:

```

MONGO\_USERNAME=your\_username
MONGO\_PASSWORD=your\_password
MONGO\_CLUSTER=your\_cluster\_url/
MONGO\_DATABASE=testdb
MONGO\_COLLECTION=users
FLASK\_SECRET\_KEY=your\_super\_secret\_key

````

> ⚠️ **Do NOT commit your `.env` file** – it’s ignored by `.gitignore`.

---

## 📦 Getting Started

1. **Create virtual environment**  
   ```bash
   python -m venv .venv
````

2. **Activate environment**

   * Windows:

     ```bash
     .\.venv\Scripts\activate
     ```
   * macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

---

## 📌 Versioned Dependencies

> 📄 Want pinned package versions? Ask and they’ll be listed here from `pip freeze`.

---

## 🧼 .gitignore Setup

```
# Virtual env
.venv/

# Secrets
.env

# Bytecode
__pycache__/
*.pyc

# Editor settings
.vscode/

# OS files
.DS_Store
Thumbs.db
```

---

## 📜 License

MIT License – free to use, modify, and distribute.

---