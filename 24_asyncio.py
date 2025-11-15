# =================================================================
# Asyncio in Python

# To write concurrent code using async and await,
# allowing your program to handle many I/O tasks
# (network, API calls, file I/O, etc.) without blocking execution.
# =================================================================

# ============================================
# 1. Sequential (Normal / Synchronous) Blocking Execution
# ============================================


# import time

# print("=" * 40, "\n")
# print("Code 1")


# def download_file(file_number):
#     print(f"Starting download {file_number}")
#     time.sleep(1)
#     print(f"Completed download {file_number}")


# start = time.time()

# download_file(1)
# download_file(2)
# download_file(3)

# end = time.time()
# print(f"Total time taken: {end - start:.2f} seconds")
# print("\n" + "=" * 40)

# ============================================
# 2. Asynchronous Version using asyncio
# ============================================


# import asyncio
# import time

# print("=" * 40, "\n")
# print("Code 2")


# async def download_file(file_number):
#     print(f"Starting download {file_number}")
#     await asyncio.sleep(1)
#     print(f"Completed download {file_number}")


# async def main():
#     start = time.time()

#     # Run tasks concurrently
#     task1 = asyncio.create_task(download_file(1))
#     task2 = asyncio.create_task(download_file(2))
#     task3 = asyncio.create_task(download_file(3))

#     await task1
#     await task2
#     await task3

#     end = time.time()
#     print(f"Total time taken: {end - start:.2f} seconds")


# asyncio.run(main())
# print("\n" + "=" * 40)


# ============================================
# 3. Running Multiple Tasks with asyncio.gather()
# ============================================

# import asyncio
# import time

# print("=" * 40, "\n")
# print("Code 3")


# async def download_file(file_number):
#     print(f"Downloading file-{file_number}...")
#     await asyncio.sleep(1)
#     print(f"File-{file_number} downloaded!")


# async def main():
#     start = time.time()

#     # Run all tasks together
#     await asyncio.gather(
#         download_file(1),
#         download_file(2),
#         download_file(3),
#     )

#     end = time.time()
#     print(f"All downloads completed in {end - start:.2f} seconds")


# asyncio.run(main())
# print("\n" + "=" * 40)


# ============================================
# 4. Returning Values from Coroutines
# ============================================

# import asyncio

# print("=" * 40, "\n")
# print("Code 4")


# async def fetch_data(n):
#     print(f"Fetching data {n}")
#     await asyncio.sleep(1)
#     return f"Data-{n}"


# async def main():
#     results = await asyncio.gather(
#         fetch_data(1),
#         fetch_data(2),
#         fetch_data(3),
#     )
#     print("Fetched results:", results)


# asyncio.run(main())
# print("\n" + "=" * 40)


# ============================================
# 5. Running Blocking Code inside Async
# ============================================

# import asyncio
# import time

# print("=" * 40, "\n")
# print("Code 5")


# def blocking_task():
#     print("Blocking task started")
#     time.sleep(1)
#     print("Blocking task finished")


# async def non_blocking_task():
#     print("Non Blocking task started")
#     await asyncio.sleep(1)
#     print("Non Blocking task finished")


# async def main():
#     start = time.time()
#     print("Starting main coroutine")

#     loop = asyncio.get_running_loop()
#     # Run blocking code in a separate thread
#     await loop.run_in_executor(None, blocking_task)
#     await asyncio.create_task(non_blocking_task())

#     print("Main coroutine continues after blocking task")
#     end = time.time()
#     print(f"Total time taken: {end - start:.2f} seconds")


# asyncio.run(main())
# print("\n" + "=" * 40)


# ============================================
# 6. Using asyncio with async for / async with
# ============================================

# import asyncio

# print("=" * 40, "\n")
# print("Code 6")


# async def countdown():
#     for i in range(3, 0, -1):  # [3, 2, 1]
#         await asyncio.sleep(1)
#         yield i


# async def main():
#     async for value in countdown():
#         print("Count:", value)


# asyncio.run(main())
# print("\n" + "=" * 40)


# ============================================
# 7. async context manager (async with)
# ============================================

import asyncio

print("=" * 40, "\n")
print("Code 7")


class AsyncManager:
    async def __aenter__(self):
        print("Entering context...")
        await asyncio.sleep(1)
        return "Resource"

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")
        await asyncio.sleep(1)


async def main():
    async with AsyncManager() as res:
        print("Using", res)


asyncio.run(main())
print("\n" + "=" * 40)
