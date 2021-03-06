# First import the ADB_Action_Script.py it must be on the same folder
from tools.ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from tools.RC_Code import SonyRCKey
from tools.AppList import AppList

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()

# Print Requirements
print("Requirements:")
print("HDMI1 with IRBlaster setup")
print("Amazon, Netflix, Hulu and Vudu are signed in")
print("Auto program completed for RF\n")

# Print Instructions
print("This is what the script does:")
print("Tune to HDMI1 for 1 hour")
print("Then change channel every 10 minutes")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune back to HDMI1 for 1 hour")
print("Power OFF TV\n")

print(tv.deviceID)

start = input("Press Enter to start")

# Automation Start
# ------------------------------- HDMI1 ----------------------------------
tv.press_rc_key(rc.HDMI1)
tv.wait_in_second(5)
# channel up
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_UP)
    tv.wait_in_second(10)  # playback time
    print(f'CHANNEL UP loop count: {i}')
# channel down
for i in range(1, 4):
    tv.press_rc_key(rc.CHANNEL_DOWN)
    tv.wait_in_second(10)  # playback time
    print(f'CHANNEL DOWN loop count: {i}')

# ------------------------ Keep terminal open -----------------------------
close = input("Press Enter to End")
