# 🚀 Task Manager API

A RESTful API built with Flask for managing tasks with secure JWT authentication.

---

## ✨ Features

* 🔐 JWT Authentication (Register / Login)
* 📋 Full CRUD for Tasks
* 📄 Pagination support
* 🔒 Password hashing
* 🧱 Clean and scalable project structure

---

## 🛠 Tech Stack

* Python / Flask
* Flask-SQLAlchemy
* PostgreSQL
* JWT

---

## ⚡ Quick Start

```bash
git clone https://github.com/saifelsayed846-gif/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt
python app.py
```

---

## 🔑 Authentication

```
Authorization: Bearer <your_token>
```

---

## 📌 API Overview

| Method | Endpoint   | Description       |
| ------ | ---------- | ----------------- |
| POST   | /register  | Create user       |
| POST   | /login     | Login & get token |
| GET    | /task      | Get tasks         |
| POST   | /task      | Create task       |
| PUT    | /task/<id> | Update task       |
| DELETE | /task/<id> | Delete task       |

---

## 📊 Example Response

```json
{
  "success": true,
  "tasks": [
    {
      "id": 1,
      "task": "Learn Flask",
      "status": "pending"
    }
  ]
}
```

---

## 🌍 Live Demo

> Coming soon (deployed on Railway)

---

## 📈 Future Improvements

* Role-based authorization
* Swagger API Docs
* Docker support

---

## 👨‍💻 Author

**Saif Elsayed**

---

## ⭐ Final Note

This project demonstrates building a real-world backend API with authentication, clean architecture, and scalable design.
