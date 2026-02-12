import asyncio
import nats
import os
from multiprocessing import Process

async def message_handler(msg):
    # Getting published messages data and printing it
    subject = msg.subject
    data = msg.data.decode()
    print(f"Process {os.getpid()} received a log on {subject}: {data}")

async def run_worker_node():
    # Connecting to NATS
    nc = await nats.connect("demo.nats.io")

    # Subscribing to the subject "logs.process" and defining a function to handle the messages
    sub = await nc.subscribe("logs.process",queue="log_workers", cb=message_handler)

    # Listener async loop
    while True:
        await asyncio.sleep(1)

def main():
    asyncio.run(run_worker_node())

if __name__ == '__main__':
    # Creating three process to show the load balancing
    p1 = Process(target=main)
    p2 = Process(target=main)
    p3 = Process(target=main)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()