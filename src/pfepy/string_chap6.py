''' data(self, start, end)
'''

a = 'I saw a wolf in the forest. A lone wolf'
print a.find('wolf')          # first occurrence
print a.find('wolf', 10, 20)  # not in range of 10 to 20
print a.find('wolf', 15)      # 15 start, second wolf in range


data = 'roger.ward@hotmail.com'

start_position = data.find('@')
print 'start_position: ',start_position
finish_position = len(data)
print  'finish_position: ',finish_position

email_host = data[start_position + 1: finish_position]
print 'email_host ',email_host

''' str.find(str, beg=0 end=len(string)) '''
data = 'From Stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@') #
print  atpos # ok, gives 21
sppos = data.find(' ',atpos, len(data))
print sppos # gives 31

host = data[atpos+1 :sppos]
print  'host ',host # correct output

str3 = 'sosososo4sos'

so1= str3.find('so')
so2 = str3.find('so', so1 + 1)
so3 = str3.find('so', so2 +1)
so4 = str3.find('4')
print so1, so2, so3, so4
