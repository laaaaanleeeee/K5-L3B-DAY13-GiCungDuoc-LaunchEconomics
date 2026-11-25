# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |    Lê Hải Lân    |  2A202603915    |  lehailan110@gmail.com     |  laaaaanleeeee      |  Người gắn nhãn 2, kiêm giữ hồ sơ        |
|   2 | Nguyễn Thành Nam | 2A202603934 | ishodajo@gmail.com | Ishodayo |  Người gắn nhãn 1 (kiêm viết pilot_plan.yaml) |
|   3 |    Trần Tùng Lâm    |   2A202603893   |    lamtt262004@gmail.com   |      lamtt262004   |    Người viết code + kiểm số     |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenThanhNam-2A202603934

Báo cáo đầy đủ: [report/team/2A202603934_NguyenThanhNam.md](report/team/2A202603934_NguyenThanhNam.md)

### Phần việc phụ trách

- Người gắn nhãn 1, kiêm viết `report/team/pilot_plan.yaml`.
- Tính tay đối chiếu CP1; chạy lại `lab13.py` ở bước bàn giao.
- CP3: gắn nhãn độc lập, thống nhất ca không trùng, bảng khắc phục.
- CP4: D2, luật dừng, `pilot_plan.yaml`. CP5: rà soát hồ sơ.

### Đóng góp cụ thể

- CP1: tính tay độc lập chi phí mỗi việc thành công `noi_dia` = 2.696 đ [simulated]; tính lại cả A2–A4 (4.472 đ, 16,3 lần, 4.599 đ = 0,38× [simulated]), khớp `lab13.py`.
- Bàn giao: chạy `lab13.py` trên máy tôi, ba phép thử ĐẠT.
- CP3: bộ nhãn người 1; đồng thuận 16/20 = 80%; chốt 4 ca lệch (8, 11, 12, 17) kèm quy tắc; bảng khắc phục 5 ca đủ năm loại.
- CP4: 5 câu D2; tỉ lệ mở lại 4,25% (phạm vi 3,97%); 3 luật dừng đủ bốn vế; chia theo nhân viên 20 + 20, ghi đánh đổi MDE 6 điểm (power 0,64). Phát hiện 6 depot chạy thử chỉ có 20 nhân viên nên sửa phạm vi ra 12 depot, 40 nhân viên.
- CP5: rà soát `report/team` (không dùng từ cấm theo quy tắc 5, lý do thu hẹp phạm vi bằng số); sửa lỗi: đổi người phụ trách trong hồ sơ từ tên người sang vai trò, thêm nhãn `simulated` còn thiếu.

### Bằng chứng

- Commit: `63188b8`, `e48ca47`, `c6bc353`, `b55c0d0`, `2d21416`.
- File: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603934_NguyenThanhNam.md`.

## TranTungLam-2A202603893

Báo cáo đầy đủ: [report/team/2A202603893_TranTungLam.md](report/team/2A202603893_TranTungLam.md)

### Phần việc phụ trách

- TV1: người viết code trước giờ giải lao (CP1, CP2), người kiểm số sau giờ giải lao.
- CP1–CP2: viết A1–A4, B1–B4 trong `src/lab13.py`; điền `report/team/bang_chi_phi.md`.
- CP3: bàn giao code cho TV3, dựng sẵn khung D1. CP4: kiểm số D1. CP5: cấp số cho rủi ro kinh tế trong `chi_so.md`.

### Đóng góp cụ thể

- CP1: ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); `mo_hinh()` cho chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated]; A3 theo loại (quoc_te 1,88×, chạy lại không giúp: ok 30,0% → 11,4% → 2,2%); A4 cộng cố định 4.599 đ = 0,38× [simulated].
- CP2: B1 đủ 9 kịch bản, có `assert` tự kiểm "giảm một nửa = −½ gấp đôi"; xếp hạng làm lại (+51,8%) · xem lại (+40,7%) · lương (+23,1%); B3 giới hạn 2 lần rẻ nhất cho công ty; B4 xem lại 100% là 11.743 đ = 0,98×, hoà vốn ≤ 5,1 phút [simulated].
- CP3: khung D1 (hằng số, công thức, `in_d1()` in 5 câu), script vẫn chạy hết khi D1 chưa viết.
- CP4: đối chiếu 5 câu D1 của TV3 và chú thích D1 trong `pilot_plan.yaml` với đáp án (1.251 · 3.103 / 42 người · 1.000 · 300 · m ≥ 299), tính tay câu b và câu e.
- CP5: rủi ro kinh tế trong `chi_so.md`: tỉ lệ làm lại trong phạm vi 48/982 = 4,9% (ngưỡng 7%), phút xem lại TB 5,0 phút sát hoà vốn 5,1 phút, thêm dòng rủi ro khối lượng thấp (0,48× khi còn nửa khối lượng) [simulated].

### Bằng chứng

- Commit: `4138ac2`, `87cf98a`, `f22e2c8`, `3faa529`, `77c3c87`.
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/2A202603893_TranTungLam.md`.
