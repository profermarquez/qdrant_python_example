from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from qdrant_client.models import PointIdsList  # Importar PointIdsList

# Conectar al servicio local
client = QdrantClient(host="localhost", port=6333,check_compatibility=False)


# 1. Crear colección 'clientes' (si no existe)
collection_name = "clientes"
vector_size = 4  # Usamos vectores pequeños para simplicidad

if client.collection_exists(collection_name):
    client.delete_collection(collection_name=collection_name)

client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
)

# 2. Insertar (Create) puntos
print("✅ Insertando cliente...")
client.upsert(
    collection_name=collection_name,
    points=[
        PointStruct(
            id=1,
            vector=[0.1, 0.2, 0.3, 0.4],
            payload={"nombre": "Ana", "email": "ana@email.com"}
        )
    ]
)

# 3. Leer (Read) por ID
print("\n📄 Leyendo cliente ID=1...")
result = client.retrieve(collection_name=collection_name, ids=[1])
print(result)

# 4. Actualizar (Update) payload
print("\n✏️ Actualizando email del cliente...")
client.set_payload(
    collection_name=collection_name,
    payload={"email": "ana.actualizado@email.com"},
    points=[1]
)

# Leer de nuevo para verificar
updated = client.retrieve(collection_name=collection_name, ids=[1])
print(updated)

# 5. Listar (List) usando filtro
print("\n📋 Listando clientes con nombre = Ana...")
filtro = Filter(
    must=[FieldCondition(key="nombre", match=MatchValue(value="Ana"))]
)

search_results = client.scroll(
    collection_name=collection_name,
    limit=10,
    scroll_filter=filtro
)
print(search_results[0])  # Solo mostramos los puntos, no el offset

# 6. Borrar (Delete)
print("\n🗑️ Borrando cliente ID=1...")

client.delete(
    collection_name=collection_name,
    points_selector=PointIdsList(points=[1])  # Usar PointIdsList en lugar de PointsSelector
)
# Verificamos que se haya borrado
final_check = client.retrieve(collection_name=collection_name, ids=[1])
print("Resultado tras borrar:", final_check)