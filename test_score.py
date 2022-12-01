dancer_a_dortmund_tango = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'MALE',
    'aboutMe': 'lorem ipsum',
    'country': 'GER',
    'version': 2,
    'latitude': 51.4971776748,
    'birthDate': '1991-02-01T00:00:00.000+00:00',
    'longitude': 7.46266673743,
    'updatedAt': '2022-11-09T05:38:40.609184112Z',
    'dancerName': '191-test',
    'ableTo': [
        {
            'dance':
                {
                    'name': 'Tango'
                },
            'level': 'INTERMEDIATE',
            'leading': 'LEAD'
        }
    ],
    'wantsTo': [
        {
            'dance': {
                'name': 'Tango'
            },
            'level': 'INTERMEDIATE',
            'leading': 'FOLLOW'}
    ]
}

dancer_b_dortmund_tango = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'FEMALE',
    'aboutMe': 'lorem ipsum',
    'country': 'GER',
    'version': 2,
    'latitude': 51.5280482482,
    'birthDate': '1991-02-01T00:00:00.000+00:00',
    'longitude': 7.44121565558,
    'updatedAt': '2022-11-09T05:38:40.609184112Z',
    'dancerName': '191-test',
    'ableTo': [
        {
            'dance':
                {
                    'name': 'Tango'
                },
            'level': 'INTERMEDIATE',
            'leading': 'LEAD'
        }
    ],
    'wantsTo': [
        {
            'dance': {
                'name': 'Tango'
            },
            'level': 'INTERMEDIATE',
            'leading': 'FOLLOW'}
    ]
}

dancer_c_essen_tango = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'MALE',
    'aboutMe': 'lorem ipsum',
    'country': 'GER',
    'version': 2,
    'latitude': 51.4465703338,
    'birthDate': '1991-02-01T00:00:00.000+00:00',
    'longitude': 6.97631009431,
    'updatedAt': '2022-11-09T05:38:40.609184112Z',
    'dancerName': '191-test',
    'ableTo': [
        {
            'dance':
                {
                    'name': 'Tango'
                },
            'level': 'INTERMEDIATE',
            'leading': 'LEAD'
        }
    ],
    'wantsTo': [
        {
            'dance': {
                'name': 'Tango'
            },
            'level': 'INTERMEDIATE',
            'leading': 'FOLLOW'}
    ]
}

dancer_d_essen_salsa = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'MALE',
    'aboutMe': 'lorem ipsum',
    'country': 'GER',
    'version': 2,
    'latitude': 51.4465703338,
    'birthDate': '1991-02-01T00:00:00.000+00:00',
    'longitude': 6.97631009431,
    'updatedAt': '2022-11-09T05:38:40.609184112Z',
    'dancerName': '191-test',
    'ableTo': [
        {
            'dance':
                {
                    'name': 'Salsa'
                },
            'level': 'INTERMEDIATE',
            'leading': 'LEAD'
        }
    ],
    'wantsTo': [
        {
            'dance': {
                'name': 'Salsa'
            },
            'level': 'INTERMEDIATE',
            'leading': 'FOLLOW'}
    ]
}

dancer_f_essen_tango = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'MALE',
    'aboutMe': 'lorem ipsum',
    'country': 'GER',
    'version': 2,
    'latitude': 51.4465703338,
    'birthDate': '1991-02-01T00:00:00.000+00:00',
    'longitude': 6.97631009431,
    'updatedAt': '2022-11-09T05:38:40.609184112Z',
    'dancerName': '191-test',
    'ableTo': [
        {
            'dance':
                {
                    'name': 'Tango'
                },
            'level': 'INTERMEDIATE',
            'leading': 'LEAD'
        }
    ],
    'wantsTo': [
        {
            'dance': {
                'name': 'Tango'
            },
            'level': 'INTERMEDIATE',
            'leading': 'FOLLOW'}
    ]
}


dancer_not_scorable = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'MALE',
    'aboutMe': 'lorem ipsum',
    'country': 'GER',
    'version': 2,
    'birthDate': '1991-02-01T00:00:00.000+00:00',
    'updatedAt': '2022-11-09T05:38:40.609184112Z',
    'dancerName': '191-test',
    'ableTo': [
        {
            'dance':
                {
                    'name': 'Lindy-Hop'
                },
            'level': 'INTERMEDIATE',
            'leading': 'LEAD'
        }
    ],
    'wantsTo': [
        {
            'dance': {
                'name': 'Lindy-Hop'
            },
            'level': 'INTERMEDIATE',
            'leading': 'FOLLOW'}
    ]
}


def test_distance():
    import score
    distance_score_two_in_same_city = score.__compute_distance(dancer_a_dortmund_tango, dancer_b_dortmund_tango)
    assert distance_score_two_in_same_city > 50
    
    distance_score_dortmund_essen = score.__compute_distance(dancer_a_dortmund_tango, dancer_c_essen_tango)
    assert  distance_score_dortmund_essen < distance_score_two_in_same_city


def test_dance():
    import score
    dancer_score_with_matching_dances = score.__compute_dance(dancer_a_dortmund_tango, dancer_f_essen_tango)
    dance_score_with_different_dances = score.__compute_dance(dancer_a_dortmund_tango, dancer_d_essen_salsa)
    assert dancer_score_with_matching_dances > dance_score_with_different_dances
    pass


def test_compute():
    import score
    same_city_not_matching_dances = score.compute(dancer_d_essen_salsa, dancer_f_essen_tango)
    different_city_matching_dances = score.compute(dancer_a_dortmund_tango, dancer_c_essen_tango)
    assert different_city_matching_dances > same_city_not_matching_dances


if __name__ == "__main__":
    test_distance()
    test_dance()
    test_compute()