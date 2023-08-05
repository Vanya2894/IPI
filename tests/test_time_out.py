from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_time_out():
    res = http_bin_api.time_out(25)
    assert res.status_code == HTTPStatus.OK

def test_2_time_out():
    res_two = http_bin_api.time_out(2)
    assert not res_two[0]