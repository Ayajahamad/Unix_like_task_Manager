from fastapi import FastAPI
from app.api import task_routes
from app.db.session import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI(title="Unix-like Task Manager")
app.include_router(task_routes.router, prefix="")

@app.get("/")
def root():
    return {
        "message": "Welcome to the Unix Task Manager API",
        "routes": {
            "POST": "/tasks/ - Create a new task",
            "GET (all)": "/tasks/ - Get all tasks",
            "GET (by ID)": "/tasks/{id} - Get task by ID",
            "PUT": "/tasks/{id} - Update a task by ID",
            "DELETE (by ID)": "/tasks/{id} - Delete a task by ID",
            "DELETE (all)": "/tasks/ - Delete all tasks",
            "Swagger UI": "http://127.0.0.1:8000/docs"
        }
    }
    
    
    # This line is required if you're running locally
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)