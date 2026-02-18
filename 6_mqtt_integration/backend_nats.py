import asyncio
import nats

async def callback_handler(msg):
    # Processing and printing the message
    subject = msg.subject
    data = msg.data.decode()
    print(f"Message received on subject {subject}:\n{data}")

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Subscribing to the subject "device.temp" (mapped from MQTT "device/temp")
    sub = await nc.subscribe("device.temp",cb=callback_handler)
    
    # Listener async loop
    print("Listening for MQTT messages on 'device.temp'...")
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())