from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime
import locale
from dateutil.relativedelta import relativedelta

# Returns the next month formatted as passed


def next_month_day_formatted(format, locale_identifier=None):
    # Get the current date
    current_date = datetime.now()

    if locale_identifier is not None:
        locale.setlocale(locale.LC_TIME, locale_identifier)
    
    # Add one month to the current date using relativedelta
    future_date = current_date + relativedelta(months=1)

    # Format the date as requested
    formatted_date = future_date.strftime(format)

    return formatted_date

def next_two_month_day_formatted(format, locale_identifier=None):
    # Get the current date
    current_date = datetime.now()

    if locale_identifier is not None:
        locale.setlocale(locale.LC_TIME, locale_identifier)
    
    # Add one month to the current date using relativedelta
    future_date = current_date + relativedelta(months=2)

    # Format the date as requested
    formatted_date = future_date.strftime(format)

    return formatted_date