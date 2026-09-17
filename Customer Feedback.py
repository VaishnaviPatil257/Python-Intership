def clean_feedback(feedback):
    return " ".join(feedback.strip().split())
def count_words(feedback):
    return len(feedback.split())
def count_characters(feedback):
    return len(feedback)
def find_keywords(feedback):
    feedback = feedback.lower()
    keywords = ["good", "bad", "excellent"]
    result = {}
    for word in keywords:
        result[word] = feedback.count(word)
    return result
def generate_summary(feedback):
    feedback = clean_feedback(feedback)
    words = count_words(feedback)
    characters = count_characters(feedback)
    keywords = find_keywords(feedback)
    print("Clean Feedback:", feedback)
    print("Words:", words)
    print("Characters:", characters)
    print("Excellent:", keywords["excellent"])
    print("Good:", keywords["good"])
    print("Bad:", keywords["bad"])
feedback = input("Enter customer feedback: ")
generate_summary(feedback)
