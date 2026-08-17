# indie:lang_version = 5

from datetime import datetime
from indie import indicator, plot, color


@indicator('London Background', overlay_main_pane=True)

@plot.background(
    'London Background',
    color=color.BLUE(alpha=0.08)
)


def Main(self):

    current_time = datetime.utcfromtimestamp(self.time[0])

    current_minutes = (
        current_time.hour * 60
        + current_time.minute
    )

    session_start = 8 * 60
    session_end = 17 * 60

    in_session = (
        current_minutes >= session_start
        and current_minutes < session_end
    )

    background_color = color.TRANSPARENT

    if in_session:
        background_color = color.BLUE(alpha=0.08)

    return plot.Background(background_color)
