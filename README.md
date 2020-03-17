# Integrating physical devices with IOTA - Pay the Light

The first part in a series of beginner tutorials on integrating physical devices with the IOTA protocol.

![img](https://miro.medium.com/max/700/1*Vqp9k65WZXDtcOsCP7P49w.jpeg)

## Introduction

This beginner’s tutorial is a simple, yet powerful demonstration of using the IOTA protocol for making payments and receiving services from a physical device. The goal of this tutorial is to demonstrate how we can build a simple power circuit that can be switched ON/OFF based on the current balance of a given IOTA address.
We will be using an internet connected Raspberry PI together with the Python programming language to check for balances on the IOTA tangle and perform switching of a connected relay using the PI’s internal GIO pins. The relay will again be connected to a simple battery powered circuit that turns ON/OFF a Light Emitting Diode (LED), representing the physical device in our project.

*Note!
A simpler version of this project would be to connect the LED directly to the Raspberry PI’s GOI pins without using the relay. However, as the Raspberry PI GIO pins can only provide a maximum of 5V we will use a relay to demonstrate that we can use the same basic setup to manage high voltage devices. The main reason for choosing a low powered circuit is however that* ***no one should be playing around with high voltage unless they absolutely know what they are doing****.*

------

## The Use Case

Before going into details on building this project we should take a step back and look at the bigger picture as to how a simple demo project like this could be applied to a real world use-case, solving real problems.

Imagine you are staying at a hotel where each room is equipped with its own refrigerator. In most cases these refrigerators just sits there, consuming energy and not being used, still you end up paying for it indirectly as part of the rent. What if there was a mechanism that would allow you to pay the refrigerator directly for the time it is being used, and at the same time have it automatically turned off when it’s not being used? This is basically the use case we are going to recreate on this tutorial, only difference is that we will be replacing the refrigerator with a LED for convenience and safety.

Now, let’s try and describe a sequence of events to demonstrate how the system can be implemented and used.

First, let’s imagine the hotel owner has installed a refrigerator in your room, placing a relay in the refrigerator power circuit. The relay is then connected to the internal GIO pins on a Raspberry PI serving as a control unit for the refrigerator payment system. Next, he creates an IOTA address for the refrigerator to be used for monitoring when new refrigerator funds are being added. Finally, he prints a QR code of the IOTA address and attaches the QR code to the refrigerator.

Now that the physical part of the system is completed, he creates a simple Python program that runs on the Raspberry PI, continuously checking the refrigerator IOTA address for new funds, switching the refrigerator (relay) ON/OFF accordingly.

Now image you as the guest coming back from shopping having bought a nice bottle of white wine for later that evening. To make sure it stays cool you pick up your mobile phone, open your favorite IOTA wallet, scan the QR code attached to your refrigerator and transfer a certain amount of IOTA’s to the refrigerator depending on how long you plan to use it.

As soon as your transaction is confirmed by the tangle, the refrigerator balance is increased and the change in balance is picked up by the Python program running on the PI. The PI will then switch on the relay using its GIO pins and the refrigerator will turn on.

The Python program will keep track of time used and the amount of IOTA’s you transferred, continuously removing time from your active balance, and finally turning off the refrigerator when your balance is empty.

That’s it… Finally, you enjoy a nice bottle of cool wine before hitting the town.

*Note!*
*In a scenario where you want to control multiple devices using the same setup it would probably be better to have a central Raspberry PI functioning as a common control unit for all devices, where each device is assigned its own unique IOTA address. This can easily be achieved using a multi-channel relay with some slight modification to the Python code. To simplify wiring and coding we will manage only one device in this tutorial, but feel free to extend the project later on to manage multiple devices.*

------

## Components

In this section we will take a look at the different components required to building the project. You should be able to acquire them at most electronic stores or on EBAY/AMAZON for less than 50 USD.

**Raspberry PI**
The “brains” of the project is the Raspberry PI. The Raspberry PI will be running the Python code that monitors our IOTA tangle address for new funds and handles the Raspberry PI’s GIO pins.

![img](https://miro.medium.com/max/280/1*FMECJ8VKTSIT0_Z9w_m3Zw.jpeg)

**Relay**
The Relay is used to switch ON/OFF our power circuit and thereby our device (in this case the LED). To simplify our circuit we will be using a relay module (shield) that has all the required components, pins and connectors built in to the module. Notice that you can buy these modules with multiple relays (channels) that can be switched ON/OFF individually. This can be useful in cases where you need to manage multiple devices as discussed earlier.

![img](https://miro.medium.com/max/225/1*4ktyvSuyTd6_jlAmj2ZaOQ.jpeg)

**Breadboard**
The breadboard is used to wire up our circuit without having to do any soldering, making it easy to assemble and disassemble.

![img](https://miro.medium.com/max/251/1*Igi0Nd93Vu08Sb4N_jEV9Q.jpeg)

**Light Emitting Diode (LED)**
The LED will light up when powered and will be representing our physical device (refrigerator) is this project.

![img](https://miro.medium.com/max/225/1*7yFEMtUvCuieBwPzlCmQpA.jpeg)

**Resistor (330 ohm)**
The resistor is used to limit the current sent to our LED. Without the resistor you may damage the LED and/or the Raspberry PI. The type of resistor you should use depends on the type of LED and the amount of voltage you are providing to the circuit. In my case I’m using a 9V battery so a 330 ohm resistor should be fine. I suggest you research what type of resistor you should use depending on the components used in your version of the project.

![img](https://miro.medium.com/max/226/1*WmcyYVlVm0IJtKlvjSO7cQ.jpeg)

**Battery**
The battery is used to provide power to our power circuit. In my case am using a 9V battery.

![img](https://miro.medium.com/max/224/1*KR1UwBURPs_TN9ISPwmH2A.jpeg)

**Wires**
We also need some wires to hook it all up.

![img](https://miro.medium.com/max/225/1*zJ5LOJ-NyWiUYlMq-8s1tw.jpeg)

**QR Code**
A printed QR code of the IOTA payment address is handy if you want to pay the LED using a mobile IOTA wallet. You will find a QR code when generating new addresses using the IOTA wallet or by searching an existing address at [https://thetangle.org](https://thetangle.org/)

![img](https://miro.medium.com/max/163/1*0Birfy2lGcfHKVHgxvEEPQ.png)

------

## Wiring the project

Now, Lets look at how to wire up the circuit used in this project.

![img](https://miro.medium.com/max/682/1*QxmP3VBpBKZeRUDPxmJmSQ.png)

![img](https://miro.medium.com/max/367/1*LyZnkPjYofggUfFNcGhzlg.png)

Connect the circuit as follows:

1. Connect pin 2 (5V) on the Raspberry PI to the VCC pin on the relay module.
2. Connect pin 6 (GROUND) on the Raspberry PI to the GND pin on the relay module.
3. Connect pin 12 (GPIO18) on the Raspberry PI to the IN (Signal) pin on the relay module.
4. Connect the COM terminal on the relay module to the positive side (+) of the battery.
5. Connect the NO terminal on the relay module to the Anode (+) side of the LED having the resistor in between.
6. Connect the negative side (-) of the battery to the Kathode (-) side of the LED.

*Note!*
*Notice how the two pins on the LED have different lengths. The short pin represents the Kathode (-) side and the long pin represents the Anode (+) side of the LED.*

------

## Required Software and libraries

Before we can start writing our Python code for this project we need to make sure that we have all the required software and libraries installed on our Raspberry PI.

First of all, we need to have an OS installed on our Raspberry PI. Any Raspberry PI supported Linux distribution should work. In my example I’m using the Raspbian distro as it already have Python and several Python editors (IDE) included. The Raspbian distro with installation instructions can be found here: https://www.raspberrypi.org/downloads/raspbian/

In case you need to install Python separately, you will find it here: https://www.python.org/downloads/

Finally, we need to install the PyOTA API library that will allow us to access the IOTA tangle using the Python programming language. The PyIOTA API library with installation instructions can be found here: https://github.com/iotaledger/iota.lib.py

------

## The Python Code

Now that we have our circuit all wired up and the necessary software and libraries installed on our Raspberry PI, we will start writing the actual Python code that runs our project.

```python
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
address = [Address(b'GTZUHQSPRAQCTSQBZEEMLZPQUPAA9LPLGWCKFNEVKBINXEXZRACVKKKCYPWPKH9AWLGJHPLOZZOYTALAWOVSIJIYVZ')]

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
```

The source code for this project can be found here: https://gist.github.com/huggre/a3044e6094867fe04096e0c64dc60f3b

------

## Running the project

To run the project, you first need to save the code in the previous section as a text file on your Raspberry PI.

Notice that Python program files uses the .py extension, so let’s save the file as **let_there_be_light.py** on the Raspberry PI.

To execute the program, simply start a new terminal window, navigate to the folder where you saved *let_there_be_light.py* and type:

**python let_there_be_light.py**

You should now see the code being executed in your terminal window, displaying your current light balance and checking the LED’s IOTA address balance for new funds every 10 seconds.

------

## Pay the light

To turn on the LED you simply use your favorite IOTA wallet and transfer some IOTA’s to the LED’s IOTA address. As soon as the transaction is confirmed by the IOTA tangle, the LED should light up and stay on until the light balance is empty depending on the amount of IOTA’s you transferred. In my example I have set the IOTA/light ratio to be 1 IOTA for 1 second of light.

*Note!*
*If using a mobile wallet to pay the light you may consider printing a QR code that can be scanned for convenience whenever you want to pay the light.*

------

## Donations

If you like this tutorial and want me to continue making others, feel free to make a small donation to the IOTA address used in the Python code. Also, feel free to use the same IOTA address when building and testing your version of this project, so that whenever my LED (and yours) lights up it gives me (us) a nice reminder that someone else is using this tutorial.

![img](https://miro.medium.com/max/382/1*j2ENIzmDzXcGSgAdY4w-Jw.png)

NYZBHOVSMDWWABXSACAJTTWJOQRPVVAWLBSFQVSJSWWBJJLLSQKNZFC9XCRPQSVFQZPBJCJRANNPVMMEZQJRQSVVGZ

