import subprocess

logIndex = "128511781"
artifact = "artifact.md"

def test_valid_inclusion():
    result = subprocess.run(
        ["python", "main.py", "--inclusion", logIndex, "--artifact", artifact],
        capture_output=True,
        text=True
    )

    assert result.stdout == "Verified inclusion\n"

def test_invalid_inclusion_logIndex():
    result = subprocess.run(
        ["python", "main.py", "--inclusion", "-1", "--artifact", artifact],
        capture_output=True,
        text=True
    )

    assert result.stdout == "No log entry found for given log index\n"

def test_invalid_inclusion_artifact():
    result = subprocess.run(
        ["python", "main.py", "--inclusion", logIndex, "--artifact", "fakefile"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "Failed to verify inclusion of log index 128511781 with artifact fakefile: [Errno 2] No such file or directory: 'fakefile'\n"
