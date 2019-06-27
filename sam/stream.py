import logging
from collections import deque
from datetime import datetime, timedelta


logger = logging.getLogger("sam")


def getdata(data):
    try:
        assert int(data['duration']) >= 0  # Checks whether duration is not negative
        return (datetime.fromisoformat(data['timestamp']), int(data['duration']))  # Attempt to convert input format to a valid datetime
    except (AssertionError, TypeError, ValueError) as err:
        logger.error(err, exc_info=True)
        return (None, None)


def mean(entries, cursor, size):
    values = [e[1] for e in entries if e[0] > cursor - timedelta(minutes=size) and e[0] <= cursor]  # Filter values inside the time window
    return sum(values)/len(values) if values else 0


def prettify(datetime, average):
    return '{ "date": "%s", "average_delivery_time": %.3g }' % (datetime.isoformat(sep=' ', timespec='seconds'), average)


def process(iterator, window_size, appender=print):
    # Initialize variables to store unique entries and cursor for the previous loop
    (entries, cursor) = (deque(maxlen=window_size), None)
    # Check events premises and then filter the stream (fields{timestamp,duration and event_name} and event_name{translation_delivered})
    for message in filter(lambda e: e and {'timestamp', 'duration', 'event_name'} <= e.keys() and e['event_name'] == 'translation_delivered', iterator):
        timestamp, duration = getdata(message)
        if not timestamp or (entries and entries[-1][0] > timestamp):  # Proceed to next valid stream message
            continue
        if not cursor:  # New stream
            prev, cursor = None, timestamp.replace(second=0, microsecond=0)
        while cursor < timestamp:
            if cursor != prev:  # Print only new cursor
                appender(prettify(cursor, mean(entries, cursor, window_size)))
            cursor += timedelta(minutes=1)
        entries += [(timestamp, duration)]
        appender(prettify(cursor, mean(entries, cursor, window_size)))
        prev = cursor  # Aux var to check whether the cursor has been already processed
