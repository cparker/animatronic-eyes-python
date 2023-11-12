import network
import time

def connectWIFI(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)

        # Wait for connect or fail
        max_attempts = 10
        attempts = 0
        while not wlan.isconnected() and attempts < max_attempts:
            attempts += 1
            time.sleep(1)

        # Check if connected
        if wlan.isconnected():
            print("Network connected!")
            print("IP address:", wlan.ifconfig()[0])
        else:
            print("Unable to connect to the network.")
    else:
        print("Already connected.")

# Example usage
# connectWIFI('your_SSID', 'your_PASSWORD')
