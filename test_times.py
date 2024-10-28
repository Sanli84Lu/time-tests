from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_overlap(range1, range2):
    overlap_time = compute_overlap_time(range1, range2)
    assert overlap_time is not None

def test_gap(range1, range2):
    gap_number_1 = len(range1)
    gap_number_2 = len(range2)
    print('gap in 1:', gap_number_1, 'and gap in 2:', gap_number_2)
    assert gap_number_1 > 1 and gap_number_2 > 1

def test_end_start(range1, range2):
    assert range1[0][0] == range2[-1][-1] or range1[-1][-1] == range2[0][0]



if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    test_overlap(large,short)
    # test_gap(large,short)
    test_end_start(large,short)