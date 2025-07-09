FROM qdrant/qdrant:v1.9.3

# Establecemos el directorio de trabajo
WORKDIR /qdrant

# Copiamos archivos personalizados (opcional)
# Ej: configuración, scripts de inicialización
# COPY ./config.yaml ./config.yaml
# COPY ./init.sh ./init.sh

# Instalamos herramientas opcionales (por ejemplo: curl, bash)
RUN apt-get update && \
    apt-get install -y curl bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Exponemos el puerto por defecto
EXPOSE 6333

# Comando por defecto (se puede sobrescribir en docker-compose)
CMD ["/qdrant/qdrant"]
