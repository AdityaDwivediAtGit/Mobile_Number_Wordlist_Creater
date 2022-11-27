from time import sleep

# Console colors
White = '\033[0m'
Red = '\033[31m' 
Green = '\033[32m' 
Orange = '\033[33m'
Blue = '\033[34m'  
Purple = '\033[35m'
Cyan = '\033[36m' 
Gray = '\033[37m'  


begin = int(input(Orange + "Enter Starting Number : " + White))
end   = int(input(Orange + "Enter Ending   Number : " + White))
outputFile =input(Orange + "Enter Output File Name: " + White)

if begin>end:
    print(Red + f"\n\n[error: STARTING GREATER THAN END]" + White)
    sleep(10)
    exit()


f = open(outputFile,"w+")

print(Cyan)
if (end - begin)>5:
    print(begin)
    print(begin+1)
    print("...")
    print(end-1)
    print(end)

print(Purple)
for x in range(begin,end+1):
	f.write(str(x)+"\n")
	print("\r"+str(x), end="") 
f.close()

if x==end:
    print(Green + f"\n\n[{outputFile} FILE CREATED SUCCESFULLY]" + White)
    sleep(10)
