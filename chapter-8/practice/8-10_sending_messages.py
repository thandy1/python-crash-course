messages = ["Hello", "Greetings", "Hi", "Good Night", "Good Morning",]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    while messages:
       current_msg = messages.pop(0)
       print(current_msg)
       sent_messages.append(current_msg) 

send_messages(messages)

print(f"Original messages: {messages}")
print(f"Sent Messages: {sent_messages}")