import asyncio
import nats

async def main():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Initializing jetstream
    js = nc.jetstream()
    
    # Binding to the existing bucket
    kv = await js.key_value("configs_playgrnd")

    # Creating a watcher to listen for updates
    watch = await kv.watch("site_maintenance")

    # Loop that reacts to key changes
    async for entry in watch:
        if entry.value:
            value = entry.value.decode()
            if value == "true":
                print(f"New Update, Maintenance in progress. [site_maintenance = {value}]")
            else:
                print(f"New Update, Site is now free. [site_maintenance = {value}]")

if __name__ == "__main__":
    asyncio.run(main())