# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: GiCungDuoc · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ, gấp 16,3 lần hoá đơn token; trong phạm vi pilot cộng cố định là 4.599 đ (0,38×) | Giả lập | Chủ sản phẩm trợ lý |
| 2 · Ba yếu tố nhạy nhất | Làm lại +51,8%; xem lại +40,7%; lương +23,1% | Giả lập | Chủ sản phẩm trợ lý |
| 3 · So với nhân viên tự làm | 5.865 đ/yêu cầu = 0,49× của 12.000 đ (đã cộng 222 ca nhân viên làm thay) | Giả lập | Chủ sản phẩm trợ lý |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (không có đối chứng): đóng trong 24 giờ và không mở lại 82,8% (994/1.200); bỏ qua gợi ý 27,1% (48/177); lỗi lọt đến khách 4,25% (51/1.200) | Xong, có bằng chứng | Trưởng vận hành CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 16/20 = 80%; 5 ca đủ 5 loại lỗi, mỗi ca có event phát hiện, ngưỡng và vai trò phụ trách | Xong, có bằng chứng | Kỹ sư AI |
| 6 · Pilot plan | Cả 12 depot, 40 nhân viên chia 20 + 20, ngẫu nhiên phân tầng theo depot; 859 yêu cầu mỗi nhóm, mức chênh 6 điểm; 3 luật dừng (an toàn, chi phí 8.000 đ [simulated], mức độ sử dụng); quyết định ngày 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 4.472 → 6.787 đ (+51,8%); xem lại 100%: 11.743 đ = 0,98× của 12.000 đ, trợ lý gần như không tiết kiệm [simulated] | Giả lập | Chủ sản phẩm trợ lý |

**Đề xuất:** Go có điều kiện. Chỉ duyệt kế hoạch pilot, trong phạm vi `noi_dia` và `hang_nang` (0,38× [simulated]); `quoc_te` (1,88× [simulated], thành công 27,3%) và `doi_tac` (0,85× [simulated]) bị loại. Con số bất lợi: nếu phải xem lại 100% thì chi phí là 0,98× [simulated], với 40 nhân viên pilot chỉ đủ mẫu cho mức chênh 6 điểm (power 0,64 nếu tác động thật là 5 điểm), và mọi số chi phí và an toàn ở trên đo trên 6 depot với 20 nhân viên của đợt chạy thử, còn pilot chạy ở cả 12 depot nên 6 depot mới chưa có dữ liệu nào.

- Giữ phạm vi pilot ở `noi_dia` và `hang_nang`, chưa mở `quoc_te` và `doi_tac` · Giám đốc vận hành LogiX-VN · kiểm tra ngày 2026-12-01.
- Xem lại theo mẫu, không xem lại toàn bộ; dừng mở rộng nếu chi phí mỗi việc thành công vượt 0,9× của 12.000 đ [simulated] · Trưởng vận hành CSKH · kiểm tra hằng tuần từ bước 0,25.
- Báo cáo chi phí mỗi việc thành công và tỉ lệ mở lại tách riêng 6 depot đã chạy thử và 6 depot mới; nếu depot mới vượt ngưỡng luật dừng thì chỉ giữ depot cũ · Trưởng vận hành CSKH · kiểm tra hằng tuần từ bước 0,10.
- Chốt trước khi bắt đầu mức chênh 6 điểm, ba luật dừng và cờ tắt trợ lý có hiệu lực trong 30 phút · Giám đốc vận hành LogiX-VN · kiểm tra ngày 2026-12-01.
