# Context 
  - This is an upload of 2 projects I worked on for CSCI 433: Intro to Internet of Things in Spring 2023. 
  - I completed these assignments with a classmate, named Prince.
  - The assignments had specific programs which we were tasked with making. 
  - These assignments were done on a Raspberry Pi, and utilized simple circuits created on a breadboard connected to the Pi via
  GPIO ports. 
  - They're all done in Python. There's no particular reason for this. 

# Format 
  - Each project is in its own folder, with one or multiple sub folders
  - Code: has the code for the project 
  - Demo Videos: Has videos demonstrating the project, as required by the professor
  - Circuit diagrams: diagram of the circuit 
  - Project 2 also has a screenshot of Wireshark, as was required by the project. 

# Project 1
  - Beginning project, intended to get us familiar with the class.
  - Step 1 was only for Arduino users, so we weren't required to do it. 
  - Step 2 involved controlling 2 LEDs via two buttons. 
    - 1 button was to change the behavior of the LED and the other was to change which LED's behavior changed
    - One LED was to blink at varying speeds. Pushing the button would lock it into the current speed, or let it go back to changing if already locked. 
    - One LED was to change brightnesses, using Pulse Width Modulation (PWM). 
  - Step 3 has been ommitted, because it involved closely following a tutorial. 

# Project 2
  - An intro to CoAP project, intended to get us familiar with CoAP, a lightweight network protocol often used by IoT Nodes. 
  - We used the aiocoap library, which was one of the libraries recommended to use by the professors. 
  - The purpose of this was to take a temperature and relay a message containing the temperature over the network. 
  - There is an aioclient.py and an aiosrvr.py for the client and server, respectively. 
    - The aioclient only exists to connect to the server. 
    - The server is run on the raspberrypi. 
