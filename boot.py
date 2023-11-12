from ota import OTAUpdater
import mysecrets
import connectWIFI

print("we are booting")

print("MAIN: Connecting to WiFi...")
connectWIFI.connectWIFI(mysecrets.WIFI_SSID, mysecrets.WIFI_PASSWORD)

OTA_UPDATE_GITHUB_REPOS = {
    "cparker/animatronic-eyes-python": ["test.py"]
}

ota_updater = OTAUpdater(
    mysecrets.GITHUB_USER,
    mysecrets.GITHUB_TOKEN,
    OTA_UPDATE_GITHUB_REPOS,
    update_interval_minutes=60,  # Set the update interval to 60 minutes
    debug=True,
    save_backups=True
)

ota_updater.updated()  # Check for updates, and apply if available
print("MAIN: Updates checked. Continuing with the main code...")
