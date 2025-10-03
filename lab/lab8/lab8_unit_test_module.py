import pytest
from datetime import datetime
from booking import search_salon, book_appointment, connect_db

# Test search_salon
def test_search_salon_found():
    results = search_salon("Quận 1")
    assert len(results) > 0
    assert results[0]["name"] == "Salon A"

def test_search_salon_not_found():
    results = search_salon("Quận 9")  # không có salon ở đây
    assert len(results) == 0

# Test book_appointment
def test_book_success():
    # Đặt lịch thành công
    book_appointment(1, 1, 1, "Fade Cut", datetime(2025, 12, 25, 10, 0))
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM appointments WHERE user_id=1 AND stylist_id=1 AND time_slot=%s",
                (datetime(2025, 10, 15, 15, 0),))
    row = cur.fetchone()
    conn.close()
    assert row is not None

def test_book_stylist_busy():
    # Đặt trùng giờ stylist đã bận
    with pytest.raises(Exception):
        book_appointment(2, 1, 1, "Uốn tóc", datetime(2025, 10, 15, 15, 0))
