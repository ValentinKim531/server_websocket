# Используйте официальный образ Python в качестве базового образа
FROM python:3.10

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы requirements.txt и server.py в рабочую директорию
COPY requirements.txt .
COPY server.py .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы в рабочую директорию
COPY . .

# Откройте порт, на котором будет работать сервер
EXPOSE 8000

# Запустите сервер
CMD ["python", "server.py"]
