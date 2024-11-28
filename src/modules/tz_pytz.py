import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print("Time zone: " + x)

for x in sorted(pytz.country_names):
    print("Country: " + x + ":" + pytz.country_names[x])

# print all timezones with their local times
for x in sorted(pytz.country_names):
    print(f"Code:{x} Country:{pytz.country_names.get(x)} Timezones:{pytz.country_timezones.get(x)}")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")


local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("=" * 80)
print("Local time is {} with TZ {}".format(local_time.strftime("%Y-%m-%d %H:%M:%S"), local_time.tzinfo))
print("UTC time is {} with TZ {}".format(utc_time.strftime("%Y-%m-%d %H:%M:%S"), utc_time.tzinfo))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware Local time is {} with TZ {}".format(aware_local_time.strftime("%Y-%m-%d %H:%M:%S"), aware_local_time.tzinfo))
print("Aware UTC time is {} with TZ {}".format(aware_utc_time.strftime("%Y-%m-%d %H:%M:%S"), aware_utc_time.tzinfo))

print("=" * 80)
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445729400
pl = pytz.timezone('Europe/Warsaw')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(pl)
print("{} seconds since EPOCH is {}".format(s, dt1))







