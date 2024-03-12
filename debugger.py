import time
def debug(msg = None):
    print('\033[33m'+f'[debug]: {msg}'+'\033[0m')
def info(msg = None):
    print(f'[info]: {msg}')
def warn(msg = None):
    print('\033[91m'+f'[warn]: {msg}'+'\033[0m')
def error(msg = None):
    print('\033[31m'+f'[Error]: {msg}'+'\033[0m')
def dinput(msg = None):
    print(f'[input]: {msg}')
    return input('>>> ')
def sinput(msg = None):
    print(f'[input]: {msg}')
def wait(msg = None, tim = None):
    print(f'[time]: {msg}')
    time.sleep(tim)