# Imports some Python Date/Time functions
import time
import datetime

# Imports GPIO library
import RPi.GPIO as GPIO

# Imports the PyOTA library
from iota import Iota
from iota import Address

# Setup O/I PIN's
LEDPIN=18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.output(LEDPIN,GPIO.LOW)


# Function for checking address balance on the IOTA tangle. 
def checkbalance():

    print("Checking balance")
    gb_result = api.get_balances(address)
    balance = gb_result['balances']
    return (balance[0])

# URL to IOTA fullnode used when checking balance
iotaNode = "https://nodes.thetangle.org:443"

# Create an IOTA object
api = Iota(iotaNode, "")

# IOTA address to be checked for new light funds 
# IOTA addresses can be created using the IOTA Wallet
address = [Address(b'NYZBHOVSMDWWABXSACAJTTWJOQRPVVAWLBSFQVSJSWWBJJLLSQKNZFC9XCRPQSVFQZPBJCJRANNPVMMEZQJRQSVVGZ')]

# Get current address balance at startup and use as baseline for measuring new funds being added.   
currentbalance = checkbalance()
lastbalance = currentbalance

# Define some variables
lightbalance = 0
balcheckcount = 0
lightstatus = False

# Main loop that executes every 1 second
while True:
    
    # Check for new funds and add to lightbalance when found.
    if balcheckcount == 10:
        currentbalance = checkbalance()
        if currentbalance > lastbalance:
            lightbalance = lightbalance + (currentbalance - lastbalance)
            lastbalance = currentbalance
        balcheckcount = 0

    # Manage light balance and light ON/OFF
    if lightbalance > 0:
        if lightstatus == False:
            print("light ON")
            GPIO.output(LEDPIN,GPIO.HIGH)
            lightstatus=True
        lightbalance = lightbalance -1       
    else:
        if lightstatus == True:
            print("light OFF")
            GPIO.output(LEDPIN,GPIO.LOW)
            lightstatus=False
 
    # Print remaining light balance     
    print(datetime.timedelta(seconds=lightbalance))

    # Increase balance check counter
    balcheckcount = balcheckcount +1

    # Pause for 1 sec.
    time.sleep(1)
