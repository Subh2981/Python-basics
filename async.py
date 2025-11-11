import time
import asyncio




async def function1():
    asyncio.sleep(1)
    print("func 1")
    
async def function2():
    asyncio.sleep(1)
    print("func 2")
    
async def function3():
    asyncio.sleep(4)
    print("func 3")
async def main():   
    # task=asyncio.create_task(function1()) 
    # await  function1()
    # await  function2()
    # await  function3()    
    task=asyncio.gather(
      function1(),
      function2(),
      function3() )
    
#asyncio.run(main())
    print(task)
