import asyncio
import nats
import json

async def sum_response(msg):
    # Processing the request data and responding with the sum
    data = json.loads(msg.data.decode())
    reply = data["x"]+data["y"]
    print(f"Sum of {data['x']} and {data['y']} requested. Responding {reply}.")
    await msg.respond(str(reply).encode())


async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Subscribing to the subject "math.sum" and defining a function to respond to the messages
    sub = await nc.subscribe("math.sum", cb=sum_response)

    # Listener async loop
    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())