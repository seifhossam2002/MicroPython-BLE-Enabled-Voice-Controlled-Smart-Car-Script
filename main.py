# Import necessary modules
from machine import Pin

import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
import utime


red_led1 = Pin(15, Pin.OUT)
red_led2 = Pin(17, Pin.OUT)
yellow_led1 = Pin(3, Pin.OUT)
yellow_led2 = Pin(16, Pin.OUT)
buzzer = Pin(0, Pin.OUT)
infrared_sensor_forward = Pin(28, Pin.IN)
infrared_sensor_backward = Pin(12, Pin.IN)

# Motor sensors
backward_enableA = Pin(27, Pin.OUT)
backward_input1 = Pin(26, Pin.OUT)
backward_input2 = Pin(22, Pin.OUT)
backward_input3 = Pin(21, Pin.OUT)
backward_input4 = Pin(20, Pin.OUT)
backward_enableB = Pin(19, Pin.OUT)

forward_enableB = Pin(14, Pin.OUT)
forward_input4 = Pin(4, Pin.OUT)
forward_input3 = Pin(2, Pin.OUT)
forward_input2 = Pin(9, Pin.OUT)
forward_input1 = Pin(13, Pin.OUT)
forward_enableA = Pin(11, Pin.OUT)

def turn_off_yellow():
    yellow_led1.off()
    yellow_led2.off()

def turn_off_red():
    red_led1.off()
    red_led2.off()

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Create a Pin object for the onboard LED, configure it as an output
led = Pin("LED", Pin.OUT)

# Initialize the LED state to 0 (off)
led_state = 0
current_response = b'stop\r\n'
previous_response = b'nothing\r\n'
value_forward = 1
value_backward = 1
flag = False

# Define a function to handle sensor values and buzzer control
def handle_sensors():
    global value_forward
    global value_backward
    global previous_response
    global current_response
    global flag

    value_forward = infrared_sensor_forward.value()
    value_backward = infrared_sensor_backward.value()
    
    #print(current_response)
    #print(value_backward)

    if not value_forward and current_response != b'backward\r\n' and current_response != b'stop\r\n':
        buzzer.on()
        previous_response = current_response
        flag = True
        print("Forwards Object detected! Turning off motors and turning on the buzzer.")
        
        stop_motors()
    elif not value_backward:
        if current_response == b'backward\r\n' and current_response != b'stop\r\n':
            buzzer.on()
            previous_response = current_response
            flag = True
            print("Backwards Object detected! Turning off motors and turning on the buzzer.")
        
            stop_motors()
    else:
            #print("No object detected. Turning on motors and turning off the buzzer.")
        buzzer.off()
        print("current"+str(current_response))
        print("previous"+str(previous_response))
        myResponse = ''
        if flag:
            myResponse = previous_response
            current_response=previous_response
        else:
            myResponse = current_response
        #print(previous_response)
        #print("previous Data in handle sensor" + str(previous_response))
        #print("Current Data in handle sensor" + str(current_response))
        if value_backward and myResponse == b'backward\r\n':
            buzzer.off()
            go_backward()
            flag = False
                
        if value_forward:
            if myResponse != b'backward\r\n' or myResponse != b'stop\r\n':
                buzzer.off()
                if(myResponse == b'left\r\n'):
                    go_left()
                if(myResponse == b'right\r\n'):
                    go_right()
                if(myResponse == b'forward\r\n'):
                    go_forward()
                flag = False
        
# Function to stop both motors
def stop_motors():
    print('stop')
    red_led1.on()
    red_led2.on()

    turn_off_yellow()
    forward_enableA.off()
    forward_enableB.off()
    forward_input1.off()
    forward_input2.off()
    forward_input3.off()
    forward_input4.off()
    
    print("enA"+str(forward_enableA.value()))
    print("enB"+str(forward_enableB.value()))
    print("in1"+str(forward_input1.value()))
    print("in2"+str(forward_input2.value()))
    print("in3"+str(forward_input3.value()))
    print("in4"+str(forward_input4.value()))

    backward_enableA.off()
    backward_enableB.off()
    backward_input1.off()
    backward_input2.off()
    backward_input3.off()
    backward_input4.off()

# Function to start both motors
def go_forward():
    turn_off_red()
    turn_off_yellow()
    
    print('forward')
    forward_enableA.on()
    forward_enableB.on()
    
    backward_enableA.on()
    backward_enableB.on()
    
    forward_input1.off()
    forward_input2.on()
    forward_input3.on()
    forward_input4.off()
    
    print("enA"+str(forward_enableA.value()))
    print("enB"+str(forward_enableB.value()))
    print("in1"+str(forward_input1.value()))
    print("in2"+str(forward_input2.value()))
    print("in3"+str(forward_input3.value()))
    print("in4"+str(forward_input4.value()))
        
    backward_enableA.on()
    backward_enableB.on()
    
    backward_input1.on()
    backward_input2.off()
    backward_input3.off()
    backward_input4.on()
    
