from selenium import webdriver
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# driver = webdriver.Chrome("/Users/kumarchandan/Desktop/NEW FOLDERS/seleniumfile/chromedriver")  
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
unique_list = ['0110Varnika', '0b101010', '1001851', '1004tarun', '1005927', '1901147', '1dod4mpty', '1rv19ec010', '2019509051', '210016', '211VDN', '21f100', '21f1000062', '21f1000141', '21f1000164', '21f1000183', '21f1000271', '21f1000330', '21f1000402', '21f1000492', '21f1000593', '21f1000732', '21f1000869', '21f1001035', '21f1001065', '21f1001134', '21f1001294', '21f1001456', '21f1001585', '21f1001712', '21f1001727', '21f1001859', '21f1001927', '21f1001990', '21f1001995', '21f1002075', '21f1002136', '21f1002157', '21f1002184', '21f1002193', '21f1002291', '21f1002353', '21F100292', '21f1002944', '21f1002952', '21f1002976', '21f1002984', '21f1003041.student.o', '21f1003055', '21f1003256', '21f1003408', '21f1003586', '21F1003593', '21f1003687', '21f1003694', '21f1003810', '21f1003860', '21f1003890', '21f1003898', '21f1004022', '21f1004059', '21f1004296', '21f1004352', '21f1004370', '21f1004501_Adhirath', '21f1004733', '21f1004979', '21f1004991', '21f1005200', '21f1005299', '21f1005387_GCSR', '21f1005474', '21F1005510', '21f1005734', '21f1005868', '21f1005880', '21f1005948', '21f1005956', '21f1005996', '21f1006043', '21f100612', '21f1006273', '21f1006304', '21f1006311', '21f1006314', '21f1006393', '21f1006477', '21f1006710', '21f1006846', '21f1007089', '21_karthik_12', '2737_2028', '2ded4u', '2old2learn', '333', '515ma3011', '5andeep', '6115', '786', '89shayan']
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






