import pika
from pika.adapters.blocking_connection import BlockingChannel
from persona_sync_pylib.utils.environment import QUEUE_NAME, RABBIT_HOST, RABBIT_PORT


class Consumer:
    def __init__(self) -> None:
        self.__channel = self.__init_channel()

    def start_listening(self) -> None:
        self.__channel.start_consuming()

    def stop_listening(self) -> None:
        self.__channel.stop_consuming()
        self.__channel.close()

    def __init_channel(self) -> BlockingChannel:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT)
        )
        channel = connection.channel()

        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue=QUEUE_NAME, on_message_callback=self.message_processor
        )

        return channel

    def message_processor(self, ch, method, _properties, body):
        pass
