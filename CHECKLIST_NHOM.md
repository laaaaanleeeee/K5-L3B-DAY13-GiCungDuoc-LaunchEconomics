# Checklist công việc Lab 13 (nhóm 3 người)

Vai: **TV1** = viết code + kiểm số · **TV2** = gắn nhãn 1 + pilot_plan · **TV3** = gắn nhãn 2 + giữ hồ sơ.

**Đổi người code sau giờ giải lao:** trước 15:35 TV1 cầm bàn phím (CP1, CP2). Sau giờ giải lao **TV3 cầm bàn phím** viết D1 trong `lab13.py`. TV1 chuyển sang kiểm số và đối chiếu với slide đáp án. TV2 chạy lại `lab13.py` trên máy mình ở bước bàn giao để cả TV2 và TV3 đều tự chạy được code. Chi tiết ở mục "Bàn giao" bên dưới.

## 0. Chuẩn bị (14:00–14:10)
- [ ] **TV3:** Tạo repo nhóm tên `K5-L3B-DAY13-TenNhom-LaunchEconomics` (fork hoặc đổi `origin`), mời các thành viên và giảng viên.
- [ ] **Cả 3:** Clone repo nhóm (không dùng repo đề).
- [ ] **Cả 3:** Cài môi trường trong `src/` (`venv`, `pip install -r requirements.txt`). Chạy thử `python lab13.py`.
- [ ] **Cả 3:** Đọc `docs/du_lieu_va_cong_thuc.md`.
- [ ] **TV3:** Điền vai trong `TEAM.md`, xoá dòng thành viên thứ 4 và ghi rõ vai kiêm nhiệm.
- [ ] **TV3:** Mở sẵn `ho_so_launch_v0.md` để điền dần từ đầu buổi.

