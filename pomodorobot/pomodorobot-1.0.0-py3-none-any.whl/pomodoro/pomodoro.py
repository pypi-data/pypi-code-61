import subprocess
import time
from datetime import datetime


class _pomodoro:
    def __init__(self, count, time, break_count=0):
        self.count = count
        self.time = time
        self.break_count = break_count

    def get_count(self) -> int:
        return self.count

    def start_timer(self) -> datetime:
        self.time = datetime.now(tz=None)
        return self.time


def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return


def take_break(pomodoro):
    print('Starting break...')
    sendmessage('Starting break...')
    pomodoro.break_count += 1
    pomodoro.start_timer()
    while True:
        time.sleep(.3)
        timedelta = pomodoro.time.now() - pomodoro.time
        if timedelta.seconds >= 300:
            print('Break is over!')
            sendmessage('Break is over!')
            pomodoro.start_timer()
            return False


def pomodoro_run(pomodoro) -> bool:
    inner = True
    while pomodoro.count < 5:
        print('Starting work session...')
        sendmessage('Starting work session')
        inner = True
        pomodoro.count += 1
        while inner is True:
            timedelta_seconds = int(
                (datetime.now() - pomodoro.time).total_seconds(),
            )
            print(f'{timedelta_seconds//60} minutes has elapsed...', end='\r')
            time.sleep(1)
            if timedelta_seconds > 0 and timedelta_seconds % 1500 == 0:
                print('\nTime for a break')
                sendmessage('Time for a break!')
                take_break(pomodoro)
                inner = False
    print('Finished Pomodoro session. Great work!')
    sendmessage('Finished Pomodoro session. Great work!')
    return True


def pomodoro_setup():
    pomodoro = _pomodoro(0, datetime.now())
    pomodoro_run(pomodoro)


def main():
    pomodoro_setup()


if __name__ == '__main__':
    exit(main())