def go_left():
    print('left')
    turn_off_red()
    turn_off_yellow()

    yellow_led1.on()
    forward_enableA.on()
    forward_enableB.off()

    forward_input1.off()
    forward_input2.on()
    forward_input3.on()
    forward_input4.on()

    backward_enableA.off()
    backward_enableB.on()

    backward_input1.off()
    backward_input2.off()
    backward_input3.off()
    backward_input4.on()
    
def go_backward():
    turn_off_red()
    turn_off_yellow()

    print('backward')
    forward_enableA.on()
    #print("enA"+str(forward_enableA.value()))
    forward_enableB.on()
    #print("enB"+str(forward_enableB.value()))
    
    forward_input1.on()
    print("in1"+str(forward_input1.value()))
    forward_input2.off()
    print("in2"+str(forward_input2.value()))
    forward_input3.off()
    print("in3"+str(forward_input3.value()))
    forward_input4.on()
    print("Testing forward_input4 directly: ", forward_input4.value())

        
    backward_enableA.on()
    backward_enableB.on()
    
    backward_input1.off()
    backward_input2.on()
    backward_input3.on()
    backward_input4.off()
    
    print("bkenA"+str(backward_enableA.value()))
    print("bkenB"+str(backward_enableB.value()))
    print("bkin1"+str(backward_input1.value()))
    print("bkin2"+str(backward_input2.value()))
    print("bkin3"+str(backward_input3.value()))
    print("bkin4"+str(backward_input4.value()))
    
def go_right():
    turn_off_red()
    turn_off_yellow()

    yellow_led2.on()
    
    forward_enableA.off()
    forward_enableB.on()

    forward_input1.on()
    forward_input2.off()
    forward_input3.off()
    forward_input4.off()
    
    print("enA"+str(forward_enableA.value()))
    print("enB"+str(forward_enableB.value()))
    print("in1"+str(forward_input1.value()))
    print("in2"+str(forward_input2.value()))
    print("in3"+str(forward_input3.value()))
    print("in4"+str(forward_input4.value()))

    backward_enableA.on()
    backward_enableB.off()

    backward_input1.on()
    backward_input2.off()
    backward_input3.off()
    backward_input4.off()
    

# Define a callback function to handle received data
def on_rx(data):
    print("Data received: ", data)  # Print the received data
    global led_state
    #global previous_response
    global current_response
    #global value_forward
    #global value_backward
    if data == b'toggle\r\n':
        led.value(not led_state)
        led_state = 1 - led_state
    
    current_response = data
    print("Current Data in data" + str(current_response))

    flag = False

    # Network response part
    if current_response == b'stop\r\n':
        print("Stop")
        stop_motors()

    # moveForward
    elif current_response == b'forward\r\n':
        

        turn_off_yellow()
        turn_off_red()

        go_forward()

    # MOVE BACKWARDS
    elif current_response == b'backward\r\n':
        
        turn_off_yellow()
        turn_off_red()

        go_backward()

    # left
    elif current_response == b'left\r\n':
        go_left()
        

    # right
    elif current_response == b'right\r\n':
        go_right()

# Start an infinite loop
while True:
    if sp.is_connected():
        sp.on_write(on_rx)
        handle_sensors()
        #forward_enableA.value(0)
        #print("enA"+str(forward_enableA.value()))
        #forward_enableA.value(1)
        #print("enA"+str(forward_enableA.value()))
        #forward_enableB.value(0)
        #print("enB"+str(forward_enableB.value()))
        #forward_enableB.value(1)
        #print("enB"+str(forward_enableB.value()))
        
        #forward_input1.value(1)
        #print("Min1 "+str(forward_input1.value()))
        
        #forward_input2.value(0)
        #print("Min2 "+str(forward_input2.value()))
        
        #forward_input3.value(0)
        #print("Min3 "+str(forward_input3.value()))
        
        #forward_input4.value(1)
        #print("Min4  "+str(forward_input4.value()))

        #if  not forward_input1.value():
            #forward_input1.value()=not forward_input1.value()
        #    print("00in1"+str(forward_input1.value()))
    
    # Handle sensor values and control the buzzer
    #handle_sensors()

    # Add any additional logic or actions based on sensor values here

    # Add a delay to avoid excessive looping
    utime.sleep_ms(100)

