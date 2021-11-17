import openai

robin_model_no_validation = "curie:ft-kangaroo-2021-10-25-16-36-39"
robin_model_with_validation = "curie:ft-kangaroo-2021-11-11-23-02-35"
ted_model_no_validation = "curie:ft-kangaroo-2021-11-09-17-02-44"
ted_model_with_validation = "curie:ft-kangaroo-2021-11-09-21-07-18"



def get_longest_response(responses):
    longest_response = ""
    for response in responses:
        if len(response["text"]) > len(longest_response):
            longest_response = response["text"]

    return longest_response


def send_prompt(prompt, model, num_completions=1):
    completion = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=40,
        temperature=0.9,
        frequency_penalty=1.5,
        presence_penalty=1.5,
        n=num_completions,
        stop=["\n"]
    )

    return completion
    # for choice in completion["choices"]:
    #     print(choice["text"])
    # print(completion["choices"][0]["text"])


def generate_story(prompt):
    num_completions = 5
    new_prompt = prompt

    completion = send_prompt(prompt, robin_model_with_validation, num_completions)
    longest_response = get_longest_response(completion["choices"])
    new_prompt = "{}{}\nTed:".format(new_prompt, longest_response)

    completion = send_prompt(prompt, ted_model_with_validation, num_completions)
    longest_response = get_longest_response(completion["choices"])
    new_prompt = "{}{}\nRobin:".format(new_prompt, longest_response)
    #
    # completion = get_longest_response(send_prompt(prompt, robin_model_with_validation, num_completions))
    # new_prompt = "{} {}\nTed:".format(new_prompt, completion)
    #
    # completion = get_longest_response(send_prompt(prompt, ted_model_with_validation, num_completions))
    # new_prompt = "{} {}\nRobin:".format(new_prompt, completion)
    #
    # completion = get_longest_response(send_prompt(prompt, robin_model_with_validation, num_completions))
    # new_prompt = "{} {}\nTed:".format(new_prompt, completion)
    #
    # completion = get_longest_response(send_prompt(prompt, ted_model_with_validation, num_completions))
    # new_prompt = "{} {}\nRobin:".format(new_prompt, completion)
    #
    # completion = get_longest_response(send_prompt(prompt, robin_model_with_validation, num_completions))
    # new_prompt = "{} {}\nTed:".format(new_prompt, completion)
    #
    # completion = get_longest_response(send_prompt(prompt, ted_model_with_validation, num_completions))
    # new_prompt = "{} {}\nRobin:".format(new_prompt, completion)

    return new_prompt


prompt_1 = """The following is a conversation between Robin and Ted. Ted has been angry lately and is upset about the cereal he has that is too sugary. Robin attempts to be compassionate and console Ted.

Ted: This cereal is too sugary! I'm totally unsatisfied with it.
Robin: I'm sorry Ted. Is there anything I can do about it?
Ted: I wish you could just get me better cereal. This cereal is terrible.
Robin:"""

print(generate_story(prompt_1))

# send_prompt(prompt_1, robin_model_with_validation)
# send_prompt(prompt_1, ted_model_with_validation)
