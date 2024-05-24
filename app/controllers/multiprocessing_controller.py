from fastapi import FastAPI
from pydantic import BaseModel
from multiprocessing import Pool
from datetime import datetime

class InputData(BaseModel):
    batchid: str
    payload: list[list[int]]

class OutputData(BaseModel):
    batchid: str
    response: list[int]
    status: str
    started_at: str
    completed_at: str


app = FastAPI()

@app.post("/addition/", response_model=OutputData)
def perform_addition(data: InputData):
    print("Received payload:", data.payload)
    try:
        started_at = datetime.now().isoformat()
        print("Received payload:", data.payload)
        # Define the function to perform addition on a single list
        def add_list(lst):
            return sum(lst)

        # Create a multiprocessing pool
        with Pool() as pool:
            # Perform addition on each inner list in parallel
            results = pool.map(add_list, data.payload)

        completed_at = datetime.now().isoformat()

        return {
            "batchid": data.batchid,
            "response": results,
            "status": "complete",
            "started_at": started_at,
            "completed_at": completed_at
        }

    except Exception as e:
        return {
            "batchid": data.batchid,
            "response": [],
            "status": "errorr",
            "started_at": started_at,
            "completed_at": datetime.now().isoformat()
            
        }
