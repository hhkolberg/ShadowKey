import sys
import requests
from payloads import payloads  # This imports the payloads list from payloads.py
from bs4 import BeautifulSoup

def find_form_action(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming the first <form> tag is the one we want
    form = soup.find('form')

    if form:
        action_url = form.get('action')
        if action_url:
            # Combine with base URL if the action is a relative path
            return requests.compat.urljoin(url, action_url)

    return None  # If no form is found, or it doesn't have an action

############################# CHECK UPLOAD VULN ################################

def check_upload_vulnerabilitie():
    page_url = input("Post the link where the upload feature is present: ")
    action_url = find_form_action(page_url)

    if action_url:
        print(f"Found form with action URL: {action_url}")

        for payload in payloads:
            files = {'file': (payload['file_name'], payload['file_content'])}
            response = requests.post(action_url, files=files)

            if response.status_code == 200:
                print(f"Uploaded {payload['file_name']} successfully!")
            else:
                print(f"Failed to upload {payload['file_name']}. Status code: {response.status_code}")
    else:
        print("No form found on the provided page, or no action attribute present.")


def exploit_file_upload():
  print("Exploiting file upload vulnerability...")
  #Code goes here

def automated_scanning():
  print("Performing automated scanning...")
  #Code goes here

def custom_payloads():
  print("Using Custom payload for file upload...")
  #Code goes here

def generate_report():
  print("Generating report...")
  #Code goes here

def main_menu():
  while True:
    print("\nWelcome to the DragonByte Sentry Toolkit")
    print("1. Check for Basic Upload Vulnerabilities")
    print("2. Exploit File Uploads")
    print("3. Automated Scanning")
    print("4. Custom Payloads")
    print("5. Reporting")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      check_upload_vulnerabilitie()
    elif choice == "2":
      exploit_file_upload
    elif choice == "3":
      automated_scanning
    elif choice == "4":
      custom_payloads
    elif choice == "5":
      generate_report
    elif choice == "6":
      print("Exiting...")
      sys.exit(0)
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main_menu()
