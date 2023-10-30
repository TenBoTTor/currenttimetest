import datetime


def printCurrentTime():
    current_date = datetime.datetime.now()
    if len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 1:
        current_time = f"0{current_date.hour}:0{current_date.minute}"
    elif len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 2:
        current_time = f"0{current_date.hour}:{current_date.minute}"
    elif len(str(current_date.hour)) == 2 and len(str(current_date.minute)) == 1:
        current_time = f"{current_date.hour}:0{current_date.minute}"
    else:
        current_time = f"{current_date.hour}:{current_date.minute}"

    print("北京时间：" + current_time)


def getCurrentTime():
    current_date = datetime.datetime.now()
    if len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 1:
        current_time = f"0{current_date.hour}:0{current_date.minute}"
    elif len(str(current_date.hour)) == 1 and len(str(current_date.minute)) == 2:
        current_time = f"0{current_date.hour}:{current_date.minute}"
    elif len(str(current_date.hour)) == 2 and len(str(current_date.minute)) == 1:
        current_time = f"{current_date.hour}:0{current_date.minute}"
    else:
        current_time = f"{current_date.hour}:{current_date.minute}"

    return current_time
