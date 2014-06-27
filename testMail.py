# version: Python 3.4.1
import smtplib  
from email.mime.text import MIMEText  
mailto_list=['xxx@qq.com'] 
mail_host="smtp.qq.com"  			# Set SMTP server address
mail_user="xxx"    						# E-mail username
mail_pass="ttt"   							# E-mail password
mail_postfix="qq.com"  				# The suffix of outbox

def send_mail(to_list,sub,content):  
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()        
        server.set_debuglevel(1)
        server.connect(mail_host)
        server.ehlo("10.10.15.52")  		# Set local IP address, when IP address is not one.
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception as e:  
        print(str(e))  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"hello","hello world！"):  
        print("Send OK.")
    else:  
        print("Send Failed.")