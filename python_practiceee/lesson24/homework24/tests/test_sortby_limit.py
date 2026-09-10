import pytest
from python_practiceee.lesson24.homework24.tests.conftest import BASE_URL

@pytest.mark.parametrize("sort_by, limit", [
    ("brand", 5),
    ("year", 10),
    ("price", 3),
    ("engine_volume", 7),
    ("brand", None)
])
def test_sort_by_limit(auth_session, sort_by, limit):
    params = {"sort_by": sort_by, "limit": limit}

    response = auth_session.get(f"{BASE_URL}/cars", params=params)

    assert response.status_code == 200

    data = response.json()
    if limit is not None:
        assert len(data) == limit

    if sort_by is not None:
        values = [car[sort_by] for car in data]
        assert values == sorted(values)

