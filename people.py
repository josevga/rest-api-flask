from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Buuny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    },
}


# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete list of people

    :return:    sorted list of people
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
