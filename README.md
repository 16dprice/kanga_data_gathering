# Project Overview

## Directory Structure

The `himym` folder contains all thing having to do with *How I Met Your Mother*. It has all of the code used to scrape the websites where we retrieved the data for the HIMYM scripts. It also has the speech of each character distilled into a file for each of those characters. The naming format is `<name>-<number of lines of speech>` and lines of speech are separated by newline characters.

The `west_wing` folder is essentially the same as the `himym` folder except it has to do with the show *West Wing*. The web scraping was different because of the differently formatted websites where the data was, but that's about it. The character speech is available for this, but is currently not in the repository.

## Models that have been trained

There are several models available. The following are their IDs along with an indication towards what their training data was.

---

| Character Name | ID | Description | Training Data Location |
| --- | --- | --- | --- |
| Barney Stinson | `curie:ft-kangaroo-2021-10-21-05-24-59` | Trained by Allen and am not sure what the training data was for this. | N/A |
| Robin Scherbatsky | `curie:ft-kangaroo-2021-10-25-16-36-39` | Initial Robin model trained with no validation data. | `himym/initial_training_data` |
| Robin Scherbatsky | `curie:ft-kangaroo-2021-11-11-23-02-35` | Initial Robin model trained with validation data. | `himym/initial_training_data_with_validation` |
| Robin Scherbatsky | `curie:ft-kangaroo-2021-11-17-21-59-32` | Robin model trained with names replaced with other random names. | `himym/training_data_for_personality` |
| Robin Scherbatsky | `curie:ft-kangaroo-2021-11-18-03-36-31` | Robin model trained with training data where prompts were non-empty. | `himym/training_data_with_prompts` |
| Ted Mosby | `curie:ft-kangaroo-2021-11-09-17-02-44` | Initial Ted model with no validation data. | `himym/initial_training_data` |
| Ted Mosby | `curie:ft-kangaroo-2021-11-09-21-07-18` | Initial Ted model trained with validation data. | `himym/initial_training_data_with_validation` |
| Ted Mosby | `curie:ft-kangaroo-2021-11-17-21-16-24` | Ted model trained with names replaced with other random names. | `himym/training_data_for_personality` |
| Ted Mosby | `curie:ft-kangaroo-2021-11-18-04-40-28` | Ted model trained with training data where prompts were non-empty | `himym/training_data_with_prompts` |

## Useful OpenAI CLI Commands

The following are some useful commands for fine-tuning models using the OpenAI command line tools.

To prepare data and send to a .jsonl file that is formatted properly

`openai tools fine_tunes.prepare_data -f <filename>`

To run a fine-tune job after the data has been prepared (<model> is typically 'curie')

`openai api fine_tunes.create -t <filename> -m <model>`

To run a fine-tune job after the data has been prepared with validation (<model> is typically 'curie')

`openai api fine_tunes.create -t <train_filename> -v <validation_filename> -m <model>`

List all created fine-tunes

`openai api fine_tunes.list`
