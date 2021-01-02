import os


def timeConversion(time):
    #
    # Write your code here.
    #
    if "AM" in time:
        if time[:2] == "12":
            time_int = "00"
            time = f"{time_int}:{time[3:5]}:{time[6:8]}"
        else:
            time = f"{time[:2]}:{time[3:5]}:{time[6:8]}"

    if "PM" in time:
        time_int = int(time[:2]) + 12
        time = f"{time_int}:{time[3:5]}:{time[6:8]}"

    return time


if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.abspath(__name__), 'OUTPUT_PATH'), exist_ok=True)
    f = open('OUTPUT_PATH', 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
