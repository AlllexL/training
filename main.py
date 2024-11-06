import uvicorn
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
def hello_index():
    return {
        'message': 'Hello index!'
    }


@app.post('/users')
def create_user(user: CreateUser):
    return {
        'message': 'success',
        'email': user.email
    }


@app.get('/items')
def list_items():
    return [
        'item1',
        'item2'
    ]

@app.get('/item/latest')
def get_latest_id():
    return {
        'id': 0,
        'name': 'latest'
    }


@app.get('/item/{item_id}')
def get_item_id(item_id: int):
    return {
        'item':{
            'id': item_id
        },
    }


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=True
    )