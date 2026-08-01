import pytest


def test_empty(pre_post_condition):
    print("test is going")
    print(pre_post_condition)

@pytest.fixture
def pre_post_condition():
    print("Pre conditions started")
    yield "fixture value returned"
    print("Post conditions started")

