from pydantic import BaseModel, Field
from datetime import datetime

class Transaction(BaseModel):
    value: float = Field(..., description="Transaction amount")
    date: datetime = Field(..., description="Transaction date")


    