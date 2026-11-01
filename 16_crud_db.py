from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI , Depends , HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test1.db"

engine = create_engine(DATABASE_URL ,
         connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db   # return db and pause till route finish the job
    finally:
        db.close()


#create API
@app.post("/todos")
def create_todo(title: str, db:Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)  
    db.commit()
    db.refresh(todo)
    return {
        "message":"todo created successfully",
        "data":todo
    }

#Read API
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "total":len(todos),
        "data":todos
    }

#Read based on ID API
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,
                         detail="todo not found")
    return {
        "data":todo
    }

#update API
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title:str, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,
                         detail="todo not found")
    
    todo.title = title
    
    db.commit()
    db.refresh(todo)
    
    return {
        "message":"todo updated successfully",
        "data":todo
    }


#Delete API
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,
                         detail="todo not found")
    
    db.delete(todo)
    db.commit()
    
    return {
        "message":"todo deleted successfully" ,
        "data":todo
    }