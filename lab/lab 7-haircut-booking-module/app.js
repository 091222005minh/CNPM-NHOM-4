const express = require("express");
const mysql = require("mysql2");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Kết nối MySQL
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  port: 3306,
  password: "123456", // điền mật khẩu MySQL của bạn
  database: "haircut_booking" 
});

db.connect(err => {
  if (err) throw err;
  console.log("✅ Đã kết nối MySQL (haircut_booking)");
});

// API đặt lịch hẹn
app.post("/appointments", (req, res) => {
  const { barber, customer, datetime, service } = req.body;

  if (!barber || !customer || !datetime || !service) {
    return res.status(400).json({ message: "Thiếu thông tin đặt lịch hẹn!" });
  }

  const sql = "INSERT INTO appointments (barber, customer, datetime, service) VALUES (?, ?, ?, ?)";
  db.query(sql, [barber, customer, datetime, service], (err, result) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: "Lỗi server!" });
    }
    res.json({ message: "Đặt lịch thành công!", appointmentId: result.insertId });
  });
});

// Chạy server
app.listen(3000, () => {
  console.log("🚀 Haircut Booking Server chạy tại http://localhost:3000");
});

