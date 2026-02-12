import asyncio
import nats

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Subscribing to the subject "hello"
    sub = await nc.subscribe("hello")

    # Publishing a message to "hello"
    await nc.publish("hello",b'Hello World!')

    # Processing and printing the received message
    msg = await sub.next_msg()
    print("Received: ", msg)

    # Making sure all published messages have reached the server
    await nc.flush()

    # Closing NATS connection
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())