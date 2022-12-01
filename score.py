
def compute(dancer_a, dancer_b):
    distance_score = __compute_distance(dancer_a, dancer_b)
    dance_score = __compute_dance(dancer_a, dancer_b)
    return int((distance_score + dance_score)/2);


def __compute_dance(dancer_a, dancer_b):
    def extract_dance_name(dances):
        return dances['dance']['name']
    dances_b_able_to = set(map(extract_dance_name, dancer_b['ableTo']))
    dances_a_wants_to = set(map(extract_dance_name, dancer_a['wantsTo']))
    b_serves_a = 0
    if len(dances_a_wants_to.intersection(dances_b_able_to)) > 0:
        b_serves_a = 100

    dances_a_able_to = set(map(extract_dance_name, dancer_a['ableTo']))
    dances_b_wants_to = set(map(extract_dance_name, dancer_b['wantsTo']))
    a_serves_b = 0
    if len(dances_b_wants_to.intersection(dances_a_able_to)) > 0:
        a_serves_b = 100

    return int((a_serves_b + b_serves_a) / 2)


def __compute_distance(dancer_a, dancer_b):
    from geopy.distance import geodesic
    longitude_a = dancer_a['longitude']
    latitude_a = dancer_a['latitude']
    longitude_b = dancer_b['longitude']
    latitude_b = dancer_b['latitude']
    distance = geodesic((latitude_a, longitude_a),(latitude_b, longitude_b)).km
    result = 100 - (distance / 2 )
    if result<0:
        return 0
    else:
        return result
