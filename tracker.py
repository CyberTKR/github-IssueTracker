import requests
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Github API'sine bağlanmak için gerekli bilgiler
username = "github_username"
repo_name = "github_repo_name"
access_token = "github_access_token"

# API endpoint url
url = f"https://api.github.com/repos/{username}/{repo_name}/issues"

# E-posta göndermek için gerekli bilgiler
sender_email = "your_email@example.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"

# Kaç saniyede bir işlemin tekrarlanacağı
interval = 60  # 1 dakika

# Son kontrol tarihi
last_checked = None

# E-posta gönderme fonksiyonu
def send_email(title, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Yeni sorun oluştu: {title}"
    msg.attach(MIMEText(body, 'plain'))

    # E-posta gönderme işlemi
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

while True:
    try:
        # API'ye istek gönderme
        headers = {
            "Authorization": f"token {access_token}"
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)

        # Son kontrol tarihini kaydetme ve yeni sorunları bildirme
        if last_checked is not None:
            for issue in data:
                created_at = issue["created_at"]
                if created_at > last_checked:
                    send_email(issue["title"], issue["body"])
        last_checked = data[0]["created_at"]

    except:
        print("Hata oluştu. Tekrar denenecek.")

    # Belirli bir süre sonra tekrar etme
    time.sleep(interval)
