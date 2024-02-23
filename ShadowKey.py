from upload_vulnerability_scanner.file_upload_tests import assess_upload_vulnerability
from upload_vulnerability_scanner.file_type_checks import check_allowed_file_types
from upload_vulnerability_scanner.form_scanner import scan_for_upload_forms
from exploit_tools.exploit_uploader import exploit_file_upload
from report_generator.report_output import generate_vulnerability_report

def main_menu():
    print("1. Scan for Upload Vulnerabilities")
    print("2. Check Allowed File Types")
    print("3. Scan for All Upload Points")
    print("4. Exploit Upload Vulnerability")
    print("5. Generate Report")
    choice = input("Select an option: ")

    if choice == '1':
        target_url = input("Enter target URL: ")
        assess_upload_vulnerability(target_url)
    elif choice == '2':
        target_url = input("Enter target URL: ")
        check_allowed_file_types(target_url)
    elif choice == '3':
        target_url = input("Enter target URL: ")
        forms = scan_for_upload_forms(target_url)
        print(f"Found {len(forms)} upload forms")
    elif choice == '4':
        target_url = input("Enter target URL: ")
        payload = input("Enter payload file path: ")
        exploit_file_upload(target_url, payload)
    elif choice == '5':
        findings = {}  # This should be replaced with actual findings from previous steps
        generate_vulnerability_report(findings)

if __name__ == "__main__":
    main_menu()
