from dotenv import load_dotenv

load_dotenv()
import openai

# Read the transcript from the file
with open("Chap3_02_YoutubeSummarizer/transcript.txt", "r") as f:
    transcript = f.read()

# Call the openai ChatCompletion endpoint, with the ChatGPT model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize the following text"},
        {"role": "assistant", "content": "Yes."},
        {"role": "user", "content": transcript},
    ],
)


print(response["choices"][0]["message"]["content"])