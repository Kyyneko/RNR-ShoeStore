# Backend Proyek RNR-ShoeStore

## Deskripsi

Proyek ini adalah backend untuk aplikasi e-commerce sepatu. Backend dibangun dengan Flask dan SQLAlchemy, serta menggunakan SQLite sebagai database.

## Instalasi

Untuk menjalankan backend, Anda perlu menginstal beberapa dependensi. Pastikan Anda menggunakan Python 3.6 atau versi yang lebih baru.

1. **Clone Repository**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository

2. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt

3. **Konfigurasi Database**

    Menambahkan Kolom atau Mengubah Struktur Database
    Untuk menambahkan kolom baru atau melakukan perubahan pada struktur tabel, buatlah file migrasi terlebih dahulu :
    ```bash
    python -m flask db migrate -m"Deskripsi Perubahan"
    ```
    Setelah itu, terapkan perubahan ke database :
    ```bash
    python -m flask db upgrade

## Endpoints API

### User Endpoints

- **Register User**
  - **Method**: `POST`
  - **Endpoint**: `/api/users/register`
  - **Body**: JSON dengan `username`, `password`, `email`, `first_name`, `last_name`, `address`, `phone`, `role`
  
- **Login User**
  - **Method**: `POST`
  - **Endpoint**: `/api/users/login`
  - **Body**: JSON dengan `username` dan `password`
  
- **Update Profile**
  - **Method**: `PUT`
  - **Endpoint**: `/api/users/profile/<int:user_id>`
  - **Body**: JSON dengan `username`, `email`, `first_name`, `last_name`, `address`, `phone`, `role`
  
- **Get User by ID**
  - **Method**: `GET`
  - **Endpoint**: `/api/users/<int:user_id>`
  
- **Get All Users**
  - **Method**: `GET`
  - **Endpoint**: `/api/users`
  
- **Delete User**
  - **Method**: `DELETE`
  - **Endpoint**: `/api/users/<int:user_id>`

### Shoes Endpoints

- **Get All Shoes**
  - **Method**: `GET`
  - **Endpoint**: `/api/shoes`
