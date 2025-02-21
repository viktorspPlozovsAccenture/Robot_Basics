from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime
import locale


# Returns today formatted
def today_formatted(format, locale_identifier=None):
    # Get the current date
    current_date = datetime.now()

    if locale_identifier is not None:
        locale.setlocale(locale.LC_TIME, locale_identifier)
    
    # Add one month to the current date using relativedelta
    today = current_date
    # Format the date as requested
    formatted_today = today.strftime(format)

    return formatted_today
