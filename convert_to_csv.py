import openai


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
# Ted personality (with validation): curie:ft-kangaroo-2021-11-17-21-16-24
# Robin personality (with validation): curie:ft-kangaroo-2021-11-17-21-59-32

# Robin w/ new training schema: curie:ft-kangaroo-2021-11-18-03-36-31
# Ted w/ new training schema: curie:ft-kangaroo-2021-11-18-04-40-28
