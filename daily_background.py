# indie:lang_version = 5

from datetime import datetime
from indie import indicator, plot, color


@indicator('Daily Background', overlay_main_pane=True)

@plot.background(
    'Daily Background',
    color=color.BLUE(alpha=0.08)
)


def Main(self):

    current_time = datetime.utcfromtimestamp(self.time[0])

    # Create YYYYMMDD
    day_number = (
        current_time.year * 10000
        + current_time.month * 100
        + current_time.day
    )

    # Select the color first
    background_color = color.BLUE(alpha=0.08)

    if day_number % 2 != 0:
        background_color = color.GRAY(alpha=0.08)

    # Return must be the final statement of Main
    return plot.Background(background_color)
