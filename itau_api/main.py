from fastapi import FastAPI
from itau_api.api.v1.endpoints import transaction




app = FastAPI()

app.include_router(transaction.router, prefix='/api/v1', tags=['transactions'])




@app.get('/')
def read_root():
    return {'message': 'Server is running!'}
