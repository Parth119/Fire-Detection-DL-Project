import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

toaddr = "receiver-address"
fromaddr = "cse.190840131004@gmail.com"
password = "your-password"
def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("Some one entered into your home.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(fromaddr, password)
    s.sendmail(fromaddr, fromaddr, msg.as_string())
    print("Mail send successfully.")
    s.quit()
SendMail("model/saved_model/sample_image/fire_image.jpg")
