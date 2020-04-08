import easygui
import subprocess
import keyboard

print("""
******************Skip UAC******************
*    This is a tool create to remove UAC   *
* from application such as installers that *
* even when you dont require admin ask for *
*  it anyway. This tool will run the file  *
*     without the UAC prompt so you can    *
*             install it anyway            *
*                                          *
*   Note this software is provided as is   *
*  and you still shouldent run any files   *
*       that could damge your system       *
********************************************


""")

print("Press enter to continue...\n\n")
keyboard.wait("enter")


print("[*] Select a file to execute")
executeFile = easygui.fileopenbox(title="Select a file to execute", default="*.exe")
if not executeFile:
    print("\nPlease select a process")
    keyboard.wait("enter")
executeStatus = easygui.ynbox("You are about to execute\n" + executeFile + "\n\nDoes this information look correct?", title="Does this look correct?",)

if executeStatus:
    print("Executing: " + executeFile)
    print("Building launch arguments")
    command = 'set __COMPAT_LAYER=RunAsInvoker && start "' + executeFile + ' - SkipUAC" "' + executeFile + '"'
    print("Executing arguments...")
    try:
        output = subprocess.check_output(command, shell=True)
    except:
        easygui.exceptionbox("While attempting to execute\n" + executeFile + "\n\nThe process generated an exception", title="Something went wrong")
    print("Exited with status " + str(output))
    print("\nPress enter to continue...")
    keyboard.wait("enter")
else:
    print("Execution was halted")
    print("\nPress enter to continue...")
    keyboard.wait("enter")