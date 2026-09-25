
from xmlrpc import client


def test_health_check():
    response = client.get("/health/")
    
    assert ...
    assert ...