from fastapi import FASTAPI, Path

app = FASTAPI()

students = {
  1: {
    "name": "John Doe",
    "age": 20,
    "class": "Year 12"
  }
}

@app.get
def index():
  return {"Message": "Hello World"}

@app.get
def get_student(student_id: int = Path(description="The ID of the student to retrieve")):
  return students[student_id]
