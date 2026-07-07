<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
    Hệ thống Quản lý Nhân sự - Chấm công - Tính lương trên Odoo 15
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 📖 1. Giới thiệu
Đây là đồ án xây dựng hệ thống **Quản lý nhân sự, chấm công và tính lương** trên nền tảng **Odoo 15**.

Hệ thống được phát triển bằng Python và XML theo kiến trúc module của Odoo.

---

## 🔧 2. Các công nghệ được sử dụng
<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
### Cơ sở dữ liệu
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>
# Chức năng chính

## 1. Quản lý nhân sự

- Thêm nhân viên
- Sửa thông tin nhân viên
- Xóa nhân viên
- Tìm kiếm nhân viên
- Quản lý thông tin cá nhân
- Mã định danh nhân viên

---

## 2. Quản lý chấm công

- Chấm công theo ngày
- Quản lý bảng chấm công tháng
- Tự động thống kê:
  - Số công
  - Số ngày vắng
  - Số ngày nghỉ phép
- Chốt công

---

## 3. Tính lương

- Quản lý lương cơ bản
- Quản lý hợp đồng lao động
- Quản lý tham số lương
- Tính lương theo số công
- Tính phụ cấp
- Tính BHXH
- Tính BHYT
- Tính BHTN
- Tính tổng bảo hiểm
- Tính lương thực nhận

---

## 4. Phiếu lương

- Tự động sinh phiếu lương từ bảng lương
- Xem chi tiết phiếu lương
- Lưu lịch sử phiếu lương

---

## 5. Đơn từ

- Tạo đơn
- Duyệt đơn
- Từ chối đơn
- Theo dõi trạng thái

---

# Kiến trúc hệ thống

```
Quản lý nhân sự
        │
        ▼
   Chấm công
        │
        ▼
 Bảng chấm công
        │
        ▼
   Tính lương
        │
        ▼
  Bảng lương
        │
        ▼
  Phiếu lương
```

---

# Cấu trúc project

```
DoAn_Odoo
│
├── nhan_su
│   ├── models
│   ├── views
│   ├── security
│   └── __manifest__.py
│
├── quan_ly_cham_cong
│   ├── models
│   ├── views
│   ├── security
│   └── __manifest__.py
│
├── tinh_luong
│   ├── models
│   ├── views
│   ├── security
│   └── __manifest__.py
│
└── README.md
```

---

# Luồng xử lý

```
Nhân viên
      │
      ▼
Chấm công hàng ngày
      │
      ▼
Bảng chấm công tháng
      │
      ▼
Tính lương
      │
      ▼
Sinh bảng lương
      │
      ▼
Sinh phiếu lương
```

---

## ⚙️ 4. Cài đặt

### 4.1. Cài đặt công cụ, môi trường và các thư viện cần thiết

#### 4.1.1. Tải project

Clone project từ GitHub:

```bash
git clone https://github.com/DOTHANHTU70/HN-QTDN-17-03-N14.git
```

Di chuyển vào thư mục project:

```bash
cd HN-QTDN-17-03-N14
```

---

#### 4.1.2. Cài đặt các thư viện cần thiết

Thực thi các lệnh sau:

```bash
sudo apt-get install libxml2-dev \
libxslt-dev \
libldap2-dev \
libsasl2-dev \
libssl-dev \
python3.10-distutils \
python3.10-dev \
build-essential \
libffi-dev \
zlib1g-dev \
python3.10-venv \
libpq-dev
```

---

#### 4.1.3. Khởi tạo môi trường ảo

Khởi tạo Virtual Environment

```bash
python3.10 -m venv ./venv
```

Kích hoạt môi trường

```bash
source venv/bin/activate
```

Cài đặt các thư viện của project

```bash
pip3 install -r requirements.txt
```

---

### 4.2. Setup Database

Khởi tạo cơ sở dữ liệu PostgreSQL bằng Docker.

```bash
sudo docker-compose up -d
```

Kiểm tra container

```bash
docker ps
```

Nếu container đã tồn tại nhưng đang dừng:

```bash
docker start postgres_odoo-base
```

---

### 4.3. Setup tham số chạy hệ thống

Tạo file `odoo.conf`

```ini
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5431
xmlrpc_port = 8069
```

Có thể kế thừa từ file:

```text
odoo.conf.template
```

---

### 4.4. Chạy hệ thống

Kích hoạt môi trường ảo

```bash
source venv/bin/activate
```

Chạy Odoo

```bash
python3 odoo-bin -c odoo.conf -u all
```

---

### 4.5. Truy cập hệ thống

Sau khi khởi động thành công, mở trình duyệt và truy cập:

```text
http://localhost:8069
```

Đăng nhập bằng tài khoản quản trị để sử dụng hệ thống.

## 📄 License

© 2024 AIoTLab, Faculty of Information Technology, DaiNam University. All rights reserved.
