from datetime import datetime, timezone

from fastapi import APIRouter, status
from fastapi.responses import Response

from itau_api.api.v1.schemas.transaction import Transaction

router = APIRouter()


@router.post('/transacao', status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction: Transaction):
    if transaction.value < 0:
        return Response(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    now = datetime.now(timezone.utc)
    if transaction.date > now:
        return Response(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    return Response(status_code=status.HTTP_201_CREATED)


@router.delete('/transacao/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction():
    """
    Delete a transaction.
    """

    return {'message': 'Todas as informações foram apagadas com sucesso'}
