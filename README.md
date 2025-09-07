# 🚀 Nhật Ký Tự Động Hóa Hàng Ngày

_Tự động tạo file trực tiếp tại dự án, cày commit contributions mỗi ngày bằng GitHub Actions, lấy dữ liệu từ các API công khai và gửi thông báo lên Discord._

> **Múi giờ:** Asia/Ho_Chi_Minh • **Lịch chạy:** 00:05 (ICT) mỗi ngày

---

## 📋 Mục Lục

- [✨ Tính Năng](#-tính-năng)
- [⚙️ Cách Hoạt Động](#️-cách-hoạt-động)
- [🛠️ Hướng Dẫn Cài Đặt](#️-hướng-dẫn-cài-đặt)
- [🎨 Tùy Chỉnh](#-tùy-chỉnh)
- [❓ Hỏi Đáp & Khắc Phục Lỗi](#-hỏi-đáp--khắc-phục-lỗi)
- [📄 Giấy Phép](#-giấy-phép)

---

## ✨ Tính Năng

Bản tin hàng ngày của bạn sẽ bao gồm các module thông tin đa dạng:

- 🗓️ **Lịch Hôm Nay:** Ngày, thứ, tuần ISO và ngày trong năm.  
- 🇻🇳 **Ngày Lễ Việt Nam:** Kiểm tra và thông báo nếu hôm nay là ngày nghỉ lễ chính thức.  
- 🌤️ **Thời tiết & Chỉ số UV:** Dữ liệu thời tiết và chỉ số tia cực tím tại địa điểm được cấu hình, kèm theo khuyến nghị sức khỏe.  
- 💰 **Dữ liệu tài chính:** Tỷ giá USD/VND và giá vàng SJC.  
- 📈 **Giá Tiền Mã Hóa:** Cập nhật giá các đồng coin phổ biến (BTC, ETH, SOL, …).  
- 🛰️ **Vị Trí Trạm ISS:** Hiển thị vị trí hiện tại của Trạm Vũ trụ Quốc tế và dịch ngược ra tên quốc gia/khu vực.  
- 🚀 **Lịch Phóng Tên Lửa:** Thông tin về vụ phóng tên lửa đáng chú ý tiếp theo trên toàn cầu.  
- #️⃣ **Sự Thật Về Con Số:** Một sự thật thú vị liên quan đến một con số ngẫu nhiên (dịch sang tiếng Việt).  
- 💡 **Lời khuyên ngắn:** Một lời khuyên ngẫu nhiên (dịch sang tiếng Việt).  
- 🏛️ **Triết Lý Stoic:** Trích dẫn ngắn từ các nhà Khắc kỷ (dịch sang tiếng Việt).  

---

## ⚙️ Cách Hoạt Động

Dự án sử dụng một workflow duy nhất đặt tại **`.github/workflows/auto-daily-note.yml`**:

1. **Lập lịch:** kích hoạt tự động mỗi ngày lúc **00:05 (ICT)** hoặc chạy thủ công.  
2. **Thực thi Script:** một script Bash chạy trên `ubuntu-latest`, gọi nhiều API công khai.  
3. **Xử lý & Ghi file:** dữ liệu JSON được xử lý bằng `jq`, sau đó ghi vào file **`YYYY-MM-DD.md`** ở thư mục gốc. **Cơ chế đánh dấu** (`<!-- MODULE-ID -->`) đảm bảo mỗi module chỉ thêm **một lần**.  
4. **Commit & Push:** nếu có thay đổi, sẽ tự động commit & push.  
5. **Thông báo Discord:** nếu có commit mới, gửi thông báo tóm tắt qua **Discord Webhook**.

---

## 🛠️ Hướng Dẫn Cài Đặt

### 1) Fork repository

- Nhấn **Fork** để sao chép repo về tài khoản của bạn.  
- Sau khi fork, vào tab **Actions** và nhấn _“I understand my workflows, go ahead and enable them”_ để bật workflow.

### 2) (Bắt buộc) Cấu hình Discord Webhook

- Trong kênh Discord muốn nhận thông báo: **Edit Channel → Integrations → Webhooks → New Webhook**.  
- Đặt tên (ví dụ: `GitHub Bot`) → **Copy Webhook URL**.  
- Trên GitHub repo: **Settings → Secrets and variables → Actions → New repository secret**.  
- **Name:** `DISCORD_WEBHOOK_URL` → **Value:** dán URL webhook → **Save**.

### 3) (Tùy chọn) Sửa địa điểm / tham số

- Mở file `.github/workflows/auto-daily-note.yml`.  
- Sửa biến môi trường trong step “Generate today’s note”:
  - `CITY`: tên hiển thị (ví dụ: `"Hanoi, VN"`).  
  - `LAT`, `LON`: toạ độ dùng cho thời tiết/UV.  
  - Có thể thêm biến khác (API key, ngôn ngữ, danh sách coin, v.v.).

---

## 🎨 Tùy Chỉnh

- **Định dạng file:** Mặc định tạo `YYYY-MM-DD.md`. Có thể đổi tên/thư mục đích.  
- **Ngôn ngữ:** Nội dung mẫu là tiếng Việt; bạn có thể chuyển sang ngôn ngữ khác.  
- **Dịch tự động:** Có thể gọi API dịch.  
- **Thông báo Discord:** Tuỳ chỉnh nội dung payload JSON gửi lên webhook (nhúng, màu sắc, avatar…).

---

## ❓ Hỏi Đáp & Khắc Phục Lỗi

- **Cron giờ lệch?** Lịch GitHub Actions dùng **UTC**. Dòng `5 17 * * *` tương đương **00:05 ICT**.  
- **Commit không xảy ra?** Nếu nội dung không thay đổi, `git status` rỗng → sẽ không commit. Hãy đảm bảo module sinh ra chuỗi mới (ví dụ đính kèm timestamp).  
- **Lỗi YAML (ví dụ “syntax error line X”):** Kiểm tra dấu `:`/dấu `-`/khoảng trắng/indent trong file workflow. YAML rất nhạy cảm với thụt lề.  
- **Webhook không nhận thông báo?** Kiểm tra `DISCORD_WEBHOOK_URL` có tồn tại ở `Actions → Secrets` và log của step gửi webhook.

---

## 📄 Giấy Phép

Phát hành theo giấy phép **MIT**. Xem [`LICENSE`](LICENSE).

---

### 💬 Góp Ý

Mở **Issue**/**Pull Request** để đóng góp tính năng, cải thiện docs, hoặc thêm module mới 🧩.
