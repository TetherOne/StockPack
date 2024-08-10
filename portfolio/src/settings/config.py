from pydantic import BaseModel


class KafkaConfig(BaseModel):
    KAFKA_HOST: str
    KAFKA_PORT: int
    TOPIC_REG: str
    TOPIC_DEL: str
