from src.encode import encode_unsigned, encode_signed

assert encode_unsigned(150) == b"\x96\x01"
assert encode_unsigned(1316) == b"\xA4\x0A"
assert encode_unsigned(9512712846) == b"\x8E\xF5\x81\xB8\x23"
assert encode_unsigned(0) == b"\x00"

assert encode_signed(3) == b"\x06"
assert encode_signed(-3) == b"\x05"
assert encode_signed(1316) == b"\xC8\x14"
assert encode_signed(-1316) == b"\xC7\x14"
assert encode_signed(0) == b"\x00"
