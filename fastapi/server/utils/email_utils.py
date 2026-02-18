import brevo_python
from brevo_python.rest import ApiException

# 1. Setup Configuration
configuration = brevo_python.Configuration()

# 🔑 REPLACE 1: Paste your Brevo v3 API Key (xkeysib-...) here
configuration.api_key['api-key'] = "xsmtpsib-584a1b95d6f085f4cc0a81a098ebd3449993021f8a7ff6b46ecc88e0b9283d5c-wMIHsyU58tsERaw4"

# 2. Initialize the API client
api_client = brevo_python.ApiClient(configuration)
api_instance = brevo_python.TransactionalEmailsApi(api_client)

def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email using the Brevo API SDK.
    """
    # 📧 REPLACE 2: This MUST be verified in Brevo -> Senders & IP
    sender_email = "satheesh.official.in@gmail.com" 
    
    # 👤 REPLACE 3: The name displayed in the user's inbox
    sender_name = "Akshaya College Admissions"

    sender = {"name": sender_name, "email": sender_email}
    to = [{"email": to_email}]
    
    # Formats the text to look good in email
    html_content = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="padding: 20px; border: 1px solid #eee; border-radius: 5px;">
                {body.replace('\n', '<br>')}
            </div>
        </body>
    </html>
    """

    send_smtp_email = brevo_python.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(f"✅ Email sent! ID: {api_response.message_id}")
        return True
    except ApiException as e:
        # If this prints 401, your API key is still wrong.
        # If this prints 403, your sender email is not verified.
        print(f"❌ Brevo Error: {e.status} - {e.body}")
        return False