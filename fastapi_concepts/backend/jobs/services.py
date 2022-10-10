
from sqlalchemy.orm import Session
from jobs import models, schemas


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        title=job.title,
        company=job.company,
        company_url=job.company_url,
        location=job.location,
        description=job.description,
        date_posted=job.date_posted,
        is_active=job.is_active
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_job_by_title(db: Session, title: str):
    return db.query(models.Job).filter(models.Job.title == title).first()


def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()


def get_active_jobs(db: Session):
    return db.query(models.Job).filter(models.Job.is_active == True).all()


def delete_job_by_id(job_id: int, db: Session):
    existing_job = db.query(models.Job).filter(models.Job.id == job_id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return job_id


def update_job_by_id(db: Session, job_id: int, job: schemas.JobUpdate, owner_id: int):
    existing_job = db.query(models.Job).filter(models.Job.id == job_id)
    if not existing_job.first():
        return 0
    # update dictionary with new key value of owner_id
    # job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return job_id
