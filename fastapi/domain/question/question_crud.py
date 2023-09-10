from sqlalchemy.orm import Session
from models import Question,User
from datetime import datetime
from domain.question.question_schema import QuestionCreate, QuestionUpdate


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

def update_question(db: Session,
                    question: Question,
                    question_update: QuestionUpdate,
                    ):
    question.subject = question_update.subject
    question.content = question_update.content
    question.modify_date = datetime.now()
    db.add(question)
    db.commit()

def delete_question(db: Session,
                    question: Question):
    db.delete(question)
    db.commit()

def vote_question(db: Session, db_question: Question, db_user: User):
    db_question.voter.append(db_user)
    db.commit()