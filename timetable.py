from tabulate import tabulate
import random

# Define time slots and periods
time_slots = [
    "9:00-10:00",
    "10:00-10:50",
    "10:50-11:00",  # Break
    "11:00-11:50",
    "11:50-12:40",
    "12:40-1:20",   # Lunch
    "1:20-2:10",
    "2:10-3:00",
    "3:00-3:50"
]

period_labels = {
    "9:00-10:00": "1st",
    "10:00-10:50": "2nd",
    "10:50-11:00": "Break",
    "11:00-11:50": "3rd",
    "11:50-12:40": "4th",
    "12:40-1:20": "Lunch",
    "1:20-2:10": "5th",
    "2:10-3:00": "6th",
    "3:00-3:50": "7th"
}

subjects = ["MSF", "ACD", "DBMS", "Python", "IAI"]
teachers = {
    "MSF": "Mahalaxmi",
    "ACD": "Kiranmai",
    "DBMS": "Swapna",
    "IAI": "Swathi",
    "Python": "GVK"
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize timetable per day
timetable = {day: {} for day in days}

for day in days:
    available_subjects = subjects.copy()
    random.shuffle(available_subjects)
    for time in time_slots:
        if "Break" in period_labels[time] or "Lunch" in period_labels[time]:
            timetable[day][time] = period_labels[time]
        else:
            if not available_subjects:
                available_subjects = subjects.copy()
                random.shuffle(available_subjects)
            subject = available_subjects.pop()
            teacher = teachers[subject]
            timetable[day][time] = f"{subject}\n({teacher})"
    
# Create table format: Rows = Time Slots, Columns = Days
table = []
for time in time_slots:
    row = [f"{time}\n({period_labels[time]})"]
    for day in days:
        row.append(timetable[day][time])
    table.append(row)

# Print the table
headers = ["Time Slot"] + days
print(tabulate(table, headers=headers, tablefmt="grid"))


