# 1. TODO: Get input for student's name and student ID
name = input('Student name: ')
sid = input('SID: ')

# 2. TODO: Print the banner
#    Hint: You may find it handy to use the len() function...

line1_3 = '-' * (7 + len(name) + len(sid))
line2 = '--' + name.upper() + ' - ' + sid + '--'

print(line1_3)
print(line2)
print(line1_3)
