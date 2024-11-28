import pytz
import datetime

available_time_zones = {
    '1': 'Europe/Warsaw',
    '2': 'Pacific/Auckland',
    '3': 'Europe/Moscow'
}

choice = '1'

while int(choice):
    for key, item in available_time_zones.items():
        print(f"{key}. {item}")
    choice = input("Please choose a timezone (0 - to quit):")

    if choice in available_time_zones.keys():
        tz_to_display = pytz.timezone(available_time_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_time_zones[choice], world_time.strftime('%A %x %X %z'),
                                               world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
        print()
