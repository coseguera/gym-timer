import usb_cdc

usb_cdc.data.timeout = 0.1

inText = ""

def check_input():
    global inText
    i = usb_cdc.data.readline().decode()
    if len(i) > 0:
        inText = i
        return True
    return False

def read_input():
    global inText
    inText = usb_cdc.data.readline().decode()

def get_value(arr, i):
    x = int(arr[i])

    if len(arr) > i + 1 and arr[i + 1].startswith("minute"):
        x = x * 60

    return x

def parse_input():
    global inText
    result = []
    params = inText.split("/")

    # command
    result.append(params[0].rstrip())

    if len(params) < 2:
        return result

    # first value
    result.append(get_value(params, 1))

    if len(params) < 4:
        return result

    # second value
    result.append(get_value(params, 4))

    if len(params) < 7:
        return result

    # third value
    result.append(get_value(params, 7))

    return result