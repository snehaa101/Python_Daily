# QUE) Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
          Dear <|Name|>,
          You are selected! 
          <|Date|>
          '''
# print(letter.replace("<|Name|>","SNEHA"))
# print(letter.replace('<|Date|>', '04/10/2025'))

print(letter.replace("<|Name|>","SNEHA").replace('<|Date|>', '04/10/2025').replace(" ","..."))