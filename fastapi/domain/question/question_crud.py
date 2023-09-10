from sqlalchemy.orm import Session
from models import Question,User
from datetime import datetime
from domain.question.question_schema import QuestionCreate


def get_question_list(db:Session, skip: int =0 , limit : int = 10):
    _question_list = db.query(Question).order_by(Question.create_date.desc())
    total = _question_list.count()
    skip = skip * limit
    question_list = _question_list.offset(skip).limit(limit).all()
    return total , question_list

def get_question(db: Session, question_id:int):
    question = db.get(Question, question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(subject=question_create.subject,
                           content=question_create.content,
                           create_date=datetime.now(),
                           user=user)
    db.add(db_question)
    db.commit()