import ngl
import colorama
import random
import string

n = ngl.NGLWrapper()

def random_text(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# ask user for username
username = input("Enter the username: ")
n.set_username(username)

print(colorama.Fore.BLUE + "Welcome to the NGL Spammer!" + colorama.Style.RESET_ALL)
print(colorama.Fore.BLUE + "Please select a mode." + colorama.Style.RESET_ALL)
print(colorama.Fore.BLUE + "Mode 1: Send random text" + colorama.Style.RESET_ALL)
print(colorama.Fore.BLUE + "Mode 2: Send custom text" + colorama.Style.RESET_ALL)
mode = input("Enter mode (1 or 2): ")
if mode == "1":
    # ask for length of text
    length = input("Enter length of text: ")
    # ask for number of times to send
    times = input("Enter number of times to send: ")
    for i in range(int(times)):
        n.send_question(random_text(int(length)))
elif mode == "2":
    # ask for text to send
    text = input("Enter text to send: ")
    # ask for number of times to send
    times = input("Enter number of times to send: ")
    for i in range(int(times)):
        n.send_question(text)
else:
    print(colorama.Fore.RED + "Invalid mode." + colorama.Style.RESET_ALL)
    exit()
