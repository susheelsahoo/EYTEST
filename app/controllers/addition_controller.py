from fastapi import APIRouter, HTTPException
from app.models.addition_model import AdditionRequest, AdditionResponse
from app.services.addition_service import process_addition
from app.utils.logger import logger
from datetime import datetime

router = APIRouter()


@router.post("/add")
async def add_numbers(addition_request: AdditionRequest):
    try:
        logger.info("Received request: %s", addition_request.json())
        start_time = datetime.now()  # Record start time
        result = process_addition(addition_request.payload)
        end_time = datetime.now()  # Record end time
        duration = end_time - start_time
        logger.info("Computed result: %s", result)
        logger.info("Time taken: %s seconds", duration.total_seconds())
        response_data = {
            "batch_id": addition_request.batch_id,
            "response": result,
            "status": "complete",
            "started_at": start_time.isoformat(),
            "completed_at": end_time.isoformat()
        }
        return response_data
    except Exception as e:
        logger.error("Error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))
