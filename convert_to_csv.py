import csv
import math


def write_lines_to_csv(lines, out_file_name):
    out_file = open("{}.csv".format(out_file_name), "w")

    fields = ["prompt", "completion"]
    rows = []
    for line in lines:
        rows.append(["", " {}\n".format(line.rstrip())])

    csv_writer = csv.writer(out_file)

    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

    out_file.close()


with open("himym/character_speech/Robin-4007") as character_file:
    all_lines = character_file.readlines()
    num_lines = len(all_lines)

    train_percentage = 0.8
    num_train_lines = math.floor(train_percentage * num_lines)

    train_lines = all_lines[:num_train_lines]
    validation_lines = all_lines[num_train_lines:]

    write_lines_to_csv(train_lines, "robin_train_lines")
    write_lines_to_csv(validation_lines, "robin_validation_lines")

    # write_lines_to_csv(character_file.readlines(), "ted")

# To prepare data and send to a .jsonl file that is formatted properly
# openai tools fine_tunes.prepare_data -f <filename>

# To run a fine-tune job after the data has been prepared (<model> is typically 'curie')
# openai api fine_tunes.create -t <filename> -m <model>

# To run a fine-tune job after the data has been prepared with validation (<model> is typically 'curie')
# openai api fine_tunes.create -t <train_filename> -v <validation_filename> -m <model>

# List all created fine-tunes
# openai api fine_tunes.list

# Robin model (no validation): curie:ft-kangaroo-2021-10-25-16-36-39
# Robin model (with validation): curie:ft-kangaroo-2021-11-11-23-02-35
# Barney model: curie:ft-kangaroo-2021-10-21-05-24-59
# Ted model (no validation): curie:ft-kangaroo-2021-11-09-17-02-44
# Ted model (with validation): curie:ft-kangaroo-2021-11-09-21-07-18
