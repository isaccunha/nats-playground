import asyncio
import nats
from random import randrange
import json

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Choosing two random numbers to sum
    x = randrange(100)
    y = randrange(100)
    payload = {
        "x": x,
        "y": y
    }
    payload_json = json.dumps(payload).encode()
    print(f"Requesting the sum of {x} and {y}")
    
    # Requesting the sum from the server and printing the result
    rep = await nc.request("math.sum",payload_json, timeout=5)
    print("Received result: "+ rep.data.decode())

    # Cleaning the connection before closing it
    await nc.flush()

    # Closing NATS connection
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())