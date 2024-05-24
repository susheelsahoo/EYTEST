#### Pip

If you prefer using `pip`, you can create a virtual environment and then install the dependencies using the following command:

```shell
$ pip install -r requirements.txt
```

## How To Run the Server

To run the server, use the following command:

```shell
$ uvicorn app.main:app --host localhost --port 8000 --reload
```

This will spin up the server at `http://localhost:8000` with a local SQLite database `users.db`.

## API Endpoints

### Create User

- `POST /api/users/`: Create a new user.

To create a user, send a POST request to `http://localhost:8000/api/app/multiprocessing` with the following JSON payload:

```json
{
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
   
}
```

As we use Pydantic models, the API will validate the request payload and return an error if the payload is invalid.


## How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```shell
$ pytest 
```

This will spin up a test database in SQLite `test_db.db`, run the tests and then tear down the database. 

You can use `pytest -v` for verbose output and `pytest -s` to disable output capture for better debugging.