def profainty_filter(msg):
    message = msg.split()
    with open("//app//profanity_words.txt", "r", encoding="utf-8") as f:
        profainty_words = [_.replace("\n", "").lower() for _ in f.readlines()]
    for words in message:
        if words.lower() in profainty_words:
            message[message.index(words)] = "***"
    return " ".join(message)
