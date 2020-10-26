"""
Leetcode: Nearest City

Attempts: 1
Completed: N
Acheived Ideal: 
Under 30 Mins: 

Time Complexity: O(cities * queries) , O(log(cities) * queries) but nlogn time for set up 
Space Complexity: O(1), O(n)

Pattern: 
Technique: 

Problems Encountered:
Other Solutions: Can keep two hashtables of x and y coords with sorted elements in keys. logn search twice 

"""


# Sample Example: Time = O(cities * queries), Space O(1)
def getDistance(x1, x2, y1, y2):
    distance = abs(x1-x2)+abs(y1-y2)
    return distance


def getNeighborCity(cities, x_cor, y_cor, query_city):
    min_dist_city = "None"
    min_distance = math.inf

    # getting the index of the query city in the list of cities to get the query city's X, Y value.
    index = cities.index(query_city)
    x = x_cor[index]
    y = y_cor[index]

    for i in range(len(cities)):
        # getting cities with same x or y coord, ignoring the query city
        if i != index and (x_cor[i] == x or y_cor[i] == y):
            city_distance = getDistance(x, x_cor[i], y, y_cor[i])

            ''' Explanation:
            The given problem have stated that 
            'If two cities have the same distance to the queried city, q[i], consider the one with an alphabetically smaller name (e.e 'ab' < 'aba' < 'abb') as the closest choice.'

            (cityDist == min_distance and cities[i] < queryCity) is checking if the city is lexicographically smaller than the query city
            If true, it means it has an alphabetically smaller name.
            '''
            if city_distance < min_distance or (city_distance == min_distance and cities[i] < query_city):
                min_distance = city_distance
                min_dist_city = cities[i]

    return min_dist_city


def nearestCity(cities, x_cor, y_cor, queries):
    output = []
    for query_city in queries:
        output.append(getNeighborCity(cities, x_cor, y_cor, query_city))

    return output
