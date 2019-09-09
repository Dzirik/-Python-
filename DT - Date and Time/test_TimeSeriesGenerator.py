import TimeSeriesGenerator as TSG


def test_size_month():
    tsg = TSG.TimeSeriesGenerator()
    ts = tsg.generate_month_data()
    assert len(ts) == 30


def test_size_day():
    tsg = TSG.TimeSeriesGenerator()
    ts = tsg.generate_day_data()
    assert len(ts) == 30 and len(ts[0]) == 2


def test_size_week():
    tsg = TSG.TimeSeriesGenerator()
    ts = tsg.generate_week_data()
    assert len(ts) == 30 and len(ts[0]) == 2


def test_size_month():
    tsg = TSG.TimeSeriesGenerator()
    ts = tsg.generate_month_data()
    assert len(ts) == 30 and len(ts[0]) == 2
