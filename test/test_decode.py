from src.decode import decode_unsigned, decode_signed

assert decode_unsigned(b"\x96\x01") == 150
assert decode_unsigned(b"\xA4\x0A") == 1316
assert decode_unsigned(b"\x8E\xF5\x81\xB8\x23") == 9512712846
assert decode_unsigned(b"\x00") == 0

assert decode_signed(b"\x06") == 3
assert decode_signed(b"\x05") == -3
assert decode_signed(b"\xC8\x14") == 1316
assert decode_signed(b"\xC7\x14") == -1316
assert decode_signed(b"\x00") == 0
