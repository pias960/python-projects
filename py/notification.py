from plyer import notification
import time
def notify(title,messege):
    notification.notify(
        title = title,
        message = messege,
        app_icon = "path/to/icon.ico",
        timeout = 10
    )
    time.sleep

notify("Task Completed","Your task has been completed")