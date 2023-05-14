from fastapi import FastAPI

app = FastAPI(title='twitter-clone')


@app.get('/api/users/me')
def foo():
    return {
        "result": "true",
        "user": {
            "id": 111,
            "name": "Maks",
            "followers": [
                {
                    "id": 333,
                    "name": "Albert"
                }
            ],
            "following": [
                {
                    "id": 222,
                    "name": "Sasha"
                }
            ]
        }
    }
