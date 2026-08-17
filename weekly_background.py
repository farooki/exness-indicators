# indie:lang_version = 5

from datetime import datetime
from indie import indicator, plot, color


@indicator('Weekly Background', overlay_main_pane=True)

@plot.background(
    'Weekly Background',
    color=color.BLUE(alpha=0.08)
)


def Main(self):

    current_time = datetime.utcfromtimestamp(self.time[0])

    # Calculate the day of the year.
    # We use the date components because Indie does not support
    # datetime.timetuple().
    day_of_year = (
        current_time.month * 31
        + current_time.day
    )

    # Calculate an approximate week number.
    week_number = (
        (day_of_year - current_time.weekday() + 6) // 7
    )

    # Use the year as well so weeks continue alternating
    # correctly across years.
    week_number = (
        current_time.year * 53
        + week_number
    )

    # Select the background color.
    background_color = color.BLUE(alpha=0.08)

    if week_number % 2 != 0:
        background_color = color.GRAY(alpha=0.08)

    return plot.Background(background_color)
