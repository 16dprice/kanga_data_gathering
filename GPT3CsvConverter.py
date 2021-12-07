import csv
import math


class GPT3CsvConverter:
    train_percentage = 0.8

    @staticmethod
    def write_to_train_and_validation_sets(lines, out_file_name):
        num_lines = len(lines)

        num_train_lines = math.floor(GPT3CsvConverter.train_percentage * num_lines)

        train_lines = lines[:num_train_lines]
        validation_lines = lines[num_train_lines:]

        GPT3CsvConverter.convert_to_csv(train_lines, "{}_TRAINING".format(out_file_name))
        GPT3CsvConverter.convert_to_csv(validation_lines, "{}_VALIDATION".format(out_file_name))

    @staticmethod
    def convert_to_csv(lines, out_file_name):
        out_file = open("{}.csv".format(out_file_name), "w")

        fields = ["prompt", "completion"]
        rows = []
        for line in lines:
            rows.append(["", " {}\n".format(line.rstrip())])

        csv_writer = csv.writer(out_file)

        csv_writer.writerow(fields)
        csv_writer.writerows(rows)

        out_file.close()

