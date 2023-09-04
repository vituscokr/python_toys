from models import  Question, Answer
from datetime import  datetime
from database import SessionLocal

# q= Question(subject='pybo가 무엇인가요',
#             content='pybo에 대해서 알고 싶습니다.',
#             create_date=datetime.now())
#
# db = SessionLocal()
# db.add(q)
# db.commit()

db = SessionLocal()


q= Question(subject='FastAPI 모델 질문입니다.',
            content='id는 자동으로 생성되나요',
            create_date=datetime.now())
db.add(q)
db.commit()

print(q.id)






