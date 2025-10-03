import mysql.connector
from datetime import datetime

# Kết nối DB
def connect_db():
    return mysql.connector.connect(
        user="root",        # user MySQL của bạn
        password="112705",  # đổi thành mật khẩu bạn đã đặt khi cài MySQL
        database="haircut_demo"
    )

# Tìm salon theo vị trí
def search_salon(location):
    conn = connect_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT salon_id, name, address FROM salons WHERE location=%s", (location,))
    results = cur.fetchall()
    conn.close()
    return results

# Đặt lịch hẹn
def book_appointment(user_id, salon_id, stylist_id, hairstyle, time_slot):
    conn = connect_db()
    cur = conn.cursor()
    try:
        conn.start_transaction()

        # Kiểm tra stylist có rảnh không
        cur.execute("SELECT COUNT(*) FROM appointments WHERE stylist_id=%s AND time_slot=%s",
                    (stylist_id, time_slot))
        if cur.fetchone()[0] > 0:
            raise Exception("Stylist is not available at this time")

        # Tạo booking
        cur.execute("""
            INSERT INTO appointments(user_id, salon_id, stylist_id, hairstyle, time_slot, status) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user_id, salon_id, stylist_id, hairstyle, time_slot, "CONFIRMED"))

        conn.commit()
        print("✅ Appointment booked successfully!")
    except Exception as e:
        conn.rollback()
        print("❌ Error:", e)
        raise
    finally:
        conn.close()
