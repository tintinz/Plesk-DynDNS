# Plesk-DynDNS
Python script that you add to local host crontab and it will update your pleskDNS
Small but generic script that you can use to get your self n Dynamic DNS for plesk.

**Requiments**

Python3

subdomain: oldip   ( oldip.yourdomain.com, It uses it as refrens to compare if you have a new IP and if all record need to be change  )


**How its working**
it connect to your pleskhost and the specify domainname, looks for oldip.yourdomain.com compare it with your current IP, if it's same, the script will end, if it is different it will scan for all records that have the old IP registerd and change to the new one. When all records are updated it will update the oldip.yourdomain.com to the new IP too.


**How to use it**
run it like 

python newip.py "Plekshost ip/fqdn:port" "domain to update" "username" "password"

**example:**
python newip.py pleskhost.com:8443 yourdomain.com admin password123

It will scan all records for "yourdaomain.com" and update it your new IP are diffrent from oldip.yourdomain.com
