import re
import os
import csv
import math


def get_prompts_and_completions_from_lines(lines, character):
    prompts_and_completions = []

    for line_num in range(len(lines)):
        regex = "^{}:.*$".format(character)
        match = re.match(regex, lines[line_num])

        if match and line_num != 0:
            prompts_and_completions.append({'prompt': lines[line_num - 1], 'completion': lines[line_num]})

    return prompts_and_completions


def get_all_prompts_and_completions(character):
    all_prompt_completions = []
    for entry in os.scandir("episodes"):
        episode_lines = open(entry.path).readlines()
        for prompt_completion in get_prompts_and_completions_from_lines(episode_lines, character):
            all_prompt_completions.append(prompt_completion)

    return all_prompt_completions


def write_prompts_and_completions_to_csv(character):
    all_prompts_and_completions = get_all_prompts_and_completions(character)

    num_prompts_completions = len(all_prompts_and_completions)

    num_train = math.floor(0.8 * num_prompts_completions)

    train_data = all_prompts_and_completions[:num_train]
    validation_data = all_prompts_and_completions[num_train:]

    fields = ["prompt", "completion"]
    train_rows = []
    validation_rows = []

    for prompt_completion in train_data:
        prompt = prompt_completion["prompt"]
        completion = prompt_completion["completion"]

        train_rows.append([" {}\n".format(prompt.rstrip()), " {}\n".format(completion.rstrip())])

    for prompt_completion in validation_data:
        prompt = prompt_completion["prompt"]
        completion = prompt_completion["completion"]

        validation_rows.append([" {}\n".format(prompt.rstrip()), " {}\n".format(completion.rstrip())])

    out_train_file = open("{}_TRAINING.csv".format(character), "w")
    out_validation_file = open("{}_VALIDATION.csv".format(character), "w")

    train_writer = csv.writer(out_train_file)
    validation_writer = csv.writer(out_validation_file)

    train_writer.writerow(fields)
    train_writer.writerows(train_rows)

    validation_writer.writerow(fields)
    validation_writer.writerows(validation_rows)

    out_train_file.close()
    out_validation_file.close()


write_prompts_and_completions_to_csv("Ted")

