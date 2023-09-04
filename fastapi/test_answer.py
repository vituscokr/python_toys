from models import  Question, Answer
from datetime import  datetime
from database import SessionLocal

db= SessionLocal()


### 답변 입력
# q = db.get(Question, 2)
# a = Answer(content="네 자동으로 생성됩니다.",
#            create_date=datetime.now(),
#            question=q
#            )
#
#
# db.add(a)
# db.commit()

# 답변
a = db.get(Answer, 1)
q = a.question
print(a.question)
print(q.answers)

