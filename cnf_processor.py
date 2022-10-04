nameOfFile = input('Name of file: \n')
myfile = open(nameOfFile)
# get the first line of the file
addline = True

n_outputs = input("\nNumber of outputs: ")
n_outputs = int(n_outputs)
outputstring = 'c ind '


for i in range(2,n_outputs+2):
    outputstring = outputstring + str(i)+ ' '
    
outputstring = outputstring + '0\n'

myline = myfile.readline()

while myline:
    if((len(myline)==4)&(myline[0].isnumeric())):
        if((int(myline[0])>1)&(int(myline[0])<= (n_outputs+1))):
            addline = False
    if((len(myline)==5)&(myline[0]=='-')):
        if((int(myline[1])>1)&(int(myline[1])<= (n_outputs+1))):
            addline = False
        
    if(addline):
        outputstring = outputstring + myline
        
    addline = True

    myline = myfile.readline()

output_file_name = 'py'+ nameOfFile   
output_file = open(output_file_name, "w")
n = output_file.write(outputstring)
output_file.close()
myfile.close()
print('\nFile created: '+output_file_name)
