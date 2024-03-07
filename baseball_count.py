n = int(input())


li = [0]

out = 0
ball = 0

for i in range(n):
   count = input() + "!"
   if count == "ball!":
       ball +=1
       if ball == 4:
           print("fourball!")
           break
       else:
           print(count)
   else:
        out +=1 
        if out == 3:
            print("out!")
            break
        else:
            print(count)
        