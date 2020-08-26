#Employee company Email ids with domain
def filter_mail(mail_list):
	domain = "hitshe6.com"
	for i in mail_list:
		if domain in i:
			pass
			print("All are company's email ids")
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


