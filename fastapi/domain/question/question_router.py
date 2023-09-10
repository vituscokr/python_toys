from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session

from domain.question import question_schema, question_crud
from starlette import status
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix="/api/question",
)

@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db), page: int=0, size: int=10):
    total, _question_list = question_crud.get_question_list(db, skip=page, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }

@router.get("/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    _question = question_crud.get_question(db, question_id=question_id)
    return _question

@router.post("",status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create:question_schema.QuestionCreate,
                    db: Session= Depends(get_db),
                    current_user: User= Depends(get_current_user)):
    question_crud.create_question(db=db, question_create=_question_create, user=current_user)



@router.put("",status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update:question_schema.QuestionUpdate,
                    db: Session= Depends(get_db),
                    current_user: User= Depends(get_current_user)):
    db_question = question_crud.get_question(db, question_id=_question_update.question_id)
    if not db_question:
        raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    question_crud.update_question(db=db,
                                  question= db_question,
                                  question_update=_question_update)


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(_question_delete: question_schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db,question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    question_crud.delete_question(db=db ,
                                  question=db_question)