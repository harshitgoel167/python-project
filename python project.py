import os
print('Tell me what you what you want to open : ',end='')
p = input()

if (('run' in p) or ('khol' in p) or ('open' in p)) and (('chrome' in p) or ('google' in p)):
    os.system('chrome')

elif (('run' in p) or ('khol' in p) or ('open' in p)) and ('teamviewer' in p):
    os.system('teamviewer')
    
elif (('run' in p) or ('khol' in p) or ('open' in p)) and (('notepad' in p)or('editor' in p)):
    os.system('notepad')

elif (('run' in p) or ('khol' in p) or ('open' in p)) and ('postman' in p):
    os.system('postman')


elif (('run' in p) or ('khol' in p) or ('open' in p)) and ('github' in p):
    os.system('github')    

else:
    print('NHI KHOLUNGA BATA KYA KARLEGA !!!!!!!!!!!!')
