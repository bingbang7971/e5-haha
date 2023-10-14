import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, seconds = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

if __name__ == '__main__':
    minutes = int(input("请输入专注时长（分钟）："))
    print("专注开始！")
    countdown(minutes)
    print("专注结束！")
