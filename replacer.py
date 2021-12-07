import random
from GPT3CsvConverter import GPT3CsvConverter


class Replacer:
    @staticmethod
    def replace_tokens(lines, tokens, replacements):
        new_lines = []
        for line in lines:
            while Replacer.line_has_token(line, tokens) is not None:
                token = Replacer.line_has_token(line, tokens)
                replacement = random.choice(replacements)
                line = line.replace(token, replacement)
            new_lines.append(line)

        return new_lines

    @staticmethod
    def line_has_token(line, tokens):
        for token in tokens:
            if token in line:
                return token
        return None


with open("random_names.txt", "r") as names_file:
    character_lines = open("himym/character_speech/Robin-4007", "r").readlines()
    himym_names = ["Barney", "Lily", "Marshall", "Ted"]
    random_names = names_file.read().splitlines()

    new_lines = Replacer.replace_tokens(character_lines, himym_names, random_names)
    GPT3CsvConverter.write_to_train_and_validation_sets(new_lines, "robin_personality")

