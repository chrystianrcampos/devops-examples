from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    "teste",
    bootstrap_servers=["172.17.0.1:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id="kafka",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
for message in consumer:
    print(f"Mensagem recebida: {message.value}")
    consumer.commit()
