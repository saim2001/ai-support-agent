from app.tools import get_order_status


def test_existing_order():
    result = get_order_status("1001")

    assert result["order_id"] == "1001"
    assert result["status"] == "shipped"


def test_missing_order():
    result = get_order_status("9999")

    assert "error" in result