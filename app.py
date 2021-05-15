from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/kumarchandan/Desktop/NEW FOLDERS/seleniumfile/chromedriver")  
# driver.maximize_window()  
driver.get("https://discourse.onlinedegree.iitm.ac.in/login")
time.sleep(2) 
driver.find_element_by_css_selector('.d-button-label').click()

username = driver.find_element_by_id("login-account-name")

username.send_keys("21f1004845@student.onlinedegree.iitm.ac.in")
 

password = driver.find_element_by_id("login-account-password")

password.send_keys("d@81352813")
  
driver.find_element_by_id("login-button").click()
time.sleep(2) 
all_user_data = []
unique_list = ['0110Varnika', ]
for user in unique_list:


	driver.get(f"https://discourse.onlinedegree.iitm.ac.in/u/{user}/summary")
	# driver.find_element_by_css_selector('.user-content-wrapper.user-content').click()
	# tree = driver.find_elements_by_xpath('/html/body/section/div/div[3]/div[2]/section/div/div/div[1]/ul')
	time.sleep(2) 
	name = driver.find_elements_by_xpath("/html/body/section/div/div[3]/div[2]/section/section/div/div/div[2]/div[1]")
	stat = driver.find_elements_by_xpath("/html/body/section/div/div[3]/div[2]/section/div/div/div[1]")
	reply = driver.find_elements_by_xpath("/html/body/section/div/div[3]/div[2]/section/div/div/div[5]/div/table/tbody")
	arr = [name,stat,reply]
	A=[]
	for links in arr:
		a=[]
		for link in links:

			if link.is_displayed():
				t=(link.text)
				A.append(t)

	# print(A)

	# A=['Kumar9\nkumar chandan', 'STATS\n9 days visited\n5h read time\n60 topics viewed\n349 posts read\n2\ngiven\n1 topic created\n19 posts created\n15\nreceived\n3\nsolutions', 'MOST REPLIED TO\nCKPIITM Chandan kumar\n3\nAnand Anand Iyer\n2\nnikunj_rabadiya Rabadiya Nikunj Vinodbhai\n1\nckg Cherian George\n1\nvalid22 dote\n1\nakshaymalik1995 AKSHAY MALIK\n1', 'MOST LIKED BY\nCKPIITM Chandan kumar\n3\nAnand Anand Iyer\n2\nKarthik_POD\n2\nvikash VIKASH RAM MAHURI\n1\n21f100612 Sandeep Nalla\n1\nckg Cherian George\n1', 'MOST LIKED\nnikunj_rabadiya Rabadiya Nikunj Vinodbhai\n1\nvalid22 dote\n1', 'Programming in Python\n1 11\nStatistics for Data Science II\n– 6\nMathematics for Data Science II\n– 2']



	user_dict={}
	first =True
	for a in A:
		if(first):
			lst = a.split('\n')
			username = lst[0]
			name = lst[1]
			user_dict['username'] = username
			user_dict['name']= name
			first=False
			continue
		users=a.split('\n')
		heading = users[0]

		n= len(users)
		
		if( heading == 'STATS'):
			user_dict['stat']=a
		else:
			d={}
			for i in range(n):
				if(i%2 == 0):
					# d[users[i]]={}
					pass
				else:
					topics = users[i].split()[0]
					replies = users[i].split()[1]

					user_dict[f'{users[i-1]} topics created']=topics
					user_dict[f'{users[i-1]} replies']=replies
			# user_dict['activity'] = d


	all_user_data.append(user_dict)
	lt=(f'{user_dict}')
	# dt=(f'dic = {user_dict}')
	print(lt)
print(all_user_data)


print('completed')
driver.close()






