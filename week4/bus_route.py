class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0

        routes_has_stops = dict()
        stops_in_routes = dict()

        for i, stops in enumerate(routes):
            routes_has_stops[i] = stops
            for stop in stops:
                if stop in stops_in_routes:
                    stops_in_routes[stop].append(i)
                else:
                    stops_in_routes[stop] = [i]

        if source not in stops_in_routes:
            return -1
        for route in stops_in_routes[source]:
            if target in routes_has_stops[route]:
                return 1

        visited = [False] * len(routes_has_stops)
        back_tracking = [i for i in range(len(routes_has_stops))]
        q = deque()
        for source_route in stops_in_routes[source]:
            q.append(source_route)
            visited[source_route] = True
        target_acquired = False
        counter = 0
        while len(q) != 0:
            current_route = q.popleft()
            if target in routes_has_stops[current_route]:
                last_route = current_route
                target_acquired = True
                break
            else:
                for stop in routes_has_stops[current_route]:
                    for route in stops_in_routes[stop]:
                        if not visited[route]:
                            q.append(route)
                            visited[route] = True
                            back_tracking[route] = current_route
        if not target_acquired:
            return -1
        back_track_route = last_route
        counter = 1
        while source not in routes_has_stops[back_track_route]:
            back_track_route = back_tracking[back_track_route]
            counter += 1
        return counter
