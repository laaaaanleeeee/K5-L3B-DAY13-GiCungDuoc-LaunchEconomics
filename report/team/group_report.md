# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: GiCungDuoc
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN (mẫu 1.200 yêu cầu, 1.624 lần chạy, dữ liệu giả lập) để trả lời bốn câu hỏi: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Cách làm: TV1 viết code A và B trước giờ giải lao, TV3 nhận code viết D1 sau giờ giải lao, TV1 chuyển sang kiểm số; TV2 và TV3 gắn nhãn lỗi độc lập; mọi số giả lập được ghi nhãn `simulated`.

## 3. Giải pháp

- **A, B:** `src/lab13.py` và [bang_chi_phi.md](bang_chi_phi.md): mô hình chi phí từ trace, chia theo loại, cộng chi phí cố định, 9 kịch bản độ nhạy, giới hạn số lần chạy, xem lại 100%.
- **C:** [bang_loi.md](bang_loi.md): hai bộ nhãn độc lập, đồng thuận 16/20, bảng khắc phục 5 ca đủ năm loại.
- **D:** [pilot_plan.yaml](pilot_plan.yaml): cỡ mẫu D1, chia theo nhân viên 20 + 20, ba luật dừng.
- **E:** [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md): chỉ số, 8 event có `trace_id`, hai dòng rủi ro kinh tế, hồ sơ bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token chia số yêu cầu (274,7 đ). Trong phạm vi `noi_dia` + `hang_nang`, cộng chi phí cố định là **4.599 đ = 0,38×** của 12.000 đ [simulated]; `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×) bị loại. Chi phí cả hệ thống 5.865 đ mỗi yêu cầu = 0,49× [simulated].
- Ba yếu tố nhạy nhất [simulated]: số ca làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% **+23,1%**. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ), khác giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ).
- Chỉ số trong đợt chạy thử (không có đối chứng): đóng trong 24 giờ và không mở lại 82,8%; bỏ qua gợi ý 27,1%; lỗi lọt đến khách 4,25%.
- Pilot: chia theo nhân viên, 40 người ở 12 depot chia 20 + 20; cần 859 yêu cầu mỗi nhóm cho mức chênh 6 điểm, vì 20 nhân viên mỗi nhóm chỉ đạt tối đa 1.000 < 1.251 nên không đủ mẫu cho mức chênh 5 điểm (power 0,64).
- **Đề xuất: Go có điều kiện** (xem `ho_so_launch_v0.md`), với con số bất lợi: xem lại 100% làm chi phí lên 0,98× [simulated].
- **Kết quả duyệt chéo nhóm nhận được từ hội đồng:** chưa có, sẽ điền sau khi nhận phiếu của nhóm hội đồng. Nhóm chấm GREEN: 30/30, quyết định Go có điều kiện (`phieu_cham.md`).

## 5. Khó khăn và cách xử lý

- Giờ gắn nhãn độc lập 8 phút trùng với giờ đổi người code: bàn giao xong trước giờ giải lao, người code mới chỉ bắt đầu D1 sau khi so nhãn.
- Lệch 4/20 ca khi gắn nhãn (8, 11, 12, 17): thống nhất theo nguyên nhân gốc, ghi một câu quy tắc cho từng ca.
- Lần đầu `scope` chỉ ghi 6 depot chạy thử, không khớp cách chia 20 + 20 vì mẫu chỉ có 20 nhân viên: sửa thành 12 depot, 40 nhân viên và ghi rõ 6 depot mới chưa có dữ liệu.
- Hồ sơ ban đầu ghi tên người ở cột người phụ trách: đổi sang vai trò và thêm nhãn `simulated` còn thiếu.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và báo cáo cá nhân.

- TV1 (Trần Tùng Lâm): CP1–CP2 (A1–A4, B1–B4), khung D1, kiểm số D1, cấp số rủi ro kinh tế.
- TV2 (Nguyễn Thành Nam): nhãn người 1, bảng khắc phục, D2, luật dừng, `pilot_plan.yaml`, rà soát hồ sơ.
- TV3 (Lê Hải Lân): nhãn người 2, D1, `chi_so.md`, hồ sơ launch v0, phiếu chấm.

## 7. Hạn chế và hướng cải thiện

- Mọi số chi phí dựa trên hai cột `_simulated`; mức tiết kiệm thật chỉ biết sau pilot.
- Đợt chạy thử không có đối chứng nên 82,8% không so được với mức 0,70.
- Số chi phí và an toàn đo trên 6 depot, 20 nhân viên; 6 depot mới chưa có dữ liệu.
- Chỉ đủ mẫu cho mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power chỉ 0,64.
- Hướng cải thiện: tách báo cáo theo depot cũ và mới, đo `phut_xem_lai` thật ở bước rollout 0,10, hạ dần tỉ lệ xem lại.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, lớp `NormalIndPower`
- Dữ liệu và công thức của lab: `docs/du_lieu_va_cong_thuc.md`
