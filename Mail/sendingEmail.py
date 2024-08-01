import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login('vaishnavishrivastava731@gmail.com', 'ryjp trzn odvm efju')
connection.sendmail('vaishnavishrivastava731@gmail.com', 'aniketsirota64@gmail.com',
                    'subject: this is the subject \n\n hello user')
print("Email sent")
connection.quit()
