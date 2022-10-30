import platform

from colorama import Fore, Style

print(platform.python_version())

print(Fore.GREEN + 'some green text' + Style.RESET_ALL)

print(Fore.RED + 'some red text' + Style.RESET_ALL)

print('one line')
