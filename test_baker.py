import pytest
from baker import cake


# STEP 1: write the production code to ensure the test passes.
def test_returns_0_if_no_ingredients_available():
    available = {}
    recipe = {"flour": 400}
    max_cakes = cake(available, recipe)
    assert max_cakes == 0


# STEP 2: now it's time to write your own tests.
def test_returns_2_if_ingredients_are_enough():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    max_cakes = cake(available, recipe)
    assert max_cakes == 2
