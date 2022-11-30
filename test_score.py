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

dancer_b_dortmund_tango = {
    'id': '0001aaa0-f0c4-4716-9382-d2d3c3c49117',
    'size': 100,
    'gender': 'MALE',
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
    distance_score = score.__compute_distance(dancer_a_dortmund_tango, dancer_b_dortmund_tango)
    assert distance_score < 50


if __name__ == "__main__":
    test_distance()