import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr = "dhruv.antala@moschip.com"
to_addr = "dhruv.antala@moschip.com"
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "File attachments."
body = "This is the body part"
msg.attach(MIMEText(body, 'plain'))
filename = "data.xlsx"
attachment = open(filename, "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.starttls()
s.login(from_addr, "yftgbvfbwyzrztvj")
text = msg.as_string()
s.sendmail(from_addr, to_addr, text)
s.quit()
