from app.services.addition_service import process_addition
from app.controllers.addition_controller import add_numbers
from app.models.addition_model import AdditionRequest
from fastapi import HTTPException

def test_process_addition():
    # Test with normal input
    assert process_addition([[3, 1], [4, 5]]) == [4, 9]


    # Test with empty input
    assert process_addition([]) == []

    # Test with input containing empty lists
    assert process_addition([[], []]) == []

    # Test with input containing lists of different lengths
    assert process_addition([[3, 1], [4]]) == [4]

    # Test with negative numbers
    assert process_addition([[-3, 1], [4, -5]]) == [-2, -1]

def test_add_numbers():
    # Test with valid request
    request = AdditionRequest(numbers=[[3, 1], [4, 5]])
    response = add_numbers(request)
    assert response.results == [4, 9]

    # Test with empty request
    request = AdditionRequest(numbers=[])
    try:
        add_numbers(request)
    except HTTPException as e:
        assert e.status_code == 422

    # Test with invalid request format
    request = AdditionRequest(numbers=[3, 1, 4, 5])  # Not a list of lists
    try:
        add_numbers(request)
    except HTTPException as e:
        assert e.status_code == 422
