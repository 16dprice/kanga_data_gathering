import re
import os
import json
import datetime

# Desired Fields
# prompt
# completion
# episode
# scene
# show name
# source (e.g., website URL)
# retrieval_date (i.e. when data originally captured)
# created_date (i.e. when data created)


# prompt will be calculated during parsing
# completion will also be calculated during parsing
# episode will be easily calculated by parsing filename (this should just be 01x01 or 02x08, for example)
# show name is How I Met Your Mother
# source can be retrieved by looking up in page_urls.json
# retrieval_date should be sometime in November or something
# created_date should be current date when code is running


# Path is path of episode file relative to this file.
# So, an example path is "episodes/08x06 - Splitsville"
def get_episode_number_from_path(path):
    return path.split("/")[1].split(" ")[0]


def get_episode_url(path):
    return json.load(open("page_urls.json", "r"))[path.split("/")[1]]


def get_previous_six_lines_of_dialogue(lines, current_line_num):
    any_character_regex = "^[A-Za-z]+:.*$"
    prompt = ""

    matches_found = 0
    for line_num in range(current_line_num - 1, -1, -1):

        match = re.match(any_character_regex, lines[line_num])
        if match:
            prompt += lines[line_num]
            matches_found += 1

        if matches_found == 6:
            return prompt

    return prompt


def get_prompts_and_completions_from_lines(lines, character, episode_path, only_dialogue):
    prompts_and_completions = []
    specific_character_regex = "^{}:.*$".format(character)

    for line_num in range(6, len(lines)):
        specific_character_match = re.match(specific_character_regex, lines[line_num])

        if only_dialogue:
            prompt = get_previous_six_lines_of_dialogue(lines, line_num)
        else:
            prompt = "{}{}{}{}{}{}".format(
                lines[line_num - 6],
                lines[line_num - 5],
                lines[line_num - 4],
                lines[line_num - 3],
                lines[line_num - 2],
                lines[line_num - 1]
            )

        if specific_character_match:
            prompts_and_completions.append({
                'prompt': prompt,
                'completion': lines[line_num],
                'episode': get_episode_number_from_path(episode_path),
                'source_url': get_episode_url(episode_path)
            })

    return prompts_and_completions


def get_all_prompts_and_completions(character, only_dialogue=True):
    all_prompt_completions = []
    for entry in os.scandir("episodes"):
        episode_lines = open(entry.path).readlines()

        prompts_and_completions = get_prompts_and_completions_from_lines(
            episode_lines,
            character,
            entry.path,
            only_dialogue
        )

        for prompt_completion in prompts_and_completions:
            all_prompt_completions.append(prompt_completion)

    return all_prompt_completions


# characters = ["Robin", "Ted", "Lily", "Marshall", "Barney"]
# only_dialogue = True
#
# for character in characters:
#     all_prompt_completions = get_all_prompts_and_completions(character, only_dialogue)
#
#     if only_dialogue:
#         file_path = "only_dialogue_with_long_prompts/{}.json".format(character.lower())
#     else:
#         file_path = "non_dialogue_with_long_prompts/{}.json".format(character.lower())
#
#     with open(file_path, "w") as outfile:
#         retrieval_date = str(datetime.datetime(2020, 10, 19, 20, 51))
#         created_date = str(datetime.datetime.now())
#         sorted_prompt_completions = sorted(all_prompt_completions, key=lambda item: item['episode'])
#
#         json_data = {
#             'source_name': 'How I Met Your Mother',
#             'retrieval_date': retrieval_date,
#             'created_date': created_date,
#             'training_data': sorted_prompt_completions
#         }
#
#         json.dump(json_data, outfile, indent=4)

