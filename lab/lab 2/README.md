# Use Case Descriptions - Mini App Cắt tóc

## Use Case 1: Đặt lịch hẹn
- **Use Case Name:** Đặt lịch hẹn  
- **Actor:** Khách hàng  
- **Mục tiêu:** Khách hàng có thể đặt lịch hẹn trước tại tiệm tóc để tránh chờ đợi.  
- **Điều kiện tiên quyết:**  
  - Khách hàng đã đăng ký/đăng nhập vào app  
  - Hệ thống có danh sách dịch vụ, nhân viên và khung giờ trống  
- **Luồng sự kiện chính:**  
  1. Khách hàng mở chức năng **Đặt lịch hẹn**  
  2. Hệ thống hiển thị danh sách dịch vụ, stylist/barber và khung giờ còn trống  
  3. Khách hàng chọn dịch vụ, stylist và thời gian mong muốn  
  4. Hệ thống xác nhận thông tin đặt lịch  
  5. Khách hàng nhấn **Xác nhận** → hệ thống lưu lại lịch hẹn  
- **Luồng thay thế:**  
  - Nếu khung giờ stylist đã kín → hệ thống thông báo và gợi ý khung giờ khác  
- **Kết quả:** Lịch hẹn được lưu, khách hàng nhận thông báo xác nhận  

---

## Use Case 2: Thanh toán dịch vụ
- **Use Case Name:** Thanh toán dịch vụ  
- **Actor:** Khách hàng  
- **Mục tiêu:** Khách hàng thanh toán nhanh chóng sau khi sử dụng dịch vụ  
- **Điều kiện tiên quyết:**  
  - Khách hàng đã hoàn thành dịch vụ tại salon  
  - Hệ thống có thông tin đơn hàng  
- **Luồng sự kiện chính:**  
  1. Hệ thống hiển thị tổng chi phí dịch vụ  
  2. Khách hàng chọn phương thức thanh toán (tiền mặt, thẻ, ví điện tử)  
  3. Nếu thanh toán online, hệ thống kết nối đến cổng thanh toán  
  4. Khách hàng xác nhận thanh toán  
  5. Hệ thống thông báo **Thanh toán thành công**  
- **Luồng thay thế:**  
  - Nếu thanh toán thất bại → hiển thị thông báo và yêu cầu thử lại hoặc chọn phương thức khác  
- **Kết quả:** Dịch vụ được thanh toán, khách hàng nhận hóa đơn/biên nhận điện tử  
