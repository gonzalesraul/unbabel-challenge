from datetime import datetime
from sam.stream import getdata,  prettify, mean, process


def test_getdata_no_input():
    assert getdata(None) == (None, None)


def test_getdata_invalid_duration():
    assert getdata({"duration": -1}) == (None, None)


def test_getdata_invalid_timestamp():
    assert getdata({"duration": 0, "timestamp": "2019-13-01 00:00:00"}) == (None, None)


def test_getdata_valid():
    ts, d = getdata({"duration": 10, "timestamp": "2019-01-01 00:00:00"})
    assert isinstance(ts, datetime) and isinstance(d, int)


def test_prettify():
    assert prettify(datetime.fromisoformat("2019-01-01 00:15:00"), 10) == '{ "date": "2019-01-01 00:15:00", "average_delivery_time": 10 }'


def test_mean_slice():
    entries = list(zip([datetime.fromisoformat("2018-12-26T18:%s" % d) for d in ["11:08", "15:19", "23:19"]], [20, 31, 54]))
    assert mean(entries, entries[-1][0], 10) == 42.5
    assert mean(entries, entries.pop()[0], 10) == 31.0
    assert mean(entries, entries.pop()[0], 10) == 20.0
    assert mean(entries, entries.pop()[0], 10) == 0


def test_process():
    import os
    with open(os.path.realpath(os.path.dirname(__file__)+"/files/coverall.jsonl")) as buffer:
        import jsonlines
        iterator = jsonlines.Reader(buffer).iter(type=dict, allow_none=True, skip_empty=True, skip_invalid=True)
        process(iterator, 1)
