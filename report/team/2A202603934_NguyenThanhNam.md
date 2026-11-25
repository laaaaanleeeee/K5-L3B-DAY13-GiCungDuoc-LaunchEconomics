# Báo cáo cá nhân — NguyenThanhNam-2A202603934

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thành Nam
- MSSV: 2A202603934
- Email: ishodajo@gmail.com
- Vai trong nhóm: Người gắn nhãn 1 (kiêm viết `pilot_plan.yaml`)

## 2. Phần việc phụ trách

- Người gắn nhãn 1: gắn nhãn độc lập 20 ca lỗi, thống nhất các ca không trùng, bảng khắc phục (`bang_loi.md`).
- Viết kế hoạch pilot `pilot_plan.yaml`: D2, luật dừng, cách chia nhóm.
- Tính tay đối chiếu chi phí với người viết code; chạy lại `lab13.py` trên máy tôi ở bước bàn giao.
- Rà soát hồ sơ trước khi gửi hội đồng; trả lời câu hỏi về lỗi và pilot khi duyệt chéo.

## 3. Đóng góp cụ thể

- **Chuẩn bị:** cài môi trường trong `src/` (pandas, numpy, scipy, statsmodels), chạy thử `lab13.py`.
- **CP1 · Chi phí:** tính tay độc lập, không dùng `mo_hinh()`. Chi phí mỗi việc thành công của `noi_dia` = (178.687 token + tool + 942.000 xem lại + 990.000 làm lại) ÷ 783 = **2.696 đ** [simulated]. Tính lại cả A2–A4: 4.472 đ/việc thành công, gấp 16,3 lần hoá đơn token; trong phạm vi cộng cố định 4.599 đ = 0,38× [simulated]. Tất cả khớp `lab13.py`.
- **Bàn giao:** chạy `lab13.py` trên máy tôi, ba phép thử ĐẠT (1,20 · 1,25 · 1,25), các bảng A2–B4 khớp số đối chiếu.
- **CP3 · Bảng lỗi:** gắn nhãn độc lập 20 ca; so với người gắn nhãn 2 (Lê Hải Lân) được **16/20 = 80%**; chốt 4 ca lệch (8, 11, 12, 17) kèm quy tắc phân biệt; bảng khắc phục 5 ca (1, 20, 18, 13, 17) đủ năm loại, mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.
- **CP4 · Pilot:** tính tỉ lệ mở lại 7 ngày hiện tại **4,25%** (51/1.200), trong phạm vi **3,97%** (39/982) trước khi đặt luật an toàn; trả lời 5 câu D2; điền đủ các trường, ghi D1 và D2 vào chú thích; 3 luật dừng (an toàn, chi phí, mức độ sử dụng) đủ NẾU – TRONG – THÌ – KHÔNG THÌ. Chọn chia theo nhân viên 20 + 20, ghi đánh đổi MDE 6 điểm (power 0,64 nếu tác động thật 5 điểm). Phát hiện 6 depot chạy thử chỉ có 20 nhân viên nên mở phạm vi ra 12 depot, 40 nhân viên; kiểm tra khối lượng: ≈ 31 yêu cầu/người/ngày, m ≥ 299 cần khoảng 10 ngày làm việc.
- **CP5 · Rà soát:** kiểm tra `report/team` không có từ cấm theo quy tắc 5 của README, phạm vi thu hẹp có lý do bằng số; đối chiếu lại các số trong `chi_so.md` và `ho_so_launch_v0.md` với dữ liệu (82,8%; 27,1%; 4,25%; 5,03 phút [simulated]). Sửa lỗi tìm được: người phụ trách mục 1, 2, 3, 7 của hồ sơ đổi từ tên người sang vai trò; thêm nhãn `[simulated]` cho các hệ số × còn thiếu.
- **Duyệt chéo:** soạn phiếu tự chấm thử theo mẫu `phieu_cham.md` để luyện bảo vệ.

## 4. Bằng chứng

| Commit | Nội dung |
| --- | --- |
| `63188b8` | Thêm thông tin thành viên vào `TEAM.md` (PR #1) |
| `e48ca47` | CP3 `bang_loi.md`: nhãn người 1, đồng thuận 16/20, quy tắc ca không trùng, bảng khắc phục 5 ca |
| `c6bc353` | CP4 `pilot_plan.yaml`: D1, D2, 3 luật dừng, chia theo nhân viên 20 + 20 |
| `b55c0d0` | CP4 sửa `scope`: 12 depot, 40 nhân viên để đủ 20 cụm mỗi nhóm |
| `2d21416` | CP5 rà soát: người phụ trách là vai trò, thêm nhãn `simulated` cho hệ số × |

- File: `report/team/bang_loi.md` (cột "Nhãn người 1", quy tắc, bảng khắc phục), `report/team/pilot_plan.yaml`.
- Con số tự tính: 2.696 đ (noi_dia) [simulated]; 4,25% và 3,97% mở lại 7 ngày; 16/20 đồng thuận; 20 nhân viên trong 6 depot chạy thử; power 0,64.

## 5. Công cụ AI đã dùng

- **Claude Code:** soạn nháp bảng khắc phục, `pilot_plan.yaml`, rà soát hồ sơ; viết script tính tay CP1.
- **Tự kiểm tra:** so số với `lab13.py` và số đối chiếu trong hướng dẫn (lệch < 2%); chạy lại bằng pandas các tỉ lệ dùng cho luật dừng; `yaml.safe_load` không lỗi, không còn dấu `?`.

## 6. Tự đánh giá

- Hoàn thành phần gắn nhãn, bảng khắc phục, kế hoạch pilot và rà soát hồ sơ; tính tay lại toàn bộ CP1 để đối chiếu.
- Hiểu và tự giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`; vì sao với 40 nhân viên cỡ mẫu hiệu dụng tối đa chỉ 1.000 < 1.251 nên phải chấp nhận mức chênh 6 điểm.
- Cần cải thiện: lần đầu viết `scope` chỉ ghi 6 depot chạy thử, không khớp với cách chia 20 + 20; đã phát hiện và sửa ở commit `b55c0d0`.
