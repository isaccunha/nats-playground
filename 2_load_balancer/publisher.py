import asyncio
import nats

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Publishing 30 test messages
    for i in range(0,30):
        log = f'log {i} message'
        await nc.publish("logs.process",log.encode())

    # Making sure all published messages have reached the server
    await nc.flush()

    # Closing NATS connection
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())