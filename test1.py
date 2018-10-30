import sys
inputpath="input1.txt"
outputpath="output1.txt"

finput = open("input1.txt","r")

foutput = open(outputpath,"w")


with open(inputpath) as fp:
   line = fp.readline()
   cnt = 1
   starcount1 = 0
   starcount2 = 0
   starcount3 = 0
   starcount4 = 0

   character1 = ''
   character2 = ''
   character3 = ''
   character4 = ''


   while line:

       character1 = line[0]
       if len(line) > 1:
           character2 = line[1]
       if len(line)>2:
           character3 = line[2]
       if len(line) > 3:
           character4 = line[3]

       if character1 == '*' and character2 == '*' and character3 == '*' and character4 == '*':
           starcount4 += 1
           repstr = str(starcount1) + '.' + str(starcount2) + '.' + str(starcount3) + '.' + str(starcount4)
           modline = line.replace('****', repstr)
       elif character1 == '*' and character2 == '*' and character3 == '*':
           starcount3 += 1
           repstr = str(starcount1) + '.' + str(starcount2) + '.' + str(starcount3)
           modline = line.replace('***', repstr)
       elif character1 == '*' and character2 == '*':
           starcount2 += 1
           repstr = str(starcount1)+'.'+str(starcount2)
           modline = line.replace('**', repstr)
       elif character1 == '*':
           starcount1 += 1
           modline = line.replace('*', str(starcount1))

       elif character1 == '.' and character2 == '.' and character3 == '.' :
           modline = line.replace('...', '-')
       elif character1 == '.' and character2 == '.':
           fp.seek(fp.tell() + 1)
           nextline = fp.readline()
           if len(nextline) > 0:
               nextindex0 = nextline[0]
           else:
               nextindex0 = ''

           if len(nextline) > 1:
               nextindex1 = nextline[1]
           else:
               nextindex1 = ''
           if len(nextline) > 2:
               nextindex2 = nextline[2]
           else:
               nextindex2 = ''

           if nextindex0 == '.' and nextindex1 == '.' and nextindex2 == '.':
               modline = line.replace('..', '+')
           else:
               modline = line.replace('..', '-')

           fp.seek(fp.tell() - 1)
           nextline = fp.readline()
          # modline = line.replace('..', '+')
       elif character1 == '.':
           fp.seek(fp.tell()+1)
           nextline=fp.readline()
           if len(nextline)>0:
                nextindex0 = nextline[0]
           else:
               nextindex0 = ''

           if len(nextline)>1:
                nextindex1 = nextline[1]
           else:
               nextindex1 = ''
           if nextindex0 == '.' and nextindex1 == '.':
               modline = line.replace('.', '+')
           else:
               modline = line.replace('.', '-')
           fp.seek(fp.tell() - 1)
           nextline = fp.readline()
       else:
           modline = line


       foutput.writelines(modline)
       line = fp.readline()
       cnt += 1

foutput.close()
