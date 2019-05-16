from pytest import approx
from finsim.mortgage import Mortgage

def test_calc_payment():
    m = Mortgage(200000, 6.0)

    assert m.calc_payment() == approx(1199.1)


def test_calc_total_cost():
    m = Mortgage(200000, 6.0, 30*12)

    assert m.calc_total_cost() == approx(431676.38)


def test_calc_total_cost_short_term():
    m = Mortgage(200000, 6.0, 15*12)

    assert m.calc_total_cost() == approx(303788.46)


def test_custom_payoff_cost():
    m = Mortgage(200000, 6.0, 30*12)

    assert m.custom_payoff_cost(2000)[0] == approx(277951, rel=0.001)


def test_custom_payoff_with_lump():
    """What happens with a lump sum payment 1 year in?"""
    m = Mortgage(200000, 6.0, 30*12)

    assert m.custom_payoff_cost(2000, lumps={12: 1000})[0] == approx(277058, rel=0.001)
