import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime

def get_pnj_gold_prices_selenium():
    """
    Lấy dữ liệu giá vàng từ PNJ sử dụng Selenium để xử lý JavaScript
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        import time
        
        # Cấu hình Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Chạy ẩn
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        print("🔍 Đang crawl dữ liệu thực từ PNJ...", file=sys.stderr)
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            url = 'https://www.pnj.com.vn/site/gia-vang'
            driver.get(url)
            time.sleep(8)  # Đợi JavaScript load đầy đủ
            
            # Tìm table với class cụ thể đã xác định
            table = driver.find_element(By.CSS_SELECTOR, 'table.w-full.text-left.border-collapse')
            
            if table:
                rows = table.find_elements(By.TAG_NAME, 'tr')
                print(f"✅ Tìm thấy table với {len(rows)} hàng", file=sys.stderr)
                
                if len(rows) > 1:
                    markdown_lines = []
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Thêm header
                    markdown_lines.append(f"# Bảng Giá Vàng PNJ")
                    markdown_lines.append(f"*Cập nhật lúc: {current_time}*")
                    markdown_lines.append("")
                    markdown_lines.append("| Loại Vàng | Giá Mua (1000đ/chỉ) | Giá Bán (1000đ/chỉ) |")
                    markdown_lines.append("|:---|:---:|:---:|")
                    
                    # Parse từng hàng
                    for row in rows[1:]:  # Bỏ qua header
                        cells = row.find_elements(By.TAG_NAME, 'td')
                        if len(cells) >= 3:
                            # Lấy text từ 3 cột đầu tiên
                            col1 = cells[0].text.strip()
                            col2 = cells[1].text.strip() 
                            col3 = cells[2].text.strip()
                            
                            if col1 and col2 and col3:
                                # Làm sạch tên vàng (loại bỏ ký tự đặc biệt)
                                clean_name = col1.replace('|', '').strip()
                                markdown_lines.append(f"| {clean_name} | {col2} | {col3} |")
                    
                    # Thêm footer
                    markdown_lines.append("")
                    markdown_lines.append("---")
                    markdown_lines.append("*Nguồn: https://www.pnj.com.vn/site/gia-vang*")
                    markdown_lines.append("*Crawled với Selenium*")
                    
                    if len(markdown_lines) > 6:  # Có dữ liệu thực
                        print(f"✅ Crawl thành công {len(rows)-1} loại vàng", file=sys.stderr)
                        return "\n".join(markdown_lines)
            
            print("❌ Không tìm thấy dữ liệu trong table", file=sys.stderr)
            return ""
            
        finally:
            driver.quit()
            
    except ImportError:
        print("❌ Selenium chưa được cài đặt. Cài đặt bằng: pip install selenium", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"❌ Lỗi khi crawl dữ liệu: {e}", file=sys.stderr)
        return ""

def get_pnj_gold_prices():
    """
    Lấy dữ liệu giá vàng từ website PNJ - CHỈ crawl dữ liệu thực
    """
    # Sử dụng Selenium để crawl dữ liệu thực
    selenium_result = get_pnj_gold_prices_selenium()
    if selenium_result:
        return selenium_result
    
    # Nếu Selenium không hoạt động, báo lỗi thay vì dùng demo
    print("❌ Không thể crawl dữ liệu thực từ PNJ", file=sys.stderr)
    print("💡 Hãy đảm bảo:", file=sys.stderr)
    print("   - Selenium đã được cài đặt: pip install selenium", file=sys.stderr)
    print("   - Chrome browser đã được cài đặt", file=sys.stderr)
    print("   - Kết nối internet ổn định", file=sys.stderr)
    
    return ""


if __name__ == "__main__":
    # Tên file output được truyền từ command line
    output_filename = sys.argv[1] if len(sys.argv) > 1 else "pnj_gold_prices.md"
    
    markdown_content = get_pnj_gold_prices()
    
    if markdown_content:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✅ Đã lưu bảng giá vàng PNJ vào file: {output_filename}")
    else:
        print("❌ Không thể crawl dữ liệu. Không tạo file output.")
        sys.exit(1)
