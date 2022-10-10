from sqlalchemy.orm import Session
from users import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=user.password,
        is_superuser=user.is_superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()



def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def delete_user(db: Session, user_id: int):

    existing_user = db.query(models.User).filter(
        models.User.id == user_id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return user_id


def update_user_by_id(db: Session, user_id: int, user: schemas.UserUpdate):

    existing_user = db.query(models.User).filter(
        models.User.id == user_id)
    if not existing_user.first():
        return 0
    existing_user.update(user.__dict__)
    db.commit()
    return user_id
