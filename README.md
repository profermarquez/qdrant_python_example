# Crear qdrant y levantar localmente

docker build -t qdrant-custom .

Si tenés un archivo docker-compose.yml, simplemente ejecutás:

docker-compose up -d

La API estará disponible en: http://localhost:6333


# Para el CRUDL en Python 

virtualenv env 

.\env\Scripts\activate

pip install qdrant-client

py .\CRUDL-qdrant-python.py
