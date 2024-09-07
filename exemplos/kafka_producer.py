from kafka import KafkaProducer
import json


producer = KafkaProducer(
    bootstrap_servers=["172.17.0.1:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)
for i in range(1, 10):
    print(f"Enviando mensagem {i}")
    future = producer.send("teste", {"index": i})
    result = future.get(timeout=60)
    producer.flush()
