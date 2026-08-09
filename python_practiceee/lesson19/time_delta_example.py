from datetime import datetime, UTC, timedelta
import pytz

todayUTC = datetime.now(UTC)
todayLocal = pytz.timezone("Europe/Kyiv").localize(datetime.now())
print(todayLocal)
print(todayUTC)

print(todayLocal - todayUTC)

today = datetime.now()
print(today)
seven_days_ago = today - timedelta(days=7)
print(seven_days_ago)
