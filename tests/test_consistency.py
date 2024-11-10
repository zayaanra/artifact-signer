import subprocess


def test_invalid_consistency_treeID():
    result = subprocess.run(
        ["python", "main.py", "--consistency", "--tree-id", "0", "--tree-size", "25265395", "--root-hash", "d64b670178e87d19fbc9b9d33f06b0ca3e04e536265f38bffd947eef72c791b6"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "Failed to verify consistency proof from Rekor Server public instance:  'hashes'\n"

def test_invalid_consistency_treeSize():
    result = subprocess.run(
        ["python", "main.py", "--consistency", "--tree-id", "1193050959916656506", "--tree-size", "0", "--root-hash", "d64b670178e87d19fbc9b9d33f06b0ca3e04e536265f38bffd947eef72c791b6"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "Failed to verify consistency proof from Rekor Server public instance:  'hashes'\n"   

def test_invalid_consistency_rootHash():
    result = subprocess.run(
        ["python", "main.py", "--consistency", "--tree-id", "1193050959916656506", "--tree-size", "25265395", "--root-hash", "x"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "root hash must be 64 characters long\n"   

def test_consistency_no_treeID():
    result = subprocess.run(
        ["python", "main.py", "--consistency"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "please specify tree id for prev checkpoint\n"

def test_consistency_no_treeSize():
    result = subprocess.run(
        ["python", "main.py", "--consistency", "--tree-id", "1193050959916656506"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "please specify tree size for prev checkpoint\n"

def test_consistency_no_rootHash():
    result = subprocess.run(
        ["python", "main.py", "--consistency", "--tree-id", "1193050959916656506", "--tree-size", "25996967"],
        capture_output=True,
        text=True
    )

    assert result.stdout == "please specify root hash for prev checkpoint\n"