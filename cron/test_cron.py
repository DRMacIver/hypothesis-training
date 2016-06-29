from cron import cron
from hypothesis import given
from hypothesis import strategies as st


def test_if_all_star_then_runs_now():
    assert cron(None, None, 10, 10) == (False, 10, 10)


def test_star_hour_can_fire_this_hour():
    assert cron(10, None, 10, 30) == (False, 10, 30)


def test_star_minute_can_fire_at_current_minute():
    assert cron(2, None, 2, 10) == (False, 2, 10)


@given(
    cron_hour=st.none() | st.integers(0, 23),
    cron_minute=st.none() | st.integers(0, 59),
    current_hour=st.integers(0, 23),
    current_minute=st.integers(0, 59),
)
def test_cron_does_not_crash(
        cron_hour, cron_minute, current_hour, current_minute
):
    cron(cron_hour, cron_minute, current_hour, current_minute)
