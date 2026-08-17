# indie:lang_version = 5

from datetime import datetime
from indie import indicator, plot, color


@indicator('New York Background', overlay_main_pane=True)

@plot.background(
    'New York Background',
    color=color.BLUE(alpha=0.08)
)


def Main(self):

    current_time = datetime.utcfromtimestamp(self.time[0])

    # New York session in UTC.
    #
    # During US Daylight Saving Time:
    # New York session starts at 13:30 UTC
    # and ends at 20:00 UTC.
    #
    # During Standard Time:
    # New York session starts at 14:30 UTC
    # and ends at 21:00 UTC.
    #
    # This version uses 13:30 - 20:00 UTC.
    
    current_minutes = (
        current_time.hour * 60
        + current_time.minute
    )

    session_start = 13 * 60 + 30
    session_end = 20 * 60

    in_new_york_session = (
        current_minutes >= session_start
        and current_minutes < session_end
    )

    background_color = color.TRANSPARENT

    if in_new_york_session:
        background_color = color.BLUE(alpha=0.08)

    return plot.Background(background_color)
