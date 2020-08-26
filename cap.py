#Employee company Email ids with domain
def filter_mail(mail_list):
	domain = "zeezee.com"
	for i in mail_list:
		if domain in i:
			pass
			print("All company's email ids")
			break 
		else:
			print(i)
		
	
mail_list=[]
x= int(input("Enter the no. of email ids:"))
for i in range(0, x):
   new = input()
   mail_list.append(new)
print("\n")

filter_mail(mail_list)


