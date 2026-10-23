from datetime import datetime


def parse_time(value):
    try:
        return datetime.strptime(value, "%H:%M").time()
    except ValueError:
        raise ValueError(f"Niepoprawny czas: {value}")
    

def time_order(train_id, departure, arrival):
    if arrival < departure:
        raise ValueError(
            f"Pociąg {train_id}:"
            f"przyjazd {arrival} jest wcześniejszy niż"
            f"odjazd {departure}"
            )