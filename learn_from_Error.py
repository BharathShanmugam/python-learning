from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)
user_router = APIRouter()

@user_router.post("/users", response_model=ViewUser)
async def create_new_user(request: Request, user_data: CreateUser, session: Session = Depends(get_db)):
    # Log the raw request body
    body = await request.json()  # Read the JSON body
    logger.info(f"Incoming user data: {body}")

    try:
        return user_service.create_user(user_data, session)
    except RequestValidationError as e:
        logger.error(f"Validation error for user data: {body}")
        logger.error(f"Error details: {e.errors()}")
        raise HTTPException(status_code=422, detail="Validation Error", headers=e.headers)
    except HTTPException as e:
        logger.error(f"Error creating user: {str(e.detail)}")
        raise e
