# Imagen base
FROM python:3.11-slim

# Instalamos Apache + mod_wsgi
RUN apt-get update && \
    apt-get install -y apache2 apache2-dev libapache2-mod-wsgi-py3 && \
    rm -rf /var/lib/apt/lists/*

# Creamos directorio de la app
WORKDIR /var/www/html/app

# Copiamos requirements.txt e instalamos dependencias
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY app/ /var/www/html/app/

# Copiamos archivo wsgi.py al nivel superior (fuera de /app)
COPY wsgi.py /var/www/html/wsgi.py

# Copiamos configuración de Apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Habilitamos mod_wsgi
RUN a2enmod wsgi

# Exponemos puerto HTTP
EXPOSE 80

# Levantamos Apache en primer plano
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]