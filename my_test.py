from subscription import interval 

def test_interval():    # note the function name is prefixed with "test_"
    result = subscription.interval(2,3)  # directly invoke the function we want to test
    assert result == 5 # describe expectations for desired behavior