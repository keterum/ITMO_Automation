def test_1_homework():
    assert ('home', 'work') == ('home', 'work')

def test_QAQC():
     assert not 'QA' == 'QC'

def test_numbers_not():
     assert (1, 1, 2, 3, 5) != (2, 3, 5)
