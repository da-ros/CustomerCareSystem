from trulens_eval.utils.generated import re_0_10_rating

# Example input
inputs = ["10", "5.5", "Score:", " ", 7, 90.7]

for input in inputs:
    try:
        print(f"Input: {input} -> Output: {re_0_10_rating(input)}")
    except Exception as e:
        print(f"Error with input {input}: {str(e)}")
