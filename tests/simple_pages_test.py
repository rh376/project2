"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/About">About</a>' in response.data
    assert b'<a class="nav-link" href="/Git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python-flask">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/integrate-deploy">Integrate & Deploy</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/About")
    assert response.status_code == 200

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/python-flask")
    assert response.status_code == 200

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/integrate-deploy")
    assert response.status_code == 200

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
