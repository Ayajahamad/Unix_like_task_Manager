# 🧰 Unix-like Task Manager API

A simple and interactive **Unix-inspired Task Manager** REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, following a clean and scalable architecture using routers, schemas, models, and CRUD logic. This project demonstrates good practices like `.env` configuration, database session management, and modular code structure.

## 📂 Project Structure

unix_like_task_manager/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── task_model.py
│   ├── schemas/
│   │   └── task_schema.py
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   ├── crud/
│   │   └── task_crud.py
│   ├── api/
│   │   └── task_routes.py
│   ├── core/
│   │   └── config.py
│
├── .env
├── requirements.txt
└── README.md
<<<<<<< HEAD
|-- venv
=======
>>>>>>> b37e4bdbc85bfb096f43172db9f9144e61bdf9bf


## 🔧 Features

- ✅ Create new tasks
- 📖 Read all tasks or by ID
- 🔄 Update task details
- ❌ Delete task by ID
- 🧹 Delete **all** tasks (bulk delete)
- 🧾 Full Swagger docs at `/docs`
- 📬 `.env` support for secure config handling

## 🚀 Tech Stack

- **FastAPI** – Fast web framework for APIs
- **SQLAlchemy** – ORM for DB communication
- **PostgreSQL** – Relational DB
- **Pydantic** – Data validation & serialization
- **dotenv** – Manage environment variables

-----------------------------------------------------------------

## 🛠️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Ayajahamad/Unix_like_task_Manager.git
cd unix_like_task_manager
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Linux/macOS
venv\Scripts\activate          # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` File

Update the `.env` file with your DB credentials:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=unix_task_db
DATABASE_USER=User_Name
DATABASE_PASSWORD=Your_Password

OR

DATABASE_URL=postgresql://postgres:Password@localhost:5432/unix_task_db
```

### 5. Create the Database

Make sure the database `unix_task_db` exists in PostgreSQL. You can create it using:

```sql
CREATE DATABASE unix_task_db;
```

## 🧪 Run the Project

```bash
uvicorn app.main:app --reload 

chenge the port if want ** --port 1000 **
```

- Visit API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative Docs (ReDoc): [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧾 API Endpoints Summary

| Method | Endpoint            | Description             |
|--------|---------------------|-------------------------|
| POST   | `/tasks/`           | Create a new task       |
| GET    | `/tasks/`           | Get all tasks           |
| GET    | `/tasks/{id}`       | Get task by ID          |
| PUT    | `/tasks/{id}`       | Update a task by ID     |
| DELETE | `/tasks/{id}`       | Delete a task by ID     |
| DELETE | `/tasks/`           | Delete **all** tasks    |
|--------------------------------------------------------|
|For Swagger | `/docs`         | Provide Swagger UI      |
|--------------------------------------------------------|

## 💬 Example Task JSON

```json
{
  "title": "Complete Unix-like Manager",
  "description": "Build the task manager using FastAPI and PostgreSQL"
}
```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.


## ✨ Acknowledgements

Special thanks to:
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)


## 👨‍💻 Built with ❤️ by Ayaj Ahamad

- GitHub: [@Ayajahamad](https://github.com/Ayajahamad)
- LinkedIn: [Ayaj Ahamad](https://linkedin.com/in/ayaj-ahamad-732153229/)
