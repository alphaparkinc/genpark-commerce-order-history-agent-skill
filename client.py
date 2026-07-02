from typing import Dict, Any

class OrderHistoryClient:
    def lookup_history(self, email: str) -> Dict[str, Any]:
        # Mock database
        orders_db = {
            "customer@test.com": [
                {"order_id": "ORD-101", "date": "2026-05-01", "total": 45.0, "status": "delivered"},
                {"order_id": "ORD-202", "date": "2026-06-15", "total": 120.0, "status": "shipped"}
            ]
        }
        return {"orders": orders_db.get(email.lower(), [])}
