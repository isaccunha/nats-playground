import asyncio
import nats
from nats.errors import TimeoutError

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Initializing jetstream
    js = nc.jetstream()

    # Creating a durable subscription to the stream
    sub = await js.subscribe("stream.stored", stream="playgrnd_stream", durable="durable_consumer")
    print("Waiting for messages...")

    # Processing pending messages from the stream
    while True:
        try:
            # Processing the message and acknowledging receipt
            msg = await sub.next_msg(timeout=5)
            print(f"Message Received: {msg.data.decode()}")
            await msg.ack()
        except TimeoutError:
            print("No new messages... Disconnecting")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    # Closing NATS connection
    await nc.close()

if __name__ == "__main__":
    asyncio.run(main())