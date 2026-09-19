class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = sorted(zip(position, speed), key = lambda c: c[0], reverse = True)

        fleets = 0
        current_slowest_arrival = 0.0

        for pos, spd in cars:
            arrival_time = (target - pos) / spd

            if arrival_time > current_slowest_arrival:
                fleets += 1
                current_slowest_arrival = arrival_time
            
        return fleets