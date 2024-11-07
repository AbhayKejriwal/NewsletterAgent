import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def generate(email):
  genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
  model = genai.GenerativeModel(model_name="gemini-1.5-flash")
  
  prompt = """You are a personal email newsletter reader and filter. Your task is to read the email message and provide a brief summary of the mail. You should also filter advertisements, promotional content, and other irrelevant content from the email and remove them. So, the end result should be an article form of the newsletter than begins with a summary of the email message followed by the main content of the email, which should be free of any promotional content and repetitive information.

  The email message is provide in HTML format and the output should also be returned in HTML or markdown format.
  
  EMAIL MESSAGE:
  """ + email + """
  
  """
  # print(prompt)
  try:
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print("Error in generating response.")
    print(e)
    return None

# Driver and test code
def main():
  with open("sample.txt", "r", encoding="utf-8") as f:
    message = f.read()
  summary = generate(message)
  print(summary)


if __name__=="__main__":
  # generate("Hello, this is a test message")
  main()