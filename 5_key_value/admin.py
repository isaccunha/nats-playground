import asyncio
import nats

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Initializing jetstream
    js = nc.jetstream()

    # Creating a KV bucket
    kv = await js.create_key_value(bucket="configs_playgrnd")

    entry = True
    # Loop that toggles the key state every 10 seconds
    while True:
        if entry:
            print("Setting the key as false")
            await kv.put('site_maintenance',b'false')
            entry = False
        else:
            print("Setting the key as true")
            await kv.put('site_maintenance',b'true')
            entry = True
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())