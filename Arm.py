#Joshua Liu
#Change Three, Four, Five, Six to the correct motor names with ctrl-f

from Phidget22.Phidget import *
from Phidget22.PhidgetException import *
from Phidget22.Devices.Stepper import *
from Phidget22.Devices.Encoder import *
from pynput import keyboard
from pynput.keyboard import Key, Listener
import traceback
import time

isBaseRunning = False
baseIndex = 0
baseControls = ["1", "q"] # change this to change the controls

isShoulderRunning = False
shoulderIndex = 1
shoulderControls = ["2", "w"] # change this to change the controls

isThreeRunning = False
ThreeIndex = 2
ThreeControls = ["3", "e"] # change this to change the controls

isFourRunning = False
FourIndex = 3
FourControls = ["4", "r"] # change this to change the controls

isFiveRunning = False
FiveIndex = 4
FiveControls = ["5", "t"] # change this to change the controls

isSixRunning = False
SixIndex = 5
SixControls = ["6", "y"] # change this to change the controls

stopFlag = False

VHubSerial_motors = 563134 #634722 #627531
VHubSerial_encoders = 561059

smoothing = 0.005 # Time delay (in seconds) for a motor to change from moving to stopped
motors = [] # baseMotor, shoulderMotor,
motorsInfo = [] # Set each motor individually with: current limit, holding current, gear box ratio, gear ratio, acceleration, max velocity when moving
motorFlagList = [isBaseRunning, isShoulderRunning, isThreeRunning, isFourRunning, isFiveRunning, isSixRunning]
encoders = []


def on_press(key):
    try: 
        # Control base motor
        if key.char == baseControls[0] and motorFlagList[baseIndex] == True: 
            if not baseMotor.getIsMoving(): 
                baseMotor.setVelocityLimit(motorsInfo[baseIndex][5]) 
        elif key.char == baseControls[1] and motorFlagList[baseIndex] == True: 
            if not baseMotor.getIsMoving(): 
                baseMotor.setVelocityLimit(-motorsInfo[baseIndex][5]) 
        # Control shoulder motor
        if key.char == shoulderControls[0] and motorFlagList[shoulderIndex] == True: 
            if not shoulderMotor.getIsMoving(): 
                shoulderMotor.setVelocityLimit(motorsInfo[shoulderIndex][5]) 
        elif key.char == shoulderControls[1] and motorFlagList[shoulderIndex] == True: 
            if not shoulderMotor.getIsMoving(): 
                shoulderMotor.setVelocityLimit(-motorsInfo[shoulderIndex][5]) 
        if key.char == ThreeControls[0] and motorFlagList[ThreeIndex] == True: 
            if not ThreeMotor.getIsMoving(): 
                ThreeMotor.setVelocityLimit(motorsInfo[ThreeIndex][5]) 
        elif key.char == ThreeControls[1] and motorFlagList[ThreeIndex] == True: 
            if not ThreeMotor.getIsMoving(): 
                ThreeMotor.setVelocityLimit(-motorsInfo[ThreeIndex][5]) 
        if key.char == FourControls[0] and motorFlagList[FourIndex] == True: 
            if not FourMotor.getIsMoving(): 
                FourMotor.setVelocityLimit(motorsInfo[FourIndex][5]) 
        elif key.char == FourControls[1] and motorFlagList[FourIndex] == True: 
            if not FourMotor.getIsMoving(): 
                FourMotor.setVelocityLimit(-motorsInfo[FourIndex][5]) 
        if key.char == FiveControls[0] and motorFlagList[FiveIndex] == True: 
            if not FiveMotor.getIsMoving(): 
                FiveMotor.setVelocityLimit(motorsInfo[FiveIndex][5]) 
        elif key.char == FiveControls[1] and motorFlagList[FiveIndex] == True: 
            if not FiveMotor.getIsMoving(): 
                FiveMotor.setVelocityLimit(-motorsInfo[FiveIndex][5]) 
        if key.char == SixControls[0] and motorFlagList[SixIndex] == True: 
            if not SixMotor.getIsMoving(): 
                SixMotor.setVelocityLimit(motorsInfo[SixIndex][5]) 
        elif key.char == SixControls[1] and motorFlagList[SixIndex] == True: 
            if not SixMotor.getIsMoving(): 
                SixMotor.setVelocityLimit(-motorsInfo[SixIndex][5]) 
        if key.char == 'p': pass
    except AttributeError: 
        print("Special key {0} pressed".format(key))

def on_release(key): 
    global baseMotor, shoulderMotor, ThreeMotor, FourMotor, FiveMotor, SixMotor, stopFlag 
    try:
        if baseControls.__contains__(key.char) and motorFlagList[baseIndex] == True: 
            lim = baseMotor.getVelocityLimit() 
            baseMotor.setVelocityLimit(lim * 3 / 4) 
            time.sleep(smoothing / 4) 
            baseMotor.setVelocityLimit(lim / 2) 
            time.sleep(smoothing / 4) 
            baseMotor.setVelocityLimit(lim / 4) 
            time.sleep(smoothing / 4) 
            baseMotor.setVelocityLimit(0)
        if shoulderControls.__contains__(key.char) and motorFlagList[shoulderIndex] == True: 
            lim = shoulderMotor.getVelocityLimit() 
            shoulderMotor.setVelocityLimit(lim * 3 / 4) 
            time.sleep(smoothing / 4) 
            shoulderMotor.setVelocityLimit(lim / 2) 
            time.sleep(smoothing / 4) 
            shoulderMotor.setVelocityLimit(lim / 4) 
            time.sleep(smoothing / 4) 
            shoulderMotor.setVelocityLimit(0)
        if ThreeControls.__contains__(key.char) and motorFlagList[ThreeIndex] == True: 
            lim = ThreeMotor.getVelocityLimit() 
            ThreeMotor.setVelocityLimit(lim * 3 / 4) 
            time.sleep(smoothing / 4) 
            ThreeMotor.setVelocityLimit(lim / 2) 
            time.sleep(smoothing / 4) 
            ThreeMotor.setVelocityLimit(lim / 4) 
            time.sleep(smoothing / 4) 
            ThreeMotor.setVelocityLimit(0)
        if FourControls.__contains__(key.char) and motorFlagList[FourIndex] == True: 
            lim = FourMotor.getVelocityLimit() 
            FourMotor.setVelocityLimit(lim * 3 / 4) 
            time.sleep(smoothing / 4) 
            FourMotor.setVelocityLimit(lim / 2) 
            time.sleep(smoothing / 4) 
            FourMotor.setVelocityLimit(lim / 4) 
            time.sleep(smoothing / 4) 
            FourMotor.setVelocityLimit(0)
        if FiveControls.__contains__(key.char) and motorFlagList[FiveIndex] == True: 
            lim = FiveMotor.getVelocityLimit() 
            FiveMotor.setVelocityLimit(lim * 3 / 4) 
            time.sleep(smoothing / 4) 
            FiveMotor.setVelocityLimit(lim / 2) 
            time.sleep(smoothing / 4) 
            FiveMotor.setVelocityLimit(lim / 4) 
            time.sleep(smoothing / 4) 
            FiveMotor.setVelocityLimit(0)
        if SixControls.__contains__(key.char) and motorFlagList[SixIndex] == True: 
            lim = SixMotor.getVelocityLimit() 
            SixMotor.setVelocityLimit(lim * 3 / 4) 
            time.sleep(smoothing / 4) 
            SixMotor.setVelocityLimit(lim / 2) 
            time.sleep(smoothing / 4) 
            SixMotor.setVelocityLimit(lim / 4) 
            time.sleep(smoothing / 4) 
            SixMotor.setVelocityLimit(0)
        if key.char == 'p':
            print("p is pressed")
            print(f"\nQuitting program...")
            for i in range(len(motors)): 
                if(motors[i].getAttached() == True): 
                    motors[i].setEngaged(False) 
                    motors[i].close() 
            stopFlag = True
    except AttributeError: 
        print("Special key {0} released".format(key)) 

def onAttach_motor(self): 
    print(" {0} attached!".format(self.getHubPort())) 
    motorFlagList[self.getHubPort()] = True
def onAttach_encoder(self): 
    print("Encoder {0} attached!".format(self.getHubPort())) 
def onDetach(self): 
    print("A motor detached!")
def onError(self,code, description): 
    print("Code: " + ErrorEventCode.getName(code)) 
    print("Description: " + str(description)) 
    print("----------")
    
def initialize_motors(): 
    global motors, motorsInfo
    for i in range(len(motors)): 
        #motors[i].setDeviceSerialNumber(VHubSerial_motors) 
        motors[i].setHubPort(i) 
        # print("Hub Port Set \n") 
        motors[i].setOnAttachHandler(onAttach_motor) 
        # print("Attach Handler Set\n") 
        motors[i].setOnDetachHandler(onDetach) 
        motors[i].setOnErrorHandler(onError) 
        try: 
            motors[i].openWaitForAttachment(300) # If having motor connection timout issues, increase this number 
        except: 
            print(" " + str(i) + " not attached")
        if (motors[i].getAttached() == True): 
            motors[i].setControlMode(StepperControlMode.CONTROL_MODE_RUN) 
            motors[i].setCurrentLimit(motorsInfo[i][0]) 
            motors[i].setHoldingCurrentLimit(motorsInfo[i][1])
            motors[i].setRescaleFactor((1/16) * 1.8 * (1/motorsInfo[i][2]) * (1/motorsInfo[i][3])) # (1/16) * Step angle * (1/Gearbox ratio) * (1/Gear ratio) p
            motors[i].setAcceleration(motorsInfo[i][4])
            motors[i].setVelocityLimit(0) 
            motors[i].setEngaged(True) 
            motors[i].setDataInterval(motors[i].getMinDataInterval())
            
def main(): 
    # All motors, encoders, and positions are declared as global variables 
    global motors, motorsInfo, baseMotor, shoulderMotor, ThreeMotor, FourMotor, FiveMotor, SixMotor
    global baseInitialPos, shoulderInitialPos, ThreeInitialPos, FourInitialPos, FiveInitialPos, SixInitialPos

    # TODO set info
    baseMotor = Stepper() 
    baseInfo = [2.8, 1.68, 100, 1, 5, 5]
    baseInitialPos = 0

    # Info is set for the shoulder
    shoulderMotor = Stepper() 
    shoulderInfo = [3, 1.68, 100, 1, 5, 5]
    shoulderInitialPos = 0
    
    # TODO set info
    ThreeMotor = Stepper() 
    ThreeInfo = [2.8, 1.68, 100, 1, 5, 5]
    ThreeInitialPos = 0
    
    # TODO set info
    FourMotor = Stepper() 
    FourInfo = [2.8, 1.68, 100, 1, 5, 5]
    FourInitialPos = 0
    
    # TODO set info
    FiveMotor = Stepper() 
    FiveInfo = [2.8, 1.68, 100, 1, 5, 5]
    FiveInitialPos = 0
    
    # TODO set info
    SixMotor = Stepper() 
    SixInfo = [2.8, 1.68, 100, 1, 5, 5]
    SixInitialPos = 0

    motors = [baseMotor, shoulderMotor, ThreeMotor, FourMotor, FiveMotor, SixMotor] 
    motorsInfo = [baseInfo, shoulderInfo, ThreeInfo, FourInfo, FiveInfo, SixInfo] 
    try: 
        # Functions to initialize components 
        print(f"\nInitializing...\n\n") 
        initialize_motors() 
        print(f"\nSuccessfully initialized!\n")
        listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
        listener.start()
        # Main loop of code, stopFlag becomes True when 'p' is pressed 
        while(stopFlag == False): 
            time.sleep(0.5)
    except PhidgetException as ex: 
        traceback.print_exc() 
        print() 
        print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)
        print(f"Successfully quit program.\n\nGoodbye!\n")


if __name__ == "__main__": 
    main()

