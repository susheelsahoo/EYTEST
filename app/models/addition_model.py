from pydantic import BaseModel
from typing import List

class AdditionRequest(BaseModel):
    batch_id: str
    payload: List[List[int]]
    
class AdditionResponse(BaseModel):
    results: List[int]
