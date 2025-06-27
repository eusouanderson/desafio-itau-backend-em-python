from datetime import datetime
from threading import Lock
from typing import List

from itau_api.domain.entities.transaction import Transaction


class TransactionMemRepo:
    def __init__(self):
        self._transactions: List[Transaction] = []
        self._lock = Lock()

    def add(self, transaction: Transaction) -> None:
        with self._lock:
            self._transactions.append(transaction)

    def get_all(self) -> List[Transaction]:
        with self._lock:
            return list(self._transactions)

    def get_by_date(self, date: datetime) -> List[Transaction]:
        with self._lock:
            return [
                t for t in self._transactions if t.date.date() == date.date()
            ]
