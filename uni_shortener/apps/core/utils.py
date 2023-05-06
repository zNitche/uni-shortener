import uuid


def generate_url_hash(hash_length=6):
    return uuid.uuid4().hex[:hash_length]
