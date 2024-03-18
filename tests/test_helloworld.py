import pytest
from hellotools.helloworld import hello_world # remember: from package.module import function

def test_hello_world():
    output = hello_world()
    assert output == "Hello, world take 2!"