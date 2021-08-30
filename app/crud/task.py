from app.models import Task


def task_from_text(text: str) -> Task:
    title, args = text.split("#")

