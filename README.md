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

- **Add Shoe Detail**
  - **Method**: `POST`
  - **Endpoint**: `/api/shoes`
  - **Body**: JSON dengan `category_id`, `shoe_name`, `shoe_price`, `shoe_size`, `stock`

- **Update Shoe Detail**
  - **Method**: `PUT`
  - **Endpoint**: `/api/shoes/<int:shoe_detail_id>`
  - **Body**: JSON dengan `category_id` (opsional), `shoe_name` (opsional), `shoe_price` (opsional), `shoe_size` (opsional), `stock` (opsional)

- **Delete Shoe Detail**
  - **Method**: `DELETE`
  - **Endpoint**: `/api/shoes/<int:shoe_detail_id>`

- **Get Shoe Detail by ID**
  - **Method**: `GET`
  - **Endpoint**: `/api/shoes/<int:shoe_detail_id>`

- **Get All Shoes**
  - **Method**: `GET`
  - **Endpoint**: `/api/shoes`

### Categories Endpoints

- **Add Category**
  - **Method**: `POST`
  - **Endpoint**: `/api/categories`
  - **Body**: JSON dengan `category_name`

- **Update Category**
  - **Method**: `PUT`
  - **Endpoint**: `/api/categories/<int:category_id>`
  - **Body**: JSON dengan `category_name` (opsional)

- **Delete Category**
  - **Method**: `DELETE`
  - **Endpoint**: `/api/categories/<int:category_id>`

- **Get Category by ID**
  - **Method**: `GET`
  - **Endpoint**: `/api/categories/<int:category_id>`

- **Get All Categories**
  - **Method**: `GET`
  - **Endpoint**: `/api/categories`

### Orders Endpoints

- **Create Order**
  - **Method**: `POST`
  - **Endpoint**: `/api/orders`
  - **Body**: JSON dengan `user_id`, `shoe_detail_id`, `order_date` (format YYYY-MM-DD), `amount`, dan `order_status`

- **Cancel Order**
  - **Method**: `DELETE`
  - **Endpoint**: `/api/orders/<int:order_id>`

- **Update Order Status**
  - **Method**: `PUT`
  - **Endpoint**: `/api/orders/<int:order_id>`
  - **Body**: JSON dengan `order_status` (opsional)

- **Get Order by ID**
  - **Method**: `GET`
  - **Endpoint**: `/api/orders/<int:order_id>`

- **Get All Orders**
  - **Method**: `GET`
  - **Endpoint**: `/api/orders`

### Payments Endpoints

- **Process Payment**
  - **Method**: `POST`
  - **Endpoint**: `/api/payments`
  - **Body**: JSON dengan `order_id`, `payment_method`, `payment_status`, dan `payment_date` (format YYYY-MM-DD)

- **Update Payment Status**
  - **Method**: `PUT`
  - **Endpoint**: `/api/payments/<int:payment_id>`

- **Get Payment by ID**
  - **Method**: `GET`
  - **Endpoint**: `/api/payments/<int:payment_id>`

- **Get All Payments**
  - **Method**: `GET`
  - **Endpoint**: `/api/payments`

- **Delete Payment**
  - **Method**: `DELETE`
  - **Endpoint**: `/api/payments/<int:payment_id>`

### Gallery Endpoints

- **Add Image**
  - **Method**: `POST`
  - **Endpoint**: `/api/gallery`
  - **Body**: JSON dengan `shoe_detail_id` dan `image_url`

- **Update Image**
  - **Method**: `PUT`
  - **Endpoint**: `/api/gallery/<int:gallery_id>`
  - **Body**: JSON dengan `shoe_detail_id` (opsional) dan `image_url` (opsional)

- **Remove Image**
  - **Method**: `DELETE`
  - **Endpoint**: `/api/gallery/<int:gallery_id>`

- **Get Image by ID**
  - **Method**: `GET`
  - **Endpoint**: `/api/gallery/<int:gallery_id>`

- **Get All Images**
  - **Method**: `GET`
  - **Endpoint**: `/api/gallery`






