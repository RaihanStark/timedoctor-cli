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

def convert_timestamp_to_hour(timestamp: int = 0) -> str:
    converted_timestamp = "{:.1f}".format(timestamp / 60 / 60).split('.')
    converted_timestamp[1] = str(int(converted_timestamp[1]) * 5)
    return '{0}h {1}m'.format(converted_timestamp[0],converted_timestamp[1])