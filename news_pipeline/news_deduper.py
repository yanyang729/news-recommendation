import datetime

def handle_message(msg):
    if msg is None or not isinstance(msg,dict):
        return

    task = msg
    text = task['text']
    if text is None:
        return

    published_at = parser.parse(task['publishedAt'])
    published_at_day_begin = datetime.datetime()
    # TODO

    db = mongodb
