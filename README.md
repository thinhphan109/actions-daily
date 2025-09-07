🚀 Nhật Ký Tự Động Hóa Hàng Ngày
Đây là một dự án sử dụng GitHub Actions để tự động tạo ra một file ghi chú (dưới dạng Markdown) mới mỗi ngày ngay tại thư mục gốc của repository. File này được làm phong phú với nhiều thông tin hữu ích và thú vị, được lấy tự động từ các API công khai trên Internet.

Mỗi khi có một file mới được tạo hoặc cập nhật, một thông báo đẹp mắt sẽ được gửi đến kênh Discord của bạn.

✨ Các Module Hiện Có
Bản tin hàng ngày của bạn sẽ bao gồm các thông tin sau:

🗓️ Lịch Hôm Nay: Ngày, tháng, năm, thứ, tuần ISO và ngày trong năm.

🇻🇳 Ngày Lễ Việt Nam: Kiểm tra và thông báo nếu hôm nay là ngày nghỉ lễ.

🌤️ Thời tiết & Chỉ số UV: Dữ liệu thời tiết và chỉ số tia cực tím tại địa điểm được cấu hình.

💰 Dữ liệu tài chính: Tỷ giá USD/VND và giá vàng SJC.

📈 Giá Tiền Mã Hóa: Cập nhật giá các đồng coin phổ biến như BTC, ETH, SOL, và nhiều hơn nữa.

🛰️ Vị Trí Trạm ISS: Hiển thị vị trí hiện tại của Trạm Vũ trụ Quốc tế và dịch ngược ra tên quốc gia/khu vực.

🚀 Lịch Phóng Tên Lửa: Thông tin về vụ phóng tên lửa đáng chú ý tiếp theo trên toàn cầu.

#️⃣ Sự Thật Về Con Số: Một sự thật thú vị được dịch sang tiếng Việt, liên quan đến một con số ngẫu nhiên.

💡 Lời khuyên ngắn: Một lời khuyên ngẫu nhiên được dịch sang tiếng Việt.

🏛️ Triết Lý Stoic: Một câu trích dẫn sâu sắc từ các nhà triết học Khắc kỷ, được dịch sang tiếng Việt.

⚙️ Cách Hoạt Động
Dự án hoạt động dựa trên một workflow duy nhất của GitHub Actions được đặt tại .github/workflows/auto-daily-note.yml.

Lập lịch (Schedule): Workflow được kích hoạt tự động mỗi ngày vào lúc 00:05 (giờ Việt Nam) thông qua cron. Nó cũng có thể được chạy thủ công (workflow_dispatch).

Thực thi Script: Một script Bash được chạy trên môi trường ubuntu-latest.

Gọi API: Script sử dụng curl để gọi hàng loạt các API công khai miễn phí để lấy dữ liệu.

Xử lý dữ liệu: Dữ liệu JSON trả về được xử lý và định dạng bằng công cụ jq.

Ghi file: Nội dung đã định dạng được ghi vào file YYYY-MM-DD.md. Cơ chế comment đánh dấu (<!-- MODULE-ID -->) đảm bảo mỗi module chỉ được thêm vào một lần duy nhất.

Commit & Push: Nếu file có thay đổi, workflow sẽ tự động commit và đẩy file lên repository.

Thông báo Discord: Nếu có commit mới, một thông báo tóm tắt đẹp mắt sẽ được gửi đến Discord thông qua Webhook.

🛠️ Hướng Dẫn Cài Đặt
Bạn có thể dễ dàng áp dụng dự án này cho repository của riêng mình.

Sao chép Workflow:

Cách đơn giản nhất là Fork repository này.

Hoặc, bạn có thể tạo một thư mục .github/workflows trong repository của bạn và sao chép nội dung của file auto-daily-note.yml vào đó.

Bật GitHub Actions:

Vào tab Settings > Actions > General trong repository của bạn.

Đảm bảo rằng "Allow all actions and reusable workflows" được chọn và bật.

(Bắt buộc) Cấu hình Discord Webhook:

Trong kênh Discord bạn muốn nhận thông báo, vào Edit Channel > Integrations > Webhooks > New Webhook.

Đặt tên và sao chép Webhook URL.

Trong repository GitHub, vào Settings > Secrets and variables > Actions.

Nhấn New repository secret.

Đặt tên secret là DISCORD_WEBHOOK_URL.

Dán URL của webhook vào và lưu lại.

🎨 Tùy Chỉnh
Bạn có thể dễ dàng tùy chỉnh nội dung của bản tin:

Thay đổi địa điểm: Sửa các biến CITY, LAT, LON ở đầu file .yml để lấy thông tin thời tiết cho địa điểm của bạn.

Thêm/Bỏ Module: Trong step "Cập nhật nội dung tự động", tìm đến khu vực "GỌI CÁC HÀM" và thêm hoặc xóa các dòng append_... tương ứng với module bạn muốn.

Chúc bạn có những bản tin tự động thật thú vị!