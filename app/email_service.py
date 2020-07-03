import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
CLIENT_EMAIL = os.environ.get("CLIENT_EMAIL_ADDRESS")


def send_email(subject="[ETP Update] This is a test", html="<p>Testing, Testing, 1 ... 2 ... 3 ...</p>"):
    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=MY_EMAIL, to_emails=CLIENT_EMAIL,
                   subject=subject, html_content=html)
    try:
        response = client.send(message)
        # > <class 'python_http_client.client.Response'>
        print("RESPONSE:", type(response))
        print(response.status_code)  # > 202 indicates SUCCESS
        return response
    except Exception as e:
        print("Oops - something went wrong.  The email alert did not send", e.message)
        return None


if __name__ == "__main__":
    example_subject = "[ETP Update] This is a test"

    example_html = f"""
    <h3>This is a test of the Price Move Alerting Service</h3>

    <h4>Today's Date</h4>
    <p>Monday, January 1, 2040</p>

    <h4>My Stocks</h4>
    <ul>
        <li>MSFT | +04%</li>
        <li>WORK | +20%</li>
        <li>ZM | +44%</li>
    </ul>
    """

    send_email(example_subject, example_html)
