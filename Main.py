import GmailAPI as ml
import Agent as astn

def processEmails(emails, count):
  for email in emails:
    response = astn.generate(str(email))
    #save in a file
    with open('summary.html', 'w') as file:
      file.write(str(response))
    with open('summary.txt', 'w') as file:
      file.write(str(response))
    # res = json.loads(response) # Parse the JSON string into a dictionary
    # print(response)
    
    # email['Summary'] = res['Summary']
    # email['Category'] = res['Category'] 

    # if res['Category'] != 'Cannot Classify':
    #   ml.addLabels(email, [res['Category']])
    #   if res['Category'] != 'Priority':
    #     ml.removeLabels(email, ['INBOX'])
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
  mails = mails[:1]
  if not mails:
    print("No emails found.")
  else:
    print(len(mails), "emails found.")
    batchProcessEmails(mails, batch_size)

if __name__ == "__main__":
  main()