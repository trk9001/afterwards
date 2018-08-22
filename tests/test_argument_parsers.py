from aw.afterwards import AwArgumentParser
from .context import SysOverwrite


sys = SysOverwrite()
parser = AwArgumentParser()


def test_parse_for_date_relative():
    sys.build_args('today 1337 Eat, code and sleep.')
    parser.arg_i = 0
    assert parser.parse_for_date() == 'today'


def test_parse_for_date_words():
    sys.build_args('Feb 29 1337 Eat, code and sleep.')
    parser.arg_i = 0
    assert parser.parse_for_date() == 'Feb 29'


def test_parse_for_date_numeric():
    sys.build_args('02/29 1337 Eat, code and sleep.')
    parser.arg_i = 0
    assert parser.parse_for_date() == 'February 29'


def test_parse_for_date_failure():
    sys.build_args('LMAO 1337 Eat, code and sleep.')
    parser.arg_i = 0
    assert parser.parse_for_date() is None


def test_parse_for_time_24hr():
    sys.build_args('today 1337 Eat, code and sleep.')
    parser.arg_i = 1
    assert parser.parse_for_time() == '1337'


def test_parse_for_time_12hr():
    sys.build_args('today 1:37 pm Eat, code and sleep.')
    parser.arg_i = 1
    assert parser.parse_for_time() == '1:37 PM'


def test_parse_for_time_failure():
    sys.build_args('today 42 Eat, code and sleep.')
    parser.arg_i = 1
    assert parser.parse_for_time() is None


def test_parse_for_msg():
    sys.build_args('today 1337 Eat, code and sleep.')
    parser.arg_i = 2
    assert parser.parse_for_msg() == 'Eat, code and sleep.'
