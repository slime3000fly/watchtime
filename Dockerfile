# Użyj obrazu bazowego
FROM postgres:latest

# Zdefiniuj zmienną środowiskową POSTGRES_DB
ENV POSTGRES_DB watch_time_db

# Zdefiniuj zmienną środowiskową POSTGRES_USER
ENV POSTGRES_USER admin

# Zdefiniuj zmienną środowiskową POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD admin

# Kopiuj plik SQL init.sql do katalogu /docker-entrypoint-initdb.d/
COPY init.sql /docker-entrypoint-initdb.d/
