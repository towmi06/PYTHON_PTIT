s = input()
print('yes' if len(s) > 4 and s[-3: ].lower() == '.py' else 'no')