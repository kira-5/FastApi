from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session
from db.dependencies import get_db
from pydantic import Required
from jobs import schemas
from jobs import services as S

router = APIRouter()


@router.post("/", response_model=schemas.Job, status_code=200)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)) -> dict:
    if db_user := S.get_job_by_title(db, title=job.title):
        raise HTTPException(
            status_code=400, detail="Job Title already registered")
    return S.create_job(db=db, job=job)


@router.get("/", response_model=list[schemas.Job], status_code=200)
def fetch_jobs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> list:
    return S.get_jobs(db, skip=skip, limit=limit)


@router.get("/{job_id}", response_model=schemas.Job, status_code=200)
def fetch_job(
    job_id: int | None = Query(default=Required, include_in_schema=False),
    db: Session = Depends(get_db)
) -> dict:
    db_job = S.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(
            status_code=404, detail="job with ID {job_id} not found")
    return db_job


@router.get("/active/", response_model=list[schemas.Job], status_code=200)
def fetch_active_jobs(
    db: Session = Depends(get_db)
) -> list:
    return S.get_active_jobs(db)


@router.delete("/{job_id}", status_code=200)
def delete_job(
    job_id: int | None = Query(default=Required, include_in_schema=False),
    db: Session = Depends(get_db)
) -> dict:
    if db_job := S.delete_job_by_id(job_id=job_id, db=db):
        return {"msg": f"Job id {db_job} Successfully deleted."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {job_id} not found")



@router.put("/{job_id}", status_code=200)
def update_job(
    job: schemas.JobUpdate,
    job_id: int | None = Query(default=Required, include_in_schema=False),
    db: Session = Depends(get_db)
) -> dict:
    current_user = 1
    if db_job := S.update_job_by_id(
        db=db, job=job, job_id=job_id, owner_id=current_user
    ):
        return {"msg": f"Job id {db_job} Successfully updated!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {job_id} not found")
