# imagen base de Python
FROM python:3.9-slim

# directorio de trabajo
WORKDIR /app

# Copiar requirements primero para cache de Docker
COPY requirements.txt .

# dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY src/ ./src/

# puerto
EXPOSE 5000

# Variables de entorno
ENV PYTHONPATH=/app
ENV FLASK_APP=src/app.py
ENV ENVIRONMENT=production

# Comando para ejecutar la aplicación
CMD ["python", "src/app.py"]
