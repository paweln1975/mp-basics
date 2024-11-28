import sys
import os
from datetime import date, datetime

print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info}")
print(f"Current dir: {os.getcwd()}")
print(f"Current date: {date.today()}")
print(f"Current time: {datetime.now()}")
