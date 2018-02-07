from bs4 import BeautifulSoup
import urllib.request
import requests
import webbrowser
################################################################################

print("\n******** Routine is Now Running ********\n")

payload = {'username': 'powerwolf',
            'password': 'power1234!',
            'rememberMe': 'true'}

numberUserIds = sum(1 for line in open('userIDs.txt'))
j = 1;
with open('output.txt', 'w+') as output:
    output.write('CRMuserNum\tUserID\tUserName\n')
    with open('userIDs.txt') as userIDs:
        for userID in userIDs:
            with requests.Session() as s:

                print("%d of %d" %(j, numberUserIds))
                ## Open webpage with Beautifulsoup
                url = "http://na.admin.estgames.co.kr/Account/LogOn?ReturnUrl=%2fcabalna%2fUser%2fUserList%3fKey%3did%26Val%3d"+ userID.split('\n')[0] + "%26State%3d1%26category%3d0%26MassCreation%3d0%26FromDate%3d%26ToDate%3d20180129%26limit%3d100&Key=id&Val=anamibeluisa&State=1&category=0&MassCreation=0&FromDate=&ToDate=20180129&limit=100"
                p = s.post(url, data=payload)
                soup = BeautifulSoup(p.text, "html.parser")

    ################################################################################
                ### Fetch Data of webpage
                result = [] # Start empty list
                rows = soup.findAll('tr') # find all table rows in html
                for row in rows:
                    result.append([])
                    cols = row.findAll('td') # find all columns within row
                    for col in cols:
                        strings = [_string.encode('utf8') for _string in col.findAll(text=True)]
                        text = ''.join(str(strings[0]))
                        result[-1].append(text) # Collects all text within rows on list
                result = [x for x in result if x] # Removes empty entries from result

    ################################################################################
                ## Data Manipulation
                # Create empty lists
                crmUserNum = []
                crmUserID = []
                userName = []
                lastIP = []
    ################################################################################
                for entry in result:
                    crmUserNum.append([])
                    crmUserID.append([])
                    userName.append([])
                    crmUserID[-1] = entry[2].split('\\n')[1].split(' ')[-1].split('\\t')[-1].split('\\r')[0]
                    userName[-1] = entry[1].split('\\n')[1].split(' ')[-1].split('\\t')[-1].split('\\r')[0]
                    crmUserNum[-1] = ''.join(c for c in entry[0] if c.isdigit())
    ################################################################################
                ## Retrieve just the correct CRMuserNum in case of several userID entries
                correctUserID = userID.split('\n')[0]
                for i in range(0,len(crmUserID)):

                    if (crmUserID[i].lower() == correctUserID.lower()):
                        output.write(crmUserNum[i] + '\t')
                        output.write(crmUserID[i] + '\t')
                        output.write(userName[i] + '\n')
                j +=1;
print("\n******** Routine is Now Complete ********\n")
