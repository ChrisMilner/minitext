from bitstring import BitArray


def get_bits_required_per_char(num_of_chars):
    power = 1

    while (2 ** power) < num_of_chars + 1:
        power += 1
    
    return power


def encode(text):
    unique_chars = list(dict.fromkeys(text))
    bits_per_char = get_bits_required_per_char(len(unique_chars))

    ordered_chars = list(unique_chars)

    encoded = BitArray()

    for c in ordered_chars:
        encoded.append(c.encode("ascii"))
    
    encoded.append('0xff')

    for c in text:
        encoded_char = ordered_chars.index(c)
        encoded.append(BitArray(uint = (encoded_char + 1), length = bits_per_char))

    return bytes(encoded)


def decode(bytes):
    prefix_length = bytes.index(255)
    dictionary = bytes[:prefix_length]

    bits_per_char = get_bits_required_per_char(len(dictionary))

    bits = BitArray(bytes)
    decoded_str = ""

    for i in range((prefix_length + 1) * 8, (len(bytes)) * 8, bits_per_char):
        b = bits[i:i+bits_per_char].uint - 1

        if b < 0:
            break

        decoded_str += chr(dictionary[b])

    return decoded_str
