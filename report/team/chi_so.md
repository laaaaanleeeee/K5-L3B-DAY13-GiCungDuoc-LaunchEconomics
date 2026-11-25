# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng (+51,8%) | Làm lại gấp đôi: chi phí mỗi việc thành công 4.472 đ → 6.787 đ (+51,8%), yếu tố mạnh nhất trong bảng B1 và B2 [simulated] | Tỉ lệ yêu cầu `ket_qua = lam_lai`, hiện 74/1.200 = 6,2%. Theo dõi hằng tuần; vượt 8% hai tuần liên tiếp là cảnh báo | Tạm dừng nhận thêm loại yêu cầu có tỉ lệ làm lại cao nhất, xem lại các ca làm lại để tìm nguyên nhân gốc | Chủ sản phẩm trợ lý |
| Phải xem lại gần hết yêu cầu (0,98×) | Xem lại 100% cho `noi_dia` + `hang_nang`: 11.743 đ/việc = 0,98× của 12.000 đ, trợ lý gần như không tiết kiệm; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) [simulated] | Tỉ lệ yêu cầu được xem lại, hiện 177/1.200 = 14,8%; và số phút xem lại trung bình mỗi ca. Vượt 30% hoặc quá 5 phút/ca là cảnh báo | Giữ xem lại theo mẫu thay vì xem lại toàn bộ; dừng mở rộng nếu chi phí mỗi việc thành công vượt 0,9× của 12.000 đ | Trưởng vận hành CSKH |
