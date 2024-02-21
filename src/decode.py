def decode_unsigned(varint: bytes) -> int:
    """
    Decode varint-encoded bytes into an unsigned integer.
    Assumes that the bytes are encoded in little-endian order.
    """
    res = 0
    for byte in reversed(varint):
        res = (res << 7) | (byte & 0x7F)
    return res


def decode_signed(varint: bytes) -> int:
    """
    Decode varint-encoded bytes into a signed integer.
    Assumes that the bytes are encoded in little-endian order.
    """
    n = decode_unsigned(varint)
    return (n >> 1) ^ -(n & 1)
