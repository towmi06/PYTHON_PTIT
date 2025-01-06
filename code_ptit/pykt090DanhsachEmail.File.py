with open('CONTACT.in', 'r') as file:
    emails = file.readlines()

emails = [e.strip().lower() for e in emails ]

ema = sorted(set(emails))
for e in ema:
    print(e)