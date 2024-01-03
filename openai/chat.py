#!/usr/bin/python3 -u

"""
Start conversation with ChatGTP
NOTE: OPENAI_API_KEY env var required
"""

import os
import sys
import signal
import time

from openai import OpenAI

###
# MAIN METHOD
###


def main():
    """Main method"""
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # Create assistant
    assistant = client.beta.assistants.create(model="gpt-4", name="Ooze", instructions="Be as helpful as possible")

    # Create a thread
    thread = client.beta.threads.create()

    # Start
    print_as_gpt("Ask me stuff. Enter 'done' when finished ...\n")

    # Create run
    while True:
        message = input("\033[93m * You: \033[0m")
        print()

        # Check if finished
        if message.strip().lower() == "done":
            break

        # Create a new message for thread
        client.beta.threads.messages.create(thread_id=thread.id, role="user", content=message)

        # Create a new run
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)

        # Wait for run to execute
        message = wait_for(client, thread.id, run.id)

        # Display message
        print("\n")
        print_as_gpt(message + "\n")

    # Loop finished. Clean up
    client.beta.assistants.delete(assistant.id)
    print_as_gpt("Get outta here.\n")


def wait_for(client, thread_id, run_id):
    print("\033[92m( thinking ", end="")

    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)

        if run.status == "completed":
            # Finish thinking bubble
            print(" )\033[0m", flush=True)

            # Get only latest message
            messages = client.beta.threads.messages.list(thread_id=thread_id, limit=1)
            return messages.data[0].content[0].text.value

        else:
            print(".", end="", flush=True)
            time.sleep(1)


# Print with green
def print_as_gpt(text):
    """Print with green"""
    print("\033[92m * GPT:\033[0m", text)


# pylint: disable=W0613
def signal_handler(sig, frame):
    """Control signal handler"""
    print(" ")
    sys.exit(0)


# Set up Ctrl-C handler
signal.signal(signal.SIGINT, signal_handler)


###
# MAIN
###

# Invoke main method
if __name__ == "__main__":
    main()
