import csv
from .train_task import TrainTask
from .validator import parse_time, time_order
from pathlib import Path


def load_trains(filename):
    trains=[]
    
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            
            id=row["id"]
            
            departure=parse_time(row["departure"])
            arrival=parse_time(row["arrival"])
            
            time_order(id,departure,arrival)
            
            train = TrainTask(
                id=id,
                origin=row["origin"],
                destination=row["destination"],
                departure=departure,
                arrival=arrival
            )
            
            trains.append(train)
    return trains
        

TRAINS = load_trains(Path(__file__).resolve().with_name("trains.csv"))