import asyncio

async def download(name):
    print(f"Downloading {name}...")
    await asyncio.sleep(1)

async def main():
    tasks = ["dataset1", "dataset2", "dataset3"]
    await asyncio.gather(*(download(t) for t in tasks))
    print("All downloads complete.")

asyncio.run(main())