import re
import os


def get_character_speech_from_text(character_name, lines):
    regex = "^{}:.*$".format(character_name)
    matched_lines = []

    for line in lines:
        match = re.match(regex, line)
        if match:
            matched_lines.append(line)

    return matched_lines


def get_character_speech(character_name):
    all_matched_lines = []
    directory = "./episodes"

    for entry in os.scandir(directory):
        if not entry.is_file():
            continue

        file = open(entry.path)
        lines = file.readlines()
        matched_lines = get_character_speech_from_text(character_name, lines)

        for line in matched_lines:
            all_matched_lines.append(line)

    return all_matched_lines


def generate_character_speech_file(character_name):
    character_lines = get_character_speech(character_name)

    speech_file = open("./character_speech/{}-{}".format(character_name, len(character_lines)), "w")
    for line in character_lines:
        speech_file.write("{}\n".format(line.rstrip()))


generate_character_speech_file("Claire")
