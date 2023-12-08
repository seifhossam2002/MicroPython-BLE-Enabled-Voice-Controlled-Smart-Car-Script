Overview: 
This MicroPython script has been crafted for a microcontroller embedded in a smart car, 
leveraging Bluetooth Low Energy (BLE) for communication. The script facilitates voice
controlled commands from a connected smartphone, directing the car to move forward, 
backward, left, right, or stop. The smart car features LED indicators providing visual 
feedback for left, right, and stop commands. Additionally, infrared sensors detect 
obstacles, causing the car to halt and subsequently resume executing commands once 
the obstacle is cleared. 


1. BLE Advertising Payloads: 
The script commences with a module (ble_advertising.py) designed for generating BLE 
advertising payloads. These payloads include essential information about the smart car, 
establishing a connection with external devices such as smartphones.


3. BLE Simple Peripheral: 
The ble_simple_peripheral.py module introduces a class (BLESimplePeripheral) responsible 
for managing BLE communication. This class oversees BLE events, sets up a UART service 
for bidirectional communication, and serves as the backbone for connecting the 
microcontroller with a smartphone.


5. UART Peripheral for BLE: 
The script showcases a UART peripheral using the BLESimplePeripheral class. It defines 
UUIDs for UART service, handles BLE events, and facilitates the exchange of data over 
UART. This establishes a seamless communication channel between the smart car's 
microcontroller and a smartphone.


7. Motor Control and Sensor Handling: 
The core functionality is embedded in the main.py script, focusing on motor control and 
sensor handling. Components include LED indicators, motors, a buzzer, and two infrared 
sensors. Specific motor control functions respond to voice commands received over BLE, 
allowing the smart car to move forward, backward, left, right, or stop. LED indicators 
provide visual cues for left, right, and stop commands. The script also incorporates 
sensor handling, causing the car to pause when obstacles are detected by the infrared 
sensors. Once the obstacle is removed, the car resumes executing the last command.


9. Voice-Controlled Operation: 
The script introduces voice-controlled operations, enabling users to dictate commands 
to the smart car via a connected smartphone. Voice commands initiate corresponding 
motor control actions, providing a hands-free and intuitive mode of operation.


11. Main Program Execution: 
The main program initializes the hardware, including GPIO pins for LEDs, motors, the 
buzzer, and infrared sensors. It continuously monitors for BLE connections, interprets 
received voice commands through the on_rx callback, and updates motor control and 
sensor handling accordingly. A delay in the main loop optimizes resource usage.

This script offers a robust foundation for a BLE-enabled voice-controlled smart car, combining 
motor control, LED indicators, and obstacle detection for an interactive and user-friendly 
experience.
