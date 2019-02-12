from time import time
import math


class Cache:

    def __init__(self, id, latitude, longitude, capacity):
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
        self.items = {}
        self.max_capacity = capacity

    # store key, value in cache
    def _set(self, key, value, expiration):
        self.items[key] = {
            'value': value,
            'access_time': time(),
            'expiration': expiration,
        }
        if len(self.items) > self.capacity:
            
            items = []
            for key, item in self.items.items():
                if time() <= item['expiration']:
                    items.append((key, item))
            items.sort(key=lambda item: item[1]['access_time'], reverse=True)
            self.items = dict(items[:self.capacity])

    def set(self, key, value, expiration=float('inf')):
        self._set(key, value, expiration)
        for c in caches:
            if c.id != self.id:
                c._set(key, value, expiration)   

    def _get(self, key):
        item = self.items.get(key)
        if item is None:
            return None
        item['access_time'] = time()
        return item['value']

    def __getitem__(self, key):
        value = self._get(key)
        for c in caches:
            if c.id != self.id:
                c._get(key) 
        return value



# Caches distributed at different geo locations
caches = [
    Cache('Montreal', 45.50884, -73.58781, 10),
    Cache('New York', 40.71427, -74.00597, 10),
    Cache('London', 51.50853, -0.12574, 10),
    Cache('Singapore', 1.28967, 103.85007, 10),
]


def distance(lat1, lon1, lat2, lon2):
    """Distance between 2 geo coordinates
    Reference: https://www.movable-type.co.uk/scripts/latlong.html
    """
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    return math.atan2(math.sqrt(a), math.sqrt(1-a))


def get_closest_cache(latitude, longitude):
    d = float('inf')
    ans = None
    for c in caches:
        d2 = distance(latitude, longitude, c.latitude, c.longitude)
        if d2 < d:
            d = d2
            ans = c
    return c


# Test
cache = get_closest_cache(45.50884, -73.58781)
for i in range(10):
    cache.set(i, i)
print(cache[1])
cache.set(10, 10)
cache.set(11, 11)
print(cache[0])
print(cache[1])
print(caches[1][0])
print(caches[1][1])
