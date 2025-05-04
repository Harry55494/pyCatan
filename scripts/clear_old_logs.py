import os
from datetime import datetime, timedelta

delta = timedelta(days=7)

for filename in os.listdir("logs"):
    if filename.endswith(".log"):
        file_path = os.path.join("logs", filename)
        file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        if datetime.now() - file_mod_time > delta:
            os.remove(file_path)
            print(f"Deleted old log file: {file_path}")
