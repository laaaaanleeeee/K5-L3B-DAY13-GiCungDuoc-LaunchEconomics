# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Thành Nam · Người gắn nhãn 2: Lê Hải Lân (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Ngầm |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Ngầm | Không | Giới hạn hệ thống |
| 12 | Ngầm | Hệ thống | Không | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 8 → **Ngầm**: trợ lý dẫn một điều khoản không tồn tại nhưng số tiền vẫn đúng, nên cả khách lẫn hệ thống đều không nhận ra; sai mà không ai thấy cho tới khi kiểm tra là Ngầm, không phải Hệ thống.
- Ca 11 → **Giới hạn hệ thống**: trợ lý không xử lý được dạng đầu vào (tin nhắn thoại) và đã báo ngay cho khách, nên lỗi lộ ra chứ không ngầm; không làm được dù cố là Giới hạn hệ thống (người gắn nhãn 2 ghi nhầm).
- Ca 12 → **Ngầm**: tool trả thiếu trường làm trợ lý gọi lại nhiều lần nhưng kết quả cuối vẫn đúng, nên suốt 3 tuần không ai thấy chi phí token tăng gấp 3; kết quả đúng che mất cách làm sai thì là Ngầm.
- Ca 17 → **Ngầm**: trợ lý dùng bảng giá cũ trong bộ nhớ đệm, lệch nhỏ trên 212 đơn trong 9 ngày mà không khách nào mở lại và hệ thống không biết đã có bản cập nhật; vi phạm chính sách nhưng không ai nhận ra là Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_refund_rejected` (mã lỗi ngân hàng "sai số tài khoản", có `trace_id`); cảnh báo khi > 1% lệnh hoàn trong ngày, đếm mỗi ngày | Kiểm tra độ dài và định dạng số tài khoản ngay khi khách nhập; hiện tên chủ tài khoản để khách xác nhận trước khi tạo lệnh hoàn | Kỹ sư backend |
| 20 | Hệ thống | Đếm event `refund_created` theo mã vận đơn: ≥ 1 đơn có từ 2 lệnh hoàn trở lên trong 24 giờ thì cảnh báo ngay; job chạy mỗi 15 phút | Thêm khoá chống trùng (mã vận đơn + loại hoàn); yêu cầu gửi lại trả về trạng thái lệnh cũ và báo khách "đang xử lý"; thu hồi khoản hoàn thừa | Kỹ sư backend |
| 18 | Ngữ cảnh | Event `request_reopened` có lý do "hoàn thiếu" trong khi số tiền hoàn khớp chính sách; theo dõi hằng tuần, cảnh báo khi tỉ lệ mở lại 7 ngày vượt mức hiện tại 4,25% | Mẫu tin nhắn luôn ghi cách tính (phí gốc × tỉ lệ hoàn theo điều khoản) kèm link chính sách; đo lại tỉ lệ mở lại sau 2 tuần | PM trợ lý hoàn phí |
| 13 | Giới hạn hệ thống | Event `intent_classified` = ngoài phạm vi mà không có `out_of_scope_notice` hoặc `handoff_to_staff` trong cùng `trace_id`; ngưỡng > 0 ca mỗi ngày, cộng kiểm tra mẫu 50 hội thoại mỗi tuần | Thêm bước nhận diện yêu cầu ngoài phạm vi (bảo hiểm hàng hoá); trả lời rõ "trợ lý không xử lý được" và chuyển đúng đầu mối công ty bảo hiểm | Kỹ sư AI |
| 17 | Ngầm | Ghi `price_table_version` trong mỗi event `refund_calculated`; job đối soát hằng ngày so với bản hiện hành, ≥ 1 đơn dùng bản cũ thì cảnh báo; kiểm tra mẫu 50 đơn mỗi tuần | Xoá bộ nhớ đệm ngay khi bảng giá đổi phiên bản, giới hạn thời gian lưu đệm tối đa 1 giờ; hoàn bù 212 đơn bị lệch | Kỹ sư dữ liệu |
