from aw.afterwards import AwArgumentParser


def test_parse_for_date_relative():
    cmd = 'aw today 1337 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    assert parser.parse_for_date() == 'today'


def test_parse_for_date_words():
    cmd = 'aw Feb 29 1337 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    assert parser.parse_for_date() == 'feb 29'


def test_parse_for_date_numeric():
    cmd = 'aw 02/29 1337 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    assert parser.parse_for_date() == 'february 29'


def test_parse_for_date_failure():
    cmd = 'aw LMAO 1337 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    assert parser.parse_for_date() is None


def test_parse_for_time_24hr():
    cmd = 'aw today 1337 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    parser.parse_for_date()
    assert parser.parse_for_time() == '1337'


def test_parse_for_time_12hr():
    cmd = 'aw today 1:37 pm Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    parser.parse_for_date()
    assert parser.parse_for_time() == '1:37 PM'


def test_parse_for_time_failure():
    cmd = 'aw today 42 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    parser.parse_for_date()
    assert parser.parse_for_time() is None


def test_parse_for_msg():
    cmd = 'aw today 1337 Eat, code and sleep.'
    parser = AwArgumentParser(cmd.split())
    parser.parse_for_date()
    parser.parse_for_time()
    assert parser.parse_for_msg() == 'Eat, code and sleep.'
