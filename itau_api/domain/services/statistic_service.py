from typing import Dict, List

from itau_api.domain.entities.transaction import Transaction


class StatisticService:
    @staticmethod
    def calculate_average(transactions: List[Transaction]) -> Dict[str, float]:
        if not transactions:
            return {'count': 0, 'sum': 0.0, 'avg': 0.0, 'max': 0.0, 'min': 0.0}

        values = [t.amount for t in transactions]

        total = sum(values)
        avg = total / len(values)

        return {
            'count': len(values),
            'sum': float(total),
            'avg': float(avg),
            'max': float(max(values)),
            'min': float(min(values)),
        }
