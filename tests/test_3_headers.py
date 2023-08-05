import re
from utils.assertion import Assert

from api.httpbin_api import http_bin_api
from http import HTTPStatus


def test_list_html():
    res_http = http_bin_api.list_html()

    assert res_http.status_code == HTTPStatus.OK
    assert res_http.headers ['Content-Type'] == 'text/html; charset=utf-8'

def test_robots():
    res_rpbots = http_bin_api.robots_txt()

    assert res_rpbots.status_code == HTTPStatus.OK
    assert res_rpbots.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(f'.*User-agent: \*.*Disallow: /deny.*',res_rpbots.text, flags=re.DOTALL)



def test_ip():
    res_ip = http_bin_api.ip()

    assert res_ip.status_code == HTTPStatus.OK
    if res_ip.headers['Content-Type'] == 'application/json':
        Assert.validate_schema(res_ip.json())

        origin = res_ip.json()['origin']
        assert re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', origin)