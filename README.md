# FastAPI Items CRUD API

A simple REST API built using **FastAPI** that performs CRUD (Create, Read, Update, Delete) operations on items. This project is ideal for learning FastAPI fundamentals, API design and backend development.

---

## 🚀 Features

- Create new items
- Get all items
- Get item by ID
- Update existing items
- Delete items
- Auto-generated API docs (Swagger UI)

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## 📁 Project Structure

```

FASTAPI-ITEMS-CRUD/
│
├── __pycache__/              # Python cache files (auto-generated)
│
├── models/
│   ├── __pycache__/
│   ├── __init__.py
│   └── item.py              # Database or ORM models
│
├── routers/
│   ├── __pycache__/
│   ├── __init__.py
│   └── item.py             # API routes (CRUD endpoints)
│
├── schemas/
│   ├── __pycache__/
│   ├── __init__.py
│   └── item.py             # Pydantic schemas (request/response models)
│
├── venv/                    # Virtual environment 
│
├── database.py             # Database connection / in-memory DB
├── main.py                 # FastAPI app entry point
├── README.md               # Project documentation
├── requirements.txt       # Dependencies list
└── test.db                # SQLite database file (if using SQLite)


## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ChadubulaVani/fastapi-items-crud.git
cd fastapi-items-crud
````

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically generates interactive docs:

* Swagger UI:
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* ReDoc:
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Example Endpoints

### Create Item

```
POST /items
```

### Get All Items

```
GET /items
```

### Get Item by ID

```
GET /items/{item_id}
```

### Update Item

```
PUT /items/{item_id}
```

### Delete Item

```
DELETE /items/{item_id}
```

---

## 🧠 Learning Goals

This project helps you understand:

* FastAPI routing
* Request & response models (Pydantic)
* CRUD operations
* API testing using Swagger UI




