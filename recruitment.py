def main():
        skills=["Python","C++","JavaScript","Meeting","Leeting","Eating"]
        cv={}
        print("Welcome to the special recuitment program, please answer the following questions:")
        
        name=input("What's your name?")
        cv.update({"name":name})
        age=int(input("How old are you?"))
        cv.update({"age":age})
        experience=input("How many years of experience do you have?")
        cv.update({"experience":experience})
        cv.update({"skills":[]})
        x=1
        for n in skills:
                print (str(x)+". "+n)
                x+=1

        

        list=[]
        
        num1=int(input("Choose a skill from above by entering its number:"))
        cv["skills"].append(skills[num1-1])
        num2=int(input("Choose another skill from above by entering its number:"))
        cv["skills"].append(skills[num2-1])


        b =False
        for n in cv["skills"]:
                if(n=="Eating"):
                        b=True
                

        if (age>=25 and age<=40)and int(experience)>=5 and b:
                print ("You have been accepted, "+name)
        else:
                print ("Sorry you are rejected, "+name)
        
       
	#write your code here

if __name__ == '__main__':
	main()
