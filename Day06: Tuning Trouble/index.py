def load_data():
    with open("input.txt", "r") as outfile:
        return outfile.read()


def is_marker(signal_extract: str):
    # Returns True if all characters in signal extract are unique else False
    signal_chars = sorted(list(signal_extract))
    removed_duplicates = sorted(list(set(signal_chars)))
    all_characters_unique = signal_chars == removed_duplicates
    return all_characters_unique


def find_distinct_character_sequence_indexes(input_string, distinct_length):
    indexes: list[int] = []
    for char_index in range(0, len(input_string) - distinct_length):
        scan = input_string[char_index:char_index + distinct_length]
        if is_marker(scan):
            indexes.append(
                char_index + distinct_length
            )
    return indexes


def find_packet_indexes(signal: str, signal_width=4) -> list[int]:
    packets: list[int] = []
    for char_index in range(0, len(signal) - signal_width):
        scan = signal[char_index:char_index + signal_width]
        if is_marker(scan):
            packets.append(
                char_index + signal_width
            )
    return packets


def get_first_packet_index(input_signal):
    packets = find_packet_indexes(input_signal, signal_width=4)
    return packets[0]


def get_first_start_of_message_marker_index(input_signal):
    packets = find_packet_indexes(input_signal, signal_width=14)
    return packets[0]


if __name__ == "__main__":
    SIGNAL_DATA = load_data()
    first_packet_index = get_first_packet_index(SIGNAL_DATA)
    print(first_packet_index)
    first_start_of_message_marker_index = get_first_start_of_message_marker_index(SIGNAL_DATA)
    print(first_start_of_message_marker_index)
