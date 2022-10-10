from fastapi import APIRouter, Depends, HTTPException, Query, status
from users import schemas
from users import services as S
from sqlalchemy.orm import Session
from db.dependencies import get_db
from pydantic import Required


router = APIRouter()


@router.post("/", response_model=schemas.User, status_code=200)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> dict:
    db_user = S.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return S.create_user(db=db, user=user)

# token: str = Depends(oauth2_scheme)


@router.get("/", response_model=list[schemas.ShowUser], status_code=200)
def fetch_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> list:
    users = S.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.ShowUser, status_code=200)
def fetch_user(
    user_id: int | None = Query(default=Required, include_in_schema=False),
    db: Session = Depends(get_db)
) -> dict:
    db_user = S.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="User with ID {user_id} not found")
    return db_user


@router.delete("/{user_id}", status_code=200)
def delete_user(
    db: Session = Depends(get_db),
    user_id: int | None = Query(default=Required, include_in_schema=False)
) -> dict:
    db_user = S.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="User with ID {user_id} not found")
    return {"msg": f"User id {db_user} Successfully deleted!"}


@router.put("/{user_id}", status_code=200)
def update_user(
    user: schemas.UserUpdate,
    user_id: int | None = Query(default=Required, include_in_schema=False),
    db: Session = Depends(get_db)
) -> dict:
    db_user = S.update_user_by_id(
        db=db, user=user, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {user_id} not found")
    return {"msg": f"Job id {db_user} Successfully updated!"}
