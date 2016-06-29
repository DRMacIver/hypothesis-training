from collections import namedtuple

ScheduledTime = namedtuple('ScheduledTime', ('tomorrow', 'hour', 'minute'))


def cron(cron_hour, cron_minute, current_hour, current_minute):
    """
    Given a cron-style specification of a time of day, and the current time of
    day, return the soonest time that this rule should fire.

    A specification is either an exact number, indicating that the task may
    only fire when the value is exactly that, or None, indicating that any
    number is valid.

    :param cron_hour: 0-23 or None, the permissible hours for this task to run
    :param cron_minute: 0-59 or None, the permissible minutes
    :param current_hour: 0-23, the current hour
    :param current_minute: 0-59, the current minute

    :return: A ScheduledTime representing the soonest time that this event can
    fire.
    """
    if cron_hour is None:
        result_hour = current_hour
    else:
        result_hour = cron_hour
    if cron_minute is None:
        result_minute = current_minute
    else:
        result_minute = cron_minute
    # If the time is after now then this can still run today, but if it's
    # earlier than now then that must be a time tomorrow.
    tomorrow = (result_hour, result_minute) < (current_hour, current_minute)
    return ScheduledTime(tomorrow, result_hour, result_minute)
