# Báo cáo cá nhân — TranTungLam-2A202603893

## 1. Thông tin thành viên

- Họ tên: Trần Tùng Lâm
- MSSV: 2A202603893
- Email: lamtt262004@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): **TV1 · Người viết code (trước giờ giải lao) + người kiểm số (sau giờ giải lao)**

## 2. Phần việc phụ trách

- **CP1 · Nhiệm vụ A:** viết `src/lab13.py` phần A1 (ba hàm kinh tế của việc chạy lại), A2 (`mo_hinh`), A3 (tách theo `loai`), A4 (cộng chi phí cố định); điền A1–A4 trong `report/team/bang_chi_phi.md`.
- **CP2 · Nhiệm vụ B:** viết B1–B4 trong `src/lab13.py` (độ nhạy, đổi một cặp, giới hạn số lần chạy, xem lại 100%); điền B1–B4 và xếp hạng ba yếu tố trong `bang_chi_phi.md`.
- **Bàn giao và CP3:** push code CP1–CP2 để TV3 nhận bàn phím; dựng sẵn khung D1 (hằng số, chữ ký 4 hàm, hàm in 5 câu) để TV3 viết thân hàm.
- **CP4 · Kiểm số:** đối chiếu D1 của TV3 và phần chú thích D1 trong `pilot_plan.yaml` với đáp án, tính tay một con số.
- **CP5:** cấp số cho các dòng rủi ro kinh tế trong `report/team/chi_so.md`; trả lời câu hỏi về chi phí và độ nhạy khi duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **A1:** ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử ĐẠT (1,20 · 1,25 · 1,25). Hệ số chi phí luôn bằng 1/p vì 1 − (1 − p)^k triệt tiêu.
- **A2:** `mo_hinh()` tính tử số trên **mọi** lần chạy (kể cả lần lỗi), mẫu số chỉ đếm `ket_qua == 'thanh_cong'`; nhận sẵn tham số giá, hệ số và `max_lan_chay` để CP2 chỉ cần gọi lại. Kết quả: chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8%, xem lại 40,7% [simulated]. Chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- **A3:** noi_dia 0,22× · hang_nang 0,69× · quoc_te 1,88× · doi_tac 0,85× [simulated]; thêm bảng tỉ lệ ok theo lần thử (quoc_te 30,0% → 11,4% → 2,2%) để chứng minh chạy lại không giúp quoc_te.
- **A4:** phạm vi noi_dia + hang_nang cộng cố định 40 triệu/tháng: 4.599 đ = 0,38× (đủ khối lượng), 5.784 đ = 0,48× (nửa khối lượng) [simulated].
- **B1–B4:** xếp hạng 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương (+23,1%) [simulated]; thêm `assert` tự kiểm "giảm một nửa = −½ gấp đôi"; B3 giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ) dù 1 lần có chi phí mỗi việc thành công thấp nhất; B4 xem lại 100% là 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút), hoà vốn khi mỗi lần xem lại ≤ 5,1 phút [simulated].
- **Khung D1:** hằng số, docstring có công thức và đáp án đối chiếu, `in_d1()` in đủ 5 câu; script vẫn chạy hết khi D1 chưa viết để TV2, TV3 pull về chạy được ngay.
- **Kiểm số D1:** 5 câu của TV3 khớp đáp án (1.251 · 3.103 / 42 người · 1.000 · 300 · m ≥ 299).
- **Rủi ro kinh tế (`chi_so.md`):** đổi dấu hiệu làm lại sang tỉ lệ trong phạm vi pilot 48/982 = 4,9% (ngưỡng 7%), thêm phút xem lại TB 5,0 phút [simulated] sát hoà vốn 5,1 phút, thêm dòng rủi ro khối lượng thấp (chi phí cố định, bảng A4).

## 4. Bằng chứng

| Commit | Nội dung |
| --- | --- |
| `4138ac2` | feat: CP1 xong - A1-A4 mô hình chi phí (`src/lab13.py`, `bang_chi_phi.md`) |
| `87cf98a` | feat: CP2 xong - B1-B4 bảng độ nhạy (`src/lab13.py`, `bang_chi_phi.md`) |
| `f22e2c8` | feat: CP3 - khung D1 cho TV3 (`src/lab13.py`) |
| `3faa529` | docs: CP4-CP5 TV1 kiểm số D1 và cấp số rủi ro kinh tế (`chi_so.md`) |

- File: `src/lab13.py` (A1–A4, B1–B4, khung D1), `report/team/bang_chi_phi.md` (A1–B4), `report/team/chi_so.md` (mục E2).
- Chạy `cd src && python lab13.py`: in `Ba phép thử đáp án biết trước: ĐẠT`, bảng A2, A3, A4, B1–B4, D1 và dòng `Tự kiểm tra "giảm một nửa = −½ gấp đôi": ĐẠT`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code.
- **Dùng vào việc gì:** đọc đề và kiểm tra code B1–B4 và khung D1 trong `lab13.py`.
- **Không dùng AI để:** bịa số, nhãn lỗi hay kết quả duyệt chéo. Mọi con số trong bảng do `src/lab13.py` tính từ hai file CSV; `phieu_cham.md` để nhóm tự điền khi chấm nhóm khác.
- **Cách tự kiểm tra:**
  - Ba phép thử A1 in ĐẠT trước khi làm tiếp.
  - Đối chiếu từng số A2, A3, A4, B1–B4, D1 với số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: tất cả trong ngưỡng 2% (đa số trùng khớp).
  - `assert` trong code: mỗi kịch bản "giảm một nửa" bằng đúng −½ mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).
  - Tính tay: 4.373.585 ÷ 978 = 4.472 đ; (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ; D1 câu b: 1 + 74 × 0,02 = 2,48 → 1.251 × 2,48 = 3.103 → ÷ 75 = 42 người; câu e: 859 × 0,98 ÷ (20 − 859 × 0,02) = 298,5 → 299.
  - Kiểm số liệu trong dòng rủi ro bằng pandas trực tiếp trên CSV (48/982 làm lại trong phạm vi, 177/1.200 được xem lại, phút xem lại TB 5,03).

## 6. Tự đánh giá

- **Làm tốt:** CP1, CP2 xong đúng mốc, số khớp đáp án; code viết để tái dùng (`mo_hinh` nhận tham số nên B1–B4 chỉ là gọi lại), có `assert` tự kiểm; khung D1 giúp TV3 nhận bàn phím nhanh và vẫn tự viết phần tính.
- **Điều đã hiểu:** tử số tính mọi lần chạy vì lần lỗi vẫn tốn tiền, mẫu số chỉ đếm việc thành công vì chỉ chúng tạo giá trị (chia 1.200 sẽ ra 3.645 đ, thấp hơn thật 18%); mô hình cộng tuyến tính nên tác động của một cặp bằng tổng hai tác động riêng; giới hạn rẻ nhất cho công ty (2 lần) khác giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần) vì phải tính phần việc đẩy sang nhân viên.
- **Cần cải thiện:** Phát hiện muộn chỗ ngưỡng chi phí chưa thống nhất giữa luật dừng (8.000 đ) và hồ sơ (0,9×).
