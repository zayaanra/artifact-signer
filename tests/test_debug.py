import subprocess

logIndex = "128511781"
artifact = "artifact.md"


def test_debug_mode():
    result = subprocess.run(
        ["python", "main.py", "--debug"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "enabled debug mode\n"