import time
import time
import sys

def typing_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

# Example usage


#work on message delay for type out style
typing_effect("messages for you to read", 0.05)

# Function to print messages with a delay
def delayed_output(messages, delay):
    for message in messages:
        typing_effect(message, 0.05)
        time.sleep(delay)

# List of messages to print
messages = ["Hello", "This is a delayed output", "Each message is printed after a delay","Can I just wait?"]

# Delay in seconds
delay = 1.5

# Call the function to print messages with a delay
delayed_output(messages, delay)


