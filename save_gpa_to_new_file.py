def is_float(string):
    try:
        float(string)
        return(1)
    except ValueError:
        return(0)
newfile = open("D:/gpafile.txt",'w')
fo = open("C:/Users/Devanand Shenoy/Downloads/S3ME.txt",'r+')
text = fo.read()
length = len(text)
for i in range(length):
    if(text[i] == "."):
        gpa = text[i-1] +"."+ text[i+1] + text[i+2]
        if(is_float(gpa)):
            if(float(gpa) >= 5.0):
                newfile.write(gpa + "\n")
fo.close()
newfile.close()
