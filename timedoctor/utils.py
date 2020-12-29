from datetime import datetime, timedelta 

def get_date_past_days(days: int = 0) -> str:
    """Getting datetime ISO format from past days

    Args:
        days (int, optional): from days. Defaults to 0.

    Returns:
        str: ISO Format Datetime
    """
    now: datetime = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    past: timedelta = timedelta(days=days)

    changed_time: datetime = now - past
    return changed_time.isoformat() + '.000Z'