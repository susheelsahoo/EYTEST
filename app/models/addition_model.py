from pydantic import BaseModel
from typing import List

class AdditionRequest(BaseModel):
    numbers: List[List[int]]

class AdditionResponse(BaseModel):
    results: List[int]
