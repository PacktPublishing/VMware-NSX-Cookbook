# Import Requests library
import requests

# NSX Variables
nsxmanager = 'https://nsxmgr-01a.corp.local'
nsxurl = '/api/2.0/services/usermgmt/user/admin'
nsxheaders = {'Content-Type': 'application/xml'}
nsxuser = 'admin'
nsxpass = 'VMware1!'

# REST API call using requests.get function from request library. Set verify to False to ignore SSL
response = requests.get(nsxmanager + nsxurl, auth = (nsxuser, nsxpass), verify = False, headers = nsxheaders)

# Print HTTP Response Code
print (response)

# Print XML Content
print (response.text)