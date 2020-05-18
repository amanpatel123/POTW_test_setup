import check50
from re import match

@check50.check()
def hello_world():
    """hello world"""

    expected = "Hello, World! "
    actual = check50.run("python3 hello_world.py").stdout()

    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)