## CP1 · A: Mô hình chi phí (14:10–14:53)
- [x] **TV1:** Viết 3 hàm A1 ở dòng `TODO CP1`. Ba phép thử phải ĐẠT (1,20 · 1,25 · 1,25) rồi mới làm tiếp.
- [x] **TV1:** Viết `mo_hinh(runs, reqs, …)` (A2).
- [x] **TV1:** Chạy lại theo từng giá trị cột `loai` (A3).
- [x] **TV1:** Cộng chi phí cố định 40 triệu/tháng cho `noi_dia` + `hang_nang` (A4).
- [ ] **TV2, TV3:** Tính tay một con số để đối chiếu với TV1.
- [x] **TV1:** Điền bảng A2 (đủ 9 dòng, 2 dòng giả lập có nhãn `simulated`) và A3 (đủ 4 dòng) vào `bang_chi_phi.md`.
- [ ] **Cả 3:** Đối chiếu số với slide đáp án (lệch không quá 2%).
- [ ] **Cả 3:** Hiểu được vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`.

## CP2 · B: Bảng độ nhạy (14:53–15:20)
- [x] **TV1:** Chạy 9 kịch bản đổi từng yếu tố (B1).
- [x] **TV1:** Chạy 1 kịch bản đổi một cặp (B2).
- [x] **TV1:** Chạy giới hạn 1/2/3 lần và tính chi phí cả hệ thống (B3).
- [x] **TV1:** Chạy kịch bản xem lại 100% cho `noi_dia` + `hang_nang` (B4).
- [x] **TV1:** Điền B1–B4 vào `bang_chi_phi.md` và xếp hạng 3 yếu tố mạnh nhất.
- [x] **TV1:** Tự kiểm tra: "giảm một nửa" phải bằng nửa mức tăng của "gấp đôi".
- [ ] **TV1, TV3:** Mỗi câu trả lời không quá 3 dòng và có số.
- [ ] **TV1:** Bàn giao cho TV3 (xem mục "Bàn giao đổi người code" ngay dưới).

## Bàn giao đổi người code (giờ giải lao 15:20–15:35)
- [ ] **TV1:** Chạy `python lab13.py`, ba phép thử ĐẠT. Commit và push `lab13.py` (ví dụ `feat: CP1-CP2 xong`) và đảm bảo A2–A4, B1–B4 đã điền trong `bang_chi_phi.md`.
- [ ] **TV3 (người code mới):** `git pull`, chạy `lab13.py` trên máy mình, ba phép thử ĐẠT (1,20 · 1,25 · 1,25).
- [ ] **TV2:** `git pull` và chạy `lab13.py` trên máy mình, ba phép thử ĐẠT, để có hai người ngoài TV1 chạy được code.
- [ ] **TV3:** Tự đọc `mo_hinh()` và trả lời không nhìn đáp án: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm `thanh_cong`; tham số nào là giá, tham số nào là hệ số; chi phí cố định 40 triệu/tháng cộng vào đâu.
- [ ] **TV3:** Tự tay tính lại một con số (ví dụ chi phí mỗi việc thành công của một `loai`) và so khớp với `mo_hinh()`.
- [ ] **TV1:** Chuyển sang vai kiểm số: ngồi cạnh trả lời câu hỏi, sau đó đối chiếu kết quả D1 với slide đáp án.
- [ ] **Cả 3:** Nếu máy ai không chạy được Python, ghi lệnh và output vào mục 5 của `group_report.md`.

## CP3 · C: Bảng lỗi (15:35–16:08)
- [ ] **TV2, TV3:** Ngồi tách nhau, gắn nhãn độc lập 20 ca trong 8 phút (không trao đổi).
- [ ] **TV2, TV3:** So nhãn và tính tỉ lệ đồng thuận (cần từ 16/20). Không sửa bộ nhãn độc lập sau khi so.
- [ ] **TV2:** Với ca không trùng, thống nhất nhãn và ghi một câu quy tắc phân biệt.
- [ ] **TV2:** Chọn 5 ca, mỗi loại một ca. Điền bảng khắc phục trong `bang_loi.md`, mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách.
- [x] **TV1:** Hoàn thiện CP2 và viết sẵn khung D1 trong lúc hai người gắn nhãn (8 phút đầu, khoảng 15:35–15:43).
- [ ] **TV3:** Chỉ cầm bàn phím viết D1 **sau khi** đã gắn nhãn xong và so nhãn với TV2 (từ khoảng 15:43).

## CP4 · D: pilot_plan.yaml (16:08–16:36)
- [ ] **TV3 (người code mới):** Viết D1 ở dòng `TODO CP4` trong `lab13.py` và tính 5 câu: cỡ mẫu theo yêu cầu, theo nhân viên, theo depot, mức chênh 6 điểm. Commit bằng tài khoản git của TV3.
- [ ] **TV1 (kiểm số):** Đối chiếu kết quả D1 với slide đáp án và tính tay một con số.
- [ ] **TV2:** Trả lời 5 câu D2 "tách được tác động".
- [ ] **TV2:** Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi đặt luật an toàn.
- [ ] **TV2:** Điền mọi dấu `?` trong `pilot_plan.yaml`. Ghi kết quả D1 và D2 vào chú thích đầu file.
- [ ] **TV2:** Viết ≥ 3 luật dừng (an toàn, chi phí, mức độ sử dụng) theo mẫu NẾU–TRONG–THÌ–KHÔNG THÌ, mỗi luật có ngưỡng, thời hạn và người có quyền dừng.
- [ ] **TV2:** Cách chia có ít nhất 20 cụm mỗi nhóm hoặc ghi rõ đánh đổi.
- [ ] **TV2:** Kiểm tra `yaml.safe_load` chạy không lỗi, và `grep -v '^ *#' … | grep -n '?'` không in gì.

## CP5 · E: Chỉ số, rủi ro, hồ sơ (16:36–17:00)
- [ ] **TV3:** Tính thử 3 chỉ số (chính, dùng, an toàn) và đề xuất thêm 1 chỉ số dùng, 1 chỉ số an toàn.
- [ ] **TV3:** Liệt kê ≥ 6 event có `trace_id` trong `chi_so.md`.
- [ ] **TV1:** Cấp số cho ≥ 2 dòng rủi ro kinh tế lấy từ bảng độ nhạy.
- [ ] **TV3:** Chốt `ho_so_launch_v0.md`: 1 trang, đủ 7 mục. Mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và người phụ trách là một vai trò. Dòng cuối là đề xuất Go, Go có điều kiện hoặc No-go.
- [ ] **TV2:** Rà soát: `grep -rni production report/team` không in gì, mọi số giả lập có nhãn `simulated`, phạm vi đã thu hẹp có lý do bằng số.
- [ ] **Cả 3:** Gửi hồ sơ cho nhóm hội đồng lúc 17:00.

## Duyệt chéo Gate 2a (17:00–17:45)
- [ ] **TV3:** Điền `phieu_cham.md` khi chấm nhóm n+1 (nhóm cuối chấm nhóm 1).
- [ ] **TV1:** Trả lời câu hỏi về chi phí và độ nhạy.
- [ ] **TV2:** Trả lời câu hỏi về lỗi và pilot.
- [ ] **Cả 3:** Bảo vệ được lý do của đề xuất cuối, kể cả số bất lợi.

## Đóng gói và nộp (17:45–18:00, hạn 23h59 GMT+7)
- [ ] **Mỗi người:** Copy `report/team/MSSV_HoTen.md` thành file riêng (tên không dấu). Điền phần việc, đóng góp, bằng chứng, công cụ AI đã dùng và cách tự kiểm tra.
- [ ] **TV3:** Điền `report/team/group_report.md`.
- [ ] **TV3:** Hoàn thiện `TEAM.md` (URL repo, nhánh nộp, commit chốt) và ghi ai viết code trước giờ giải lao (TV1), ai sau giờ giải lao (TV3).
- [ ] **Một người:** `cd src && python3 lab13.py` chạy hết trên máy khác, rồi commit và push. Không commit `.venv/` hay `.env`.
- [ ] **Cả 3:** Đủ 6 file hồ sơ trong `report/team/` đúng tên, không có từ "production", repo mở được cho người chấm.
- [ ] **Mỗi người, tự nộp:** Nộp cùng link repo trên LMS bằng tài khoản cá nhân. Ai không nộp thì không có điểm.
