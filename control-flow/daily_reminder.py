# daily_reminder.py

# Prompt the user for the task description, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Create the basic reminder message based on priority
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        priority_message = "task with unknown priority"

# Check if the task is time-bound and modify the message accordingly
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

# Combine the task, priority, and time-bound information for the final reminder
print(f"Reminder: '{task}' is a {priority_message} {time_message}")
