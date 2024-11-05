import subprocess

def test_invalid_logIndex():
    result = subprocess.run(
        ["python", "main.py", "--inclusion -1", "--artifact artifact.md"],
        capture_output=True,
        text=True
    )
    output = result.stdout

    assert output == "No log entry found for given log index"