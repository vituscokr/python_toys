from models import  Question, Answer
from datetime import  datetime
from database import SessionLocal

db= SessionLocal();

# questions= db.query(Question).all()
# print(questions);

# questions= db.query(Question).filter(Question.id == 1).all()
# print(questions);

# # question = db.query(Question).get(1) : Legacy use
# question = db.get(Question, 1)
# print(question)

# questions = db.query(Question).filter(Question.subject.like('%FastAPI%')).all()
# print(questions)


## 데이터 수정하기 ##
# question = db.get(Question, 2)
# print(question.id)
#
# question.subject = 'FastAPI Model Question'
# db.commit()


q = db.get(Question, 2)
a = Answer(content="네 자동으로 생성됩니다.",
           create_date=datetime.now(),
           question=q
           )


db.add(a)
db.commit()


