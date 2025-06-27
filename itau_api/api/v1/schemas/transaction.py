from datetime import datetime

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    value: float = Field(..., description='Transaction amount')
    date: datetime = Field(..., description='Transaction date')
