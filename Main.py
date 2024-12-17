import GmailAPI as ml
import Agent as astn
import os
import re

def sanitize_filename(filename):
  # Remove invalid characters for file names
  return re.sub(r'[<>:"/\\|?*\x00-\x1f\x80-\xff]', '_', filename)

def processEmails(emails, count):
  for email in emails:
    response = astn.generate(str(email))

    # Save in newsletters folder with sanitized subject as file name
    file_name = sanitize_filename(str(email['Subject'])) + '.txt'
    
    file_path = os.path.join(os.getcwd(), "Newsletters")
    os.makedirs(file_path, exist_ok=True)
    file_path = os.path.join(file_path, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as file:
      file.write(str(response))
    
    try:
      # Mark email as read and archive it
      ml.removeLabels(email, ['UNREAD', 'INBOX'])
    except:
      print("Error in marking email as read.")
      
    print("Emails Processed:", count)
  
    count += 1
  return count

def batchProcessEmails(mails, batch_size):
  count = 1
  for i in range(0, 10, batch_size):
    print("Batch", i//batch_size + 1) # printing the batch number
    batch = mails[i:i+batch_size]
    print("Processing", len(batch), "emails.") # printing the number of emails in the batch
    emails = ml.getEmails(batch)
    count = processEmails(emails, count)
  print("No more emails.")
  return  

def main():
  labels = ['Productivity & Life'] # this line specifies the label of the emails to be read
  state = "is:unread" # this line specifies the state of the emails to be read
  
  mails = ml.listEmails(labels, state)
  batch_size = 10
  # mails = mails[:1]
  if not mails:
    print("No emails found.")
  else:
    print(len(mails), "emails found.")
    batchProcessEmails(mails, batch_size)

if __name__ == "__main__":
  main()