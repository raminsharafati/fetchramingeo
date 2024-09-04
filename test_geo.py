import subprocess

def run_utility(*args):
    command = ['python', 'ramingeoloc_util.py'] + list(args)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def test_geo():
    # I'm testing valid inputs
    output = run_utility('--locations', 'Madison, WI', '12345', 'Chicago, IL', '10001')
    assert "Place: Madison" in output
    assert "Latitude:" in output
    assert "Longitude:" in output
    assert "Place: 12345" in output
    assert "Place: Chicago" in output
    assert "Place: 10001" in output

    # I'm testing invalid input
    output = run_utility('--locations', 'InvalidCity, ZZ', '00000')
    assert "error" in output.lower()

    # I'm testing empty input
    output = run_utility('--locations')
    assert "error" in output.lower()

    # I'm testing single city and zip code
    output = run_utility('--locations', 'New York, NY', '10001')
    assert "Place: New York" in output
    assert "Place: 10001" in output
    assert "Latitude:" in output
    assert "Longitude:" in output

    # I'm testing for cases where the API might return multiple locations
    output = run_utility('--locations', 'Los Angeles, CA', '90001')
    assert "Place: Los Angeles" in output
    assert "Latitude:" in output
    assert "Longitude:" in output

if __name__ == '__main__':
    test_geo()
    print("All tests passed!")
