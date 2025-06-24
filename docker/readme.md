# 🐳 hello-docker – Interactive Python App in a Container

## 📌 Overview

This project demonstrates how to containerize a **simple interactive Python script** using a lightweight Docker image. The script takes a user input and greets them — a minimal but effective introduction to containerized user interaction.

---

## 📂 Files Included

```bash
docker/
├── Dockerfile     ← Defines the container behavior
├── hello.py       ← Simple Python input-output script
└── README.md      ← (This file)
````

---

## 🚀 How to Build and Run

### 🧱 Step 1: Build the Docker Image

```bash
docker build -t hello-docker .
```

### ▶️ Step 2: Run the Container

```bash
docker run -it hello-docker
```

* `-it` is required to make `input()` work interactively
* You'll be prompted to enter your name, and it will greet you

---

## ✅ Sample Output

```bash
Enter your Name: Ritik
Hey Ritik, Welcome!! to the Docker journey.
```

---

## 🧠 Learning Highlights

| Concept              | What I Learned                                 |
| -------------------- | ---------------------------------------------- |
| Dockerfile basics    | Writing a minimal container blueprint          |
| Python interactivity | Ensuring `input()` works inside containers     |
| `-it` flag usage     | Required for standard input/output in CLI      |
| Image optimization   | Used `python:3.10-slim` for smaller image size |

