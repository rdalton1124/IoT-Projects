from aiocoap import * 
import aiocoap.resource as resource
import asyncio 
import os 
import glob 
import time 

'''
    The CoAP server file. 
    This runs on the Raspberry Pi. 
    The theromemeter writes to a specific file.
    This program periodically checks the file and 
    returns a formatted temperature. 
'''

#set up thermometer device.  
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir +'28*')[0]
device_file = device_folder + '/w1_slave'

#reads the information directly from the device
def read_temp_raw(): 
    f = open(device_file, 'r') #open the file for reading
    lines = f.readlines() #read from the file
    f.close() #close
    return lines
def read(): 
    lines = read_temp_raw()
    #file will end in YES when temp has been read
    while lines[0].strip()[-3:] != 'YES': #if not yes, wait and try again
        time.sleep(.2) 
        lines = read_temp_raw()
    pos = lines[1].find('t=') #'t=' precedes the temperature. 
    if pos != -1: #if found 
        temp_str = lines[1][pos+2:]
        #format temperature 
        return float(temp_str) / 1000
    else:
        return -1
#temperature resource. 
class temp(resource.Resource):
    async def render_get(self, request):
        tmp = read( )#read the temperature. 
        payload = "".join(str(tmp)).encode('utf8') #payload is the temperature, encodeded in utf-8
        return Message(payload = payload) #Message is a message, payload is the content of the message

#a test resource we made before the actual resource. 
class hello(resource.Resource): 
    async def render_get(self, request):
        txt = "hello world"
        payload = "".join(txt).encode('utf8')
        return Message(payload = payload)
async def main(): 
    root = resource.Site()
    root.add_resource(['default'], hello()) #add the test resource, called efault. 
    root.add_resource(['temp'], temp()) #add the temperature resource, called temp. 
    await Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()
asyncio.run(main()) # run indefinitely. 
