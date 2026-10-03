ORDERS = {
    "1001": {
        "customer": "Ahmed",
        "status": "shipped",
        "total": 125.50,
        "estimated_delivery": "2026-10-05",
    },
    "1002": {
        "customer": "Sara",
        "status": "processing",
        "total": 89.99,
        "estimated_delivery": "2026-10-07",
    },
    "1003": {
        "customer": "John",
        "status": "delivered",
        "total": 210.00,
        "estimated_delivery": "2026-09-30",
    },
}


def get_order_status(order_id: str) -> dict:
    """Retrieve order information by order ID."""

    order = ORDERS.get(order_id)

    if not order:
        return {
            "error": f"Order {order_id} was not found."
        }

    return {
        "order_id": order_id,
        **order,
    }