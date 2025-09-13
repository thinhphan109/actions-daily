import requests
from bs4 import BeautifulSoup
import sys

def get_pnj_gold_prices():
    """
    Lấy dữ liệu giá vàng từ website PNJ và trả về dưới dạng bảng Markdown.
    """
    url = 'https://www.pnj.com.vn/blog/gia-vang'
    markdown_lines = []

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        div_container = soup.find('div', class_='bang-gia-vang-outer')

        if not div_container:
            return ""

        table = div_container.find('table')
        if not table:
            return ""
            
        # Thêm tiêu đề và định dạng bảng Markdown
        markdown_lines.append("| Loại Vàng | Mua vào (nghìnđ/chỉ) | Bán ra (nghìnđ/chỉ) |")
        markdown_lines.append("|:---|:---:|:---:|")

        rows = table.find_all('tr')
        # Bỏ qua hàng đầu tiên (header của bảng gốc)
        for row in rows[1:]:
            cols = [col.text.strip() for col in row.find_all('td')]
            if len(cols) == 3:
                # Định dạng lại hàng cho bảng Markdown
                markdown_lines.append(f"| {cols[0]} | {cols[1]} | {cols[2]} |")
        
        return "\n".join(markdown_lines)

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy dữ liệu PNJ: {e}", file=sys.stderr)
        return f""

if __name__ == "__main__":
    # Tên file output được truyền từ command line
    output_filename = sys.argv[1] if len(sys.argv) > 1 else "pnj_gold_prices.md"
    
    markdown_table = get_pnj_gold_prices()
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_table)
    
    print(f"Đã lưu bảng giá vàng PNJ vào file: {output_filename}")
