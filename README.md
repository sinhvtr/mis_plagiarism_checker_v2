# 🔍 Tool Kiểm Tra Mức Độ Trùng Lặp - ITDE BAV

Công cụ hỗ trợ kiểm tra mức độ trùng lặp giữa các bài nộp của sinh viên, sử dụng tại Học viện Ngân hàng - Khoa CNTT & Kinh tế số (ITDE BAV).

## 🚀 Cài đặt

Trước tiên, cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt

## 📁 Chuẩn Bị Dữ Liệu

Tổ chức các file bài nộp theo cấu trúc thư mục:

data/
└── data_original/
    └── [Năm học]/
        └── [Học kỳ]/
            └── [Tên giảng viên]/
                └── [Tên lớp]/
                    └── [Các file bài nộp của sinh viên]

Ví dụ:

data/
└── data_original/
    └── 2024-2025/
        └── HK2/
            └── NguyenVanA/
                └── D15CQCN01-N/
                    ├── 25A4011234.docx
                    ├── 25A4015678.pdf
                    └── ...

##🧾 Chuyển Đổi File Word/PDF Sang Text

Chạy script word2txt.py để chuyển đổi các file .docx và .pdf sang định dạng .txt:

```bash
python word2txt.py

## 🔎 Kiểm Tra Trùng Lặp

Sau khi đã có các file .txt, chạy script plagiarism_detector.py để kiểm tra mức độ trùng lặp:
```bash
python plagiarism_detector.py

## 📊 Kết Quả

Sau khi chạy xong, bạn sẽ nhận được file output.csv chứa thông tin mức độ trùng lặp giữa các cặp bài nộp.

Bạn có thể mở file này bằng Excel hoặc phần mềm bảng tính khác để sắp xếp, lọc và xử lý theo nhu cầu.
