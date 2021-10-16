# Imports some Python Date/Time functions
import time
import datetime

# Imports GPIO library
import RPi.GPIO as GPIO

# Imports the PyOTA library
import iota_client

# Setup O/I PIN's
LEDPIN=18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.output(LEDPIN,GPIO.LOW)

address = "atoi1qp9427varyc05py79ajku89xarfgkj74tpel5egr9y7xu3wpfc4lkpx0l86"

#connect to default node in the Chrysalis Testnet https://api.hornet-0.testnet.chrysalis2.com
client = iota_client.Client()

#get balance of a specific address
print("Return a balance for a single address:")
print(
    client.get_address_balance(address)
)

# Get current address balance at startup and use as baseline for measuring new funds being added.   
currentbalance = client.get_address_balance(address)
lastbalance = currentbalance

# Define some variables
lightbalance = 0
balcheckcount = 0
lightstatus = False

# Main loop that executes every 1 second
while True:
    
    # Check for new funds and add to lightbalance when found.
    if balcheckcount == 10:
        currentbalance = client.get_address_balance(address)
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
