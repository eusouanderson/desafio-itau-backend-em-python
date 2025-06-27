from fastapi import APIRouter, Depends, status,  HTTPException
from itau_api.api.v1.schemas.transaction import Transaction

router = APIRouter()


@router.post("/transacao", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction: Transaction):
    """
    Create a new transaction.
    """
    # Here you would typically save the transaction to a database
    # For now, we will just return the transaction as is
    return transaction