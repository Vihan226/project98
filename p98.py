def swapFileData():
    file3=input('enter the file name/ ')
    file4=input('enter the file name/ ')
    with open(file3,'r') as a:
        data_a= a.read()

    with open(file4,'r') as b:
        data_b= b.read()

    with open(file3,'w') as a:
        a.write(data_b)

    with open(file4,'w') as b:
        b.write(data_a)
    

    

swapFileData()