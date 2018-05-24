import sys, os.path
tool_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) + '/tools/')
sys.path.append(tool_dir)
# First import the ADB_Action_Script.py it must be on the same folder
from ADB_Action_Scipt import ActionScript
# then import the RC keys and App PKGs for easy scripting
from RC_Code import SonyRCKey
from AppList import AppList

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
print("Launch Hulu for 1 hour")
print("Launch Netflix for 1 hour")
print("Launch Amazon for 1 hour")
print("Tune back to HDMI1 for 1 hour")
print("Power OFF TV")


# Automation Start
# ------------------------------- Hulu ----------------------------------
tv.clear_launch_app(app.HULU_PKG, app.HULU_ACT)
tv.wait_in_second(5) # wait load hulu
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_hour(1) # playback time

# ------------------------------- Netflix ---------------------------------
tv.clear_launch_app(app.NETFLIX_PKG, app.NETFLIX_ACT)
tv.wait_in_second(8)
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_second(2)
tv.press_rc_key(rc.NAV_DOWN)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.NAV_ENTER) # playback start
tv.wait_in_minute(1)
tv.press_rc_key(rc.HOME)
tv.wait_in_second(5)

# ------------------------------- Amazon ---------------------------------
tv.clear_launch_app(app.AMAZON_PKG, app.AMAZON_ACT)
tv.wait_in_second(8)
tv.press_rc_key(rc.NAV_DOWN)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.NAV_ENTER)
tv.wait_in_second(1.5)
tv.press_rc_key(rc.NAV_ENTER) # playback start
tv.wait_in_second(5)
tv.press_rc_key(rc.HOME)
tv.wait_in_second(5)

# RC OFF TV
tv.press_rc_key(rc.POWER)

# ------------------------------- Keep terminal open ---------------------------------
close = input("Press Enter to close terminal")
