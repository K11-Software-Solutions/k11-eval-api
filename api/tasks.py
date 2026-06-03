from fastapi import BackgroundTasks
def send_email_background(bg: BackgroundTasks, to: str, body: str):
    bg.add_task(send_email, to, body)
