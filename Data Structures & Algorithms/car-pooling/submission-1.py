class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickups = defaultdict(int)
        dropoffs = defaultdict(int)
        minx, maxx = trips[0][1], trips[0][2]
        for arr in trips:
            pickups[arr[1]] += arr[0]
            dropoffs[arr[2]] += arr[0]
            minx = min(minx, arr[1])
            maxx = max(maxx, arr[2])
            
        arr = [0] * (maxx-minx+1)
        for k,v in pickups.items():
            arr[k-minx] += v
        for k,v in dropoffs.items():
            arr[k-minx] -= v
        curr_passengers = 0
        for num in arr:
            curr_passengers += num
            if curr_passengers > capacity:
                return False
        return True
