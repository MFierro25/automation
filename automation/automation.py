import re

def collect_info():
    with open('./automation/potential-contacts.txt') as file:
        text = file.read()
        
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b'
        email_result = re.findall(email_pattern, text)
        
        email_result.sort()
        sorted_emails = '\n'.join(email_result)
        
        
        phone_pattern = r'(\d{3}[-]\d{3}[-]\d{4}|\(\d{3}\)\s*\d{3}[-]??\d{4})'
        phone_result = re.findall(phone_pattern, text)
        
        phone_result.sort()
        sorted_phone = '\n'.join(phone_result)
        
    with open('./automation/email.txt', 'w') as file:
        for email in sorted_emails:
            file.write(email)
            
    with open('./automation/phone_numbers.txt', 'w') as file:
        for number in sorted_phone:
            file.write(number)
           
        
if __name__ == '__main__':
    collect_info()