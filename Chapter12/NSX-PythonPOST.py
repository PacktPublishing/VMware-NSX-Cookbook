# Import Requests library
import requests

# NSX Variables
nsxmanager = 'https://nsxmgr-01a.corp.local'
nsxurl = '/api/2.0/vdn/scopes/vdnscope-1/virtualwires'
nsxheaders = {'Content-Type': 'application/xml'}
nsxuser = 'admin'
nsxpass = 'VMware1!'
nsxpayload = '''
<virtualWireCreateSpec>
  <name>Python-Logical-Switch</name>
  <description>Logical Switch created from Python</description>
  <tenantId>Python Tenant</tenantId>
  <controlPlaneMode>UNICAST_MODE</controlPlaneMode>
  <guestVlanAllowed>false</guestVlanAllowed>
</virtualWireCreateSpec>
'''

# REST API call using requests.get function from request library. Set verify to False to ignore SSL
response = requests.post(nsxmanager + nsxurl, data = nsxpayload, auth = (nsxuser, nsxpass), verify = False, headers = nsxheaders)

# Print HTTP Response Code
print (response)

# Print XML Content
print (response.text)