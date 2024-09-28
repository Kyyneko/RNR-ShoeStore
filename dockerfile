# Gunakan image Python sebagai base
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/requirements.txt

# Install dependencies yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh folder aplikasi ke dalam container
COPY . /app

# Expose port yang digunakan Flask (5000)
EXPOSE 5000

# Menjalankan aplikasi Flask
CMD ["python", "app.py"]
