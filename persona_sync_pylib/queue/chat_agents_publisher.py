from typing import Union
import pika

from persona_sync_pylib.utils.prompt_inputs import (
    QueueRequest,
    StateMachineQueueRequest,
)
from persona_sync_pylib.utils.environment import RABBIT_HOST, RABBIT_PORT, QUEUE_NAME
from persona_sync_pylib.utils.logger import Logger, LogLevel


def publish_message(message: Union[QueueRequest, StateMachineQueueRequest]) -> bool:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT)
    )
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    try:
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=message.model_dump_json(),
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
    except Exception as e:
        Logger().log(LogLevel.ERROR, f"Failed to publish message: {e}")
        return False

    connection.close()
    return True
