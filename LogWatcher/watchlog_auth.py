import os, sys, time
import smtplib
import re

logfile_path = "/var/log/auth.log"

gmail_user = "the.mail.of.your.bot@gmail.com"
gmail_password = "your_password"
notification_subject = "WARNING: new log activity"
notification_recipient = "your.mail@company.com"

# sorry I'm lazy! :P
matching_patterns=[
  re.compile(r"Failed password for"),
  re.compile(r"Invalid user"),
  re.compile(r"Too many"),
  re.compile(r"preauth")
]

MAX_BUFFER = 2048 * 100 

def send_email(subject, msg, recipient):
    sender = gmail_user
    session = smtplib.SMTP('smtp.gmail.com', 587)
    hello_msg_tuple=session.ehlo()
    if hello_msg_tuple[0] != 250:
        print "ERROR: client is not able to get a valid ehlo msg from the SMTP server"
        return

    starttls_msg_tuple = session.starttls()
    if starttls_msg_tuple[0] != 220:
        print "ERROR: client is not able to get a valid start tls msg from the SMTP server"
        return

    # reasking ehlo
    hello_msg_tuple = session.ehlo()
    if hello_msg_tuple[0] != 250:
        print "ERROR: client is not able to get a valid ehlo msg from the SMTP server"
        return

    auth_msg_tuple = session.login(gmail_user, gmail_password)
    if auth_msg_tuple[0] != 235:
        print "ERROR: client is not able to login"
        return

    headers = ["from: " + sender,
               "subject: " + subject,
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/plain"]
    headers = "\r\n".join(headers)

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + msg)

if __name__ == "__main__":
    current = open(logfile_path, "r")
    curino = os.fstat(current.fileno()).st_ino
    while True:
        while True:
            fbuf = []
            buf = current.read(MAX_BUFFER)
            if buf == "":
                break

            # filter buffer
            for line in buf.split("\n"):
                for rx in matching_patterns:
                    if rx.search(line):
                        fbuf.append(line)
                        break
            buf = "\n".join(fbuf)
            sys.stdout.write(buf)
            send_email(notification_subject, buf, notification_recipient)
        try:
            if os.stat(logfile_path).st_ino != curino:
                new = open(name, "r")
                current.close()
                current = new
                curino = os.fstat(current.fileno()).st_ino
                continue
        except IOError:
            pass
        time.sleep(1)
