# Imports
from colored import Fore, Back, Style
from functions.functions import menu

# Set up colors
color1: str = f"{Style.BOLD}{Back.GREEN}"
color2: str = f"{Style.BOLD}{Fore.RED}"

print(f" {color1}>>> HEALTH CHECK APP <<<{Style.reset} \n")
print("This app will collect health metrics from you to provide a number of results for you, such as: ")
print("- Body Mass Index (BMI)")
print("- Waist to hip ratio")
print("- Heart rate rating")
print("- Overall risk rating for your age and biological sex.\n")
print(f"{color2}Important Note:{Style.reset} This app does not diagnose medical conditions and does not share any of your information without written consent. This output from this app is to be used as a guide only and may suggest you seek guidance from a General Practitioner\n")
try:
    menu()
except ZeroDivisionError:
    print(f"\n{color2}ERROR:{Style.reset} Cannot Divide by Zero. \nMeasurements cannot be zero. \nTry Again.")
except KeyboardInterrupt:
    print(f"\n {color2}>>> Program Terminated <<<{Style.reset} ")
except OSError:
    print(f"\n{color2}SYSTEM ERROR:{Style.reset} Try Again.")
except SystemError:
    print(f"\n{color2}SYSTEM ERROR:{Style.reset} Try Again.")
except RuntimeError:
    print(f"\n{color2}RUNTIME ERROR:{Style.reset} Try Again.")
except OverflowError:
    print(f"\n{color2}OVERFLOW ERROR:{Style.reset} Check the information you are entering and try again.")



