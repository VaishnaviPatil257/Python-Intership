def clean_message(message):
    return " ".join(message.strip().split())


def detect_keyword(message):
    keywords = ["order", "payment", "help", "delivery"]

    message = message.lower()

    for keyword in keywords:
        if keyword in message:
            return keyword

    return "No keyword"


def is_question(message):
    return message.endswith("?")


def count_words(message):
    return len(message.split())


def generate_response_type(message):
    if is_question(message):
        return "Question"
    else:
        return "Statement"


message = input("Enter message: ")

message = clean_message(message)

print("Clean Message:", message)
print("Type:", generate_response_type(message))
print("Words:", count_words(message))
print("Keyword Detected:", detect_keyword(message))
