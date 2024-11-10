from main import get_verification_proof
from jsonschema import validate


logIndex = "128511781"

verificationSchema = {
    "type": "object",
    "verification": {
        "type": "object",
        "properties": {
            "inclusionProof": {
                "type": "object",
                "properties": {
                    "checkpoint": {"type": "string"},
                    "hashes": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "logIndex": {"type": "integer"},
                    "rootHash": {"type": "string"},
                    "treeSize": {"type": "integer"}
                },
                "required": ["checkpoint", "hashes", "logIndex", "rootHash", "treeSize"]
            },
            "signedEntryTimestamp": {"type": "string"}
        },
        "required": ["inclusionProof", "signedEntryTimestamp"]
    }
}

def test_get_valid_verification():
    verification = get_verification_proof(logIndex)
    assert verification

def test_get_invalid_verification():
    verification = get_verification_proof("-1")
    assert not verification

def test_verification_schema():
    verification = get_verification_proof(logIndex)
    validate(instance=verification, schema=verificationSchema)