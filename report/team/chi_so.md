# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994 / 1.200 = **82,8%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | (41 + 7) / 177 = 48 / 177 = **27,1%** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51 / 1.200 = **4,25%** |
| Dùng | Nhóm tự đề xuất: phút xem lại trung bình mỗi yêu cầu được xem lại [simulated] | tổng `phut_xem_lai_simulated` ÷ số yêu cầu có `duoc_xem_lai` bằng 1 | Không cần tính |
| An toàn | Nhóm tự đề xuất: số yêu cầu bị hoàn trùng trong 24 giờ | số `request_id` có từ 2 event `refund_created` trở lên trong 24 giờ, đếm mỗi ngày; ngưỡng > 0 | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng. Con số 82,8% là chỉ số trong đợt chạy thử, không so được với mức 0,70 của nhóm chỉ có nhân viên. Ba chỉ số đầu tính từ cột không có đuôi `_simulated`; chỉ số dùng do nhóm đề xuất dùng cột giả lập nên có nhãn `simulated`.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_received` | Cổng tiếp nhận yêu cầu | request_id, depot, staff_id, loai, so_tien_vnd, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Trợ lý | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Cuối mỗi lần chạy của trợ lý |
| `refund_calculated` | Trợ lý | request_id, so_tien_hoan, price_table_version, trace_id | Khi trợ lý tính xong số tiền hoàn |
| `refund_created` | Sổ cái hoàn tiền | request_id, ma_van_don, so_tien_hoan, trace_id | Khi lệnh hoàn được ghi vào sổ cái |
| `review_decision` | Nhân viên CSKH | request_id, staff_id, quyet_dinh_xem_lai (`giu`, `sua`, `bo`), phut_xem_lai, trace_id | Khi nhân viên bấm quyết định xem lại |
| `handoff_to_staff` | Trợ lý | request_id, ly_do, so_lan_chay, trace_id | Khi chạy hết 3 lần vẫn lỗi hoặc ngoài phạm vi |
| `request_closed` | Hệ thống | request_id, ket_qua (`thanh_cong`, `lam_lai`, `chuyen_nhan_vien`), thoi_diem_dong, trace_id | Khi yêu cầu được đóng |
| `request_reopened` | Khách hoặc nhân viên CSKH | request_id, ly_do, so_ngay_sau_khi_dong, trace_id | Khi yêu cầu bị mở lại trong 7 ngày |

Các event dùng trong cách phát hiện ở `bang_loi.md` (`bank_refund_rejected`, `intent_classified`, `out_of_scope_notice`) cũng gắn `trace_id` và được thêm vào danh sách khi triển khai pilot.

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `request_received` và `request_closed` (hiệu thời điểm ≤ 24 giờ), `request_reopened` (không có event nào trong 7 ngày). Đo được.
- Tỉ lệ bỏ qua gợi ý: `review_decision` (đếm `sua` và `bo` chia tổng số event). Đo được.
- Tỉ lệ lỗi lọt đến khách: `request_reopened` chia số `request_closed`. Đo được; lưu ý "mở lại" chỉ là dấu hiệu gần đúng của lỗi lọt đến khách, không phải mọi ca mở lại đều do lỗi trợ lý.
- Phút xem lại trung bình [simulated]: `review_decision` (thuộc tính `phut_xem_lai`). Đo được.
- Yêu cầu bị hoàn trùng: `refund_created` đếm theo `ma_van_don` trong 24 giờ. Đo được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng (+51,8%) | Làm lại gấp đôi: chi phí mỗi việc thành công 4.472 đ → 6.787 đ (+51,8%), yếu tố mạnh nhất trong bảng B1 và B2 [simulated] | Tỉ lệ yêu cầu `ket_qua = lam_lai` trong phạm vi pilot `noi_dia` + `hang_nang`, hiện 48/982 = 4,9% (toàn mẫu 74/1.200 = 6,2%). Theo dõi hằng tuần; vượt 7% hai tuần liên tiếp là cảnh báo | Tạm dừng nhận thêm loại yêu cầu có tỉ lệ làm lại cao nhất, xem lại các ca làm lại để tìm nguyên nhân gốc | Chủ sản phẩm trợ lý |
| Phải xem lại gần hết yêu cầu (0,98×) | Xem lại 100% cho `noi_dia` + `hang_nang`: 11.743 đ/việc = 0,98× của 12.000 đ, trợ lý gần như không tiết kiệm; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) [simulated] | Tỉ lệ yêu cầu được xem lại, hiện 177/1.200 = 14,8% (phạm vi 128/982 = 13,0%); và số phút xem lại trung bình mỗi ca, hiện 5,0 phút [simulated], đã sát mức hoà vốn 5,1 phút. Vượt 30% hoặc quá 5 phút/ca là cảnh báo | Giữ xem lại theo mẫu thay vì xem lại toàn bộ; đo phút xem lại thật từ tuần 1 thay cho số simulated; dừng mở rộng nếu chi phí mỗi việc thành công vượt 0,9× của 12.000 đ | Trưởng vận hành CSKH |
| Khối lượng thấp hơn dự kiến (chi phí cố định) | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng (33.750 việc thành công) → 4.599 đ = 0,38×; còn một nửa khối lượng thì +2.370 đ/việc → 5.784 đ = 0,48× (bảng A4) [simulated] | Số việc thành công trong phạm vi theo tuần, kế hoạch ≈ 7.900/tuần ở quy mô đầy đủ (33.750 × 7 / 30); dưới 50% kế hoạch hai tuần liên tiếp là cảnh báo | Không mở rộng pilot; báo cáo hội đồng chi phí mỗi việc thành công đã cộng cố định ở khối lượng thật | Chủ sản phẩm trợ lý |
