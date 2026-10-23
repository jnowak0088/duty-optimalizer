import depots
from data.trains_loader import TRAINS

def can_follow(task1, task2):
    """Can I do task2 after task1?"""
    return (
        (task1.destination == task2.origin) and (task1.arrival <= task2.departure)
    )
    
def can_start(depot, train):
    """Can I start duty in this depo from this train?"""
    return depot.location == train.origin

def can_finish(depot, train):
    """Can I finish duty in this depo from this train?"""
    return depot.location == train.destination

def generate_duties(depot, trains):
    """Generate duties, for given depot"""
    duties=[]
    
    def extend(current_duty):
        """If it is possible extend the duty"""
        current=current_duty[-1]
        
        if can_finish(depot, current):
            """If we visit depot, copy this duty and save"""
            duties.append(current_duty.copy())
            
        for next_train in TRAINS:
            """If specific train is in current duty - ignore it"""
            if next_train in current_duty:
                continue
            
            if can_follow(current, next_train):
                """If we can follow from current to next train, then add this next train to current duty, extend current duty to get new current variable and delete old current duty"""
                current_duty.append(next_train)
                extend(current_duty)
                current_duty.pop()
            
    for train in TRAINS:
        """Check trains one by one. If it starts from our depot - the duty can start with this train."""
        if can_start(depot,train):
            extend([train])
                
    return duties    
        
    
        
duties_A = generate_duties(depots.Depo_A, TRAINS)
duties_B = generate_duties(depots.Depo_B, TRAINS)

#print("Duties for A:")

#for duty in duties_A:
#    print(" -> ".join(train.id for train in duty))
    
print("Duties for B:")

for duty in duties_B:
    print(" -> ".join(train.id for train in duty))
    
print("Duties for A:")

for duty in duties_A:
    print(" -> ".join(train.id for train in duty))