def encode_unsigned(n: int) -> bytes:
    """
    Encode an unsigned integer into variable-length bytes using varint encoding.
    Returns the varint-encoded bytes in little-endian order.
    """
    if n < 0:
        raise ValueError("Negative value provided: {}".format(n))
    res = []
    while True:
        byte = n & 0x7F
        n >>= 7
        if n:
            byte |= 0x80
        res.append(byte)
        if not n:
            break

    return bytes(res)


def encode_signed(n: int) -> bytes:
    """
    Encode a signed integer into variable-length bytes using varint encoding.
    Returns the varint-encoded bytes in little-endian order.
    """
    zigzag = (n << 1) ^ (n >> 63)
    return encode_unsigned(zigzag)
