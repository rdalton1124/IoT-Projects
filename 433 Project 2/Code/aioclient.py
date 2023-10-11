from aiocoap import *
import asyncio
import time

'''
    The CoAP client file. 
    Ran off of a laptop which connects to the 
    Raspberry Pi. 
'''

async def  main():
    protocol = await Context.create_client_context()
    for i in range(10):
        msg = Message(code=GET, uri="coap://192.168.197.140/temp") #this was the local IP of the Raspberry Pi.
        res = await protocol.request(msg).response #await resposne from the Pi. 
        print(res.payload.decode('utf8')) #decode response
        time.sleep(1) #wait. 

asyncio.run(main()) #run indefinitely. 

