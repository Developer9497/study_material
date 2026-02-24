


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import ssl

# Your personal configuration
YOUR_EMAIL = "kirankale9497@gmail.com"
YOUR_PASSWORD = "Ashugore75@"  
YOUR_NAME = "Kiran Kale"
YOUR_PHONE = "9637283704"
YOUR_LINKEDIN = "https://www.linkedi.com/in/chetan-kale-9a16b8353"
RESUME_PATH = "Chetan_Resume.pdf"

# COMPLETE HR EMAIL DICTIONARY (All companies with HR emails)
company_email_dict = {
  "kpmg": "kirankale0999@gmail.com"
  
}


# Email content template
SUBJECT = f"Job Application {YOUR_NAME} Python Developer"

EMAIL_BODY = """ 
Dear Hiring Manager,

I am writing to express my enthusiastic interest in entry-level Python Developer opportunities at your organization. As a recent graduate with strong foundational knowledge in Python programming, web development, and software engineering principles, I am eager to begin my professional journey and contribute to your team's success.

During my academic journey, I have developed proficiency in:
• Python Programming & OOP Concepts
• Django/Flask Web Framework
• REST API Development
• Database Management (MySQL, MongoDB)
• Problem-solving & Algorithm Design

I am a quick learner with strong analytical skills and passion for coding. I am excited about the possibility of starting my career with your company and growing alongside your innovative team.

I have attached my resume for your review and would be grateful for the opportunity to discuss how my fresh perspective and dedication can benefit your organization.
Thank you for considering my application.

Best regards,
{your_name}
{your_phone} 
{your_email}  
{your_linkedin}
"""
def test_gmail_connection(email, password):
    """Test Gmail connection before sending emails"""
    try:
        print("🔐 Testing Gmail connection...")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(email, password)
            print("✅ Gmail authentication successful!")
            return True
    except Exception as e:
        print(f"❌ Gmail authentication failed: {e}")
        return False

def send_email(to_company, to_email, your_name, your_email, your_password, your_phone, your_linkedin):
    """Send email to a specific company"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = your_email
        msg['To'] = to_email
        msg['Subject'] = f"Job Application - {your_name} - Python Developer"
        
        # Customize email body
        customized_body = EMAIL_BODY.format(
            your_name=your_name,
            company_name=to_company,
            your_email=your_email,
            your_phone=your_phone,
            your_linkedin=your_linkedin
        )
        
        msg.attach(MIMEText(customized_body, 'plain'))
        
        # Attach resume
        if os.path.exists(RESUME_PATH):
            with open(RESUME_PATH, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(RESUME_PATH)}")
                msg.attach(part)
        
        # Create SMTP session with SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(your_email, your_password)
            server.sendmail(your_email, to_email, msg.as_string())
        
        print(f"✅ Email sent successfully to {to_company} ({to_email})")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email to {to_company} ({to_email}): {str(e)}")
        return False

def main():
    print("🚀 Starting Email Campaign...")
    print(f"Total companies: {len(company_email_dict)}")
    print("=" * 60)
    
    # Verify resume file exists
    if not os.path.exists(RESUME_PATH):
        print(f"❌ Resume file not found: {RESUME_PATH}")
        print("Please make sure your resume file is in the same folder as this script.")
        return
    
    # Use predefined credentials or ask user
    use_predefined = input("Use predefined credentials? (y/n): ").strip().lower()
    
    if use_predefined == 'y':
        your_email = YOUR_EMAIL
        your_password = YOUR_PASSWORD
        your_name = YOUR_NAME
        your_phone = YOUR_PHONE
        your_linkedin = YOUR_LINKEDIN
    else:
        your_email = input("Enter your email: ").strip()
        your_password = input("Enter your app password: ").strip()
        your_name = input("Enter your name: ").strip()
        your_phone = input("Enter your phone: ").strip()
        your_linkedin = input("Enter your LinkedIn: ").strip()
    
    if not your_email or not your_password or not your_name:
        print("❌ Please provide all required information.")
        return
    
    # Test connection first
    if not test_gmail_connection(your_email, your_password):
        print("\n❌ Cannot connect to Gmail. Please check:")
        print("1. Is 2-Step Verification enabled?")
        print("2. Did you generate an App Password?")
        print("3. Go to: https://myaccount.google.com/apppasswords")
        print("4. Make sure you're using App Password, not your regular password")
        return
    
    # Ask for confirmation before sending
    print(f"\n📧 Ready to send {len(company_email_dict)} emails")
    confirm = input("Continue? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Campaign cancelled.")
        return
    
    successful_emails = 0
    failed_emails = 0
    
    # Send emails to all companies
    print("\n" + "=" * 60)
    for i, (company, email) in enumerate(company_email_dict.items(), 1):
        print(f"\n[{i}/{len(company_email_dict)}] 📧 Sending to {company}...")
        
        success = send_email(company, email, your_name, your_email, your_password, your_phone, your_linkedin)
        
        if success:
            successful_emails += 1
        else:
            failed_emails += 1
        
        # Add delay to avoid being flagged as spam
        time.sleep(3)
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 EMAIL CAMPAIGN SUMMARY")
    print("=" * 60)
    print(f"✅ Successful: {successful_emails}")
    print(f"❌ Failed: {failed_emails}")
    print(f"📨 Total Sent: {successful_emails + failed_emails}")
    
    if (successful_emails + failed_emails) > 0:
        success_rate = (successful_emails / (successful_emails + failed_emails)) * 100
        print(f"🎯 Success Rate: {success_rate:.1f}%")
    
    print("\n🎉 Campaign completed!")

if __name__ == "__main__":
    main()