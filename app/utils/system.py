import time
from datetime import datetime

from app.core.app_state import (
    APP_START_TIME
)


def get_uptime():

    uptime_seconds = (
        time.time() - APP_START_TIME
    )

    return round(
        uptime_seconds,
        2
    )


def get_timestamp():

    return datetime.now().strftime(
        "%m/%d/%Y, %I:%M:%S %p"
    )