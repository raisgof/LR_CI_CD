def new_feature():
    return "This is a new feature for testing CI/CD"
def test_new_feature():
    result = new_feature()
    assert "new feature" in result
