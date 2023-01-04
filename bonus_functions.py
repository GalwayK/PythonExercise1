FREEZING_POINT = 0
BOILING_POINT = 100


def feet_to_meters(measure_feet):
    """
    Accepts a given value in feet and converts that value to meters.
    :param measure_feet:
    :return:
    """
    return measure_feet / 3.281


def inches_to_meters(measure_inch):
    """
    Accepts a given value in inches and converts that value to meters.
    :param measure_inch:
    :return:
    """
    return measure_inch / 39.37


def parse_feet_inches(measure_imperial_string):
    """
    Accepts a String and returns that String as a list delimited by blank whitespaces.
    :param measure_imperial_local:
    :return:
    """
    return measure_imperial_string.split(" ")


def convert_list_to_float(string_list):
    """
    Accepts a list of String as input and returns that String with its items converted to floats.
    :param string_list:
    :return:
    """
    return [float(item) for item in string_list]


def convert_list_to_dict(measure_list_local):
    """
    Accepts a list of measurements in feet and inches and returns that list as a dictionary for each
    measurement.
    :param measure_list_local:
    :return:
    """
    return {"feet": measure_list_local[0], "inches": measure_list_local[1]}


def why(message):
    """
    This entirely unnecessary functions prints a message.
    It fills entirely the same purpose as the print() function and should never be used in a real program.
    :param message:
    :return:
    """
    print(message)
    return None


def is_freezing(temp):
    if temp <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temp < BOILING_POINT:
        return "Liquid"
    elif temp >= BOILING_POINT:
        return "Gas"


def count_period(statement):
    period_count = 0
    for char in statement:
        if char == ".":
            period_count = period_count + 1
    return period_count
