### Design Underground System

"""
An underground railway system is kee

ping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel 
from one station to another.

Implement the UndergroundSystem class:

    void checkIn(int id, string stationName, int t)
        A customer with a card ID equal to id, checks in at the station stationName at time t.
        A customer can only be checked into one place at a time.
    void checkOut(int id, string stationName, int t)
        A customer with a card ID equal to id, checks out from the station stationName at time t.
    double getAverageTime(string startStation, string endStation)
        Returns the average time it takes to travel from startStation to endStation.
        The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning
         a check in at startStation followed by a check out from endStation.
        The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
        There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, 
then t1 < t2. All events happen in chronological order.
"""


class UndergroundSystem:
    def __init__(self):
        self.full_trips = {} ## contains the times from one station to the other (completed trips)
        self.current_clients = {} ## contains clients that checked in haven't checked out yet


    def checkIn(self, id: int, stationName: str, t:int) -> None:
        ## we add the new client to stationName
        self.current_clients[id] = [stationName, t] ## we suppose a client can't check in twice so we don't care about a potential stored check in

    def checkOut(self, id: int, stationName: str, t:int) -> None:
        if(id not in self.current_clients):
            print("Client ", id, " has not check in yet")
            return

        startStation, checkin_time = self.current_clients[id]

        
        if(startStation in self.full_trips):
            trip_stat = self.full_trips[startStation].get(stationName, [0, 0])
            self.full_trips[startStation][stationName] = [trip_stat[0] + t - checkin_time, trip_stat[1] + 1]
        else :
            self.full_trips[startStation] = {stationName : [t - checkin_time, 1]}
        
        
            
        

    def getAverage(self, startStation: str, endStation: str) -> float :
        tot_time, t = self.full_trips[startStation][endStation]

        return tot_time / t

if __name__ == "__main__":
    u = UndergroundSystem()

    u.checkIn(45, "Leyton", 3)
    u.checkIn(32,"Paradise",8)
    u.checkIn(27,"Leyton",10)
    u.checkOut(45,"Waterloo",15)
    u.checkOut(27,"Waterloo",20)
    u.checkOut(32,"Cambridge",22)
    print(u.getAverage("Paradise","Cambridge"), " (expected : 14.0)")
    print(u.getAverage("Leyton", "Waterloo"), " (expected : 11.0)")
    u.checkIn(10, "Leyton", 24)
    print(u.getAverage("Leyton", "Waterloo"), " (expected : 11.0)")
    u.checkOut(10, "Waterloo", 38)
    print(u.getAverage("Leyton", "Waterloo"), " (expected : 12.0)")
    


    
