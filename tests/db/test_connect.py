from sqlalchemy import create_engine


def test_connect_is_alive():
    engine = create_engine('postgresql://myuser:mypassword@localhost:5432/mydb');
    assert engine == True