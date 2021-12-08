The training (and validation) data located in this folder use actual prompts from the script that the text came from. The idea here is to use the line that immediately preceded a line of speech from a character to be the prompt for that character's speech (the completion).

For example, if the script contained the following lines:

`Barney: Hello. How are you doing this evening?`

`Robin: Well. How are you doing?`

the training data would have `Barney: Hello. How are you doing this evening?` as a prompt and the completion for that prompt would be `Robin: Well. How are you doing?`.

The data is prepared by the code in this project to be `csv` files. The OpenAI command line tools prepare the data into `.jsonl` format files. The split between training and validation data is **80% training** and **20% validation**.

When making a fine-tune, OpenAI takes the `.jsonl` files for training and validation but I leave the `csv` files here just in case we want to use them again later.