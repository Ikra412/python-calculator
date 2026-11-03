from datetime import datetime

today = datetime.now().date()
christmas = datetime(today.year, 12, 25).date()

if today > christmas:
    christmas = datetime(today.year + 1, 12, 25).date()

left_days = (christmas - today).days

print("today date:", today)
print("christmas date:", christmas)
print("days left until christmas:", left_days)
