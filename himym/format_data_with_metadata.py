import re
import os
import json

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
def get_episode_from_path(path):
    return path.split("/")[1].split(" ")[0]


def get_prompts_and_completions_from_lines(lines, character, episode):
    prompts_and_completions = []
    specific_character_regex = "^{}:.*$".format(character)
    # any_character_regex = "^[A-Za-z]+:.*$"
    # narrator_regex = "^Narrator:.*$"

    for line_num in range(6, len(lines)):
        specific_character_match = re.match(specific_character_regex, lines[line_num])
        # any_character_match = re.match(any_character_regex, lines[line_num - 1])
        # narrator_match = re.match(narrator_regex, lines[line_num - 1])

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
                'episode': episode
            })

    return prompts_and_completions


def get_all_prompts_and_completions(character):
    all_prompt_completions = []
    for entry in os.scandir("episodes"):
        episode_lines = open(entry.path).readlines()

        prompts_and_completions = get_prompts_and_completions_from_lines(
            episode_lines,
            character,
            get_episode_from_path(entry.path)
        )

        for prompt_completion in prompts_and_completions:
            all_prompt_completions.append(prompt_completion)

    return all_prompt_completions


all_prompt_completions = get_all_prompts_and_completions("Robin")
for x in all_prompt_completions:
    print(x['episode'])
    print(x['prompt'])

with open("non_dialogue_with_long_prompts/sample.json", "w") as outfile:
    json.dump(all_prompt_completions, outfile, indent=4)

# need a robust-ish way to determine if something is in a flashback
# the most difficult part here is determining when something isn't in a flashback
# some ways that flashbacks start
#   (flashback ...)
#   [FLASHBACK]

# total_episodes = 0
# episodes_with_flashbacks = 0
#
# for entry in os.scandir("episodes"):
#     episode_lines = open(entry.path).readlines()
#     scene_regex = "^(\\(flashback.*|\\[FLASHBACK])$"
#     total_episodes += 1
#
#     for line in episode_lines:
#         match = re.match(scene_regex, line)
#         if match:
#             episodes_with_flashbacks += 1
#             print(entry.path)
#             break
#
# print(total_episodes)
# print(episodes_with_flashbacks)
