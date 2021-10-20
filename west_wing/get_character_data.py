import re
import os


def get_character_speech_from_text(character_name, lines):
    matched_lines = []

    for line_num in range(len(lines)):
        if lines[line_num] == "{}\n".format(character_name):

            character_text = ""
            line_num += 1
            while lines[line_num] != "\n":
                character_text = "{} {}".format(character_text.rstrip(), lines[line_num].rstrip())
                line_num += 1

            matched_lines.append("{}: {}".format(character_name, character_text))

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


generate_character_speech_file("TOBY")
