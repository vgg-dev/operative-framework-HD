#!/usr/bin/env  python

import subprocess
import datetime
import requests
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0])
from colorama import Fore, Style
from framework import config


def print_log(color_string, type_string, text):
    return datetime.datetime.today().strftime('[%Y-%m-%d %H:%M:%S] ') + color_string + str(type_string) +  Style.RESET_ALL + " " + str(text)


def main():
    print print_log(Fore.BLUE, 'INFO', 'Welcome to Operative Framework client' + str(config.OPERATIVE_FRAMEWORK_VERSION))
    try:
        requests.head("http://127.0.0.1:" + config.BACKEND_PORT + "/")
    except:
        print print_log(Fore.RED, 'ERROR', "Please run backend sudo python bin/opf_server.py")
        sys.exit()
    if not os.path.isdir(os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0] + "/client"):
        print print_log(Fore.RED, 'ERROR', "directory : '" + os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0] + "/client' not found")
        sys.exit()
    print print_log(Fore.BLUE, 'INFO', 'Starting client in background....')
    print print_log(Fore.GREEN, 'SUCCESS', 'framework start  at 127.0.0.1:' + config.FRONTEND_PORT)
    cmd = "npm start --prefix " + os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0] + "/client/"
    a = subprocess.Popen(cmd, shell=True)
    stdout, stderr = a.communicate()
    if a.returncode != 0:
        print print_log(Fore.RED, "ERROR", "A error has been occurred with a client")
        print print_log(Fore.RED, "ERROR", "Please run it manually: npm run build --prefix 'client/'")
        sys.exit()


if __name__ == "__main__":
    main()