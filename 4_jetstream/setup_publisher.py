import asyncio
import nats
from datetime import datetime

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")
    
    # Initializing jetstream
    js = nc.jetstream()

    # Defining and creating the stream configuration
    await js.add_stream(name="playgrnd_stream",subjects=["stream.stored"], storage="memory")

    # Publishing a persistent message to the stream
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    day = now.strftime("%d/%m/%y")
    payload = f'Message stored at {time} on day {day}'.encode()
    await js.publish("stream.stored",payload)
    print(await js.streams_info(),"\n")

    # Cleaning the connection before closing it
    await nc.flush()

    # Closing NATS connection
    await nc.close()

if __name__ == "__main__":
    asyncio.run(main())