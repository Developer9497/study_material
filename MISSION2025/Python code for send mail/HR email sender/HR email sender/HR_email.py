


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
YOUR_PASSWORD = "vdkoxsuxcolcpbqm"  
YOUR_NAME = "Kiran Kale"
YOUR_PHONE = "9637283704"
YOUR_LINKEDIN = "https://www.linkedi.com/in/chetan-kale-9a16b8353"
RESUME_PATH = "Kiran_Kale_Resume_Java_2025.pdf"

# COMPLETE HR EMAIL DICTIONARY (All companies with HR emails)
company_email_dict = {
  "Benoy Koshy":"benoy.koshy@sisainfosec.com",
"Bensely Zachariah":"bensely.zachariah@fulcrumdigital.com",
"Bensley Zachariah":"bensley.zachariah@fulcrumdigital.com",
"Benson Mendez":"benson.mendez@microobjects.net",
"Bhakti Dharod":"bhakti.dharod@idfy.com",
"Bharat Bhartia":"bharat.bhartia@workindia.in",
"Bharat Rao":"bharat@ka-nex.com",
"Bharathi Ravipati":"bravipati@appstekcorp.com",
"Bhargavi Challa":"bhargavic@aissel.com",
"Bharti Negi":"bharti.negi@edifecs.com",
"Bhavana Jain":"bhavana@netcore.co.in",
"Bhavik Kaklotar":"bkaklotar@diabsolut.com",
"Bhavik Shah":"bhavik@games2win.com",
"Bhavika Sheth":"bhavika.sheth@itcgindia.com",
"Bhavin Sanghavi":"bhavin@mydukaan.io",
"Bhavya Shetty":"bhavya@supplywisdom.com",
"Bhawna Suri":"bhawna@weexcel.in",
"Bhupesh Wasmatkar":"bhupesh.wasmatkar@verse.in",
"Biju Varghese":"biju.v@inapp.com",
"Bikram Dash":"bikram.dash@tatwa.info",
"Bindu Krishnan":"bindu.krishnan@ospyn.com",
"Binoy Varghese":"binoy.varghese@rgigroup.com",
"Biplob Das":"biplob.das@izmoltd.com",
"Birendra Rout":"birendra.rout@weavertec.com",
"Bishnu Rai":"bishnu.rai@iglobalservices.net",
"Bosky Wadhwa":"bosky.w@totalitglobal.com",
"Brij Kishore":"brij@claritusconsulting.com",
"Britto Ambrose":"britto@xoxoday.com",
"Bushra Mehdi":"bushra.mehdi@axeno.co",
"Byju Valappil":"byju@rdalabs.com",
"Capt Kansal":"capt.kansal@writerinformation.com",
"Celina Joseph":"celina.joseph@extentia.com",
"Chainsingh Rathore":"chainsingh.rathore@thegatewaycorp.com",
"Chaitali Bhattacharya":"cbhattacharya@inventive-it.com",
"Chaitali Ray":"cray@netwoven.com",
"Chaitanya Arikati":"chaitanya.arikati@abjayon.com",
"Chaitanya Kanthi":"chaitanya.kanthi@smartims.com",
"Chaitanya Peeta":"chaitanya.peeta@polygon.technology",
"Chamola Hal":"chamola.hal@hal-dz.com",
"Chanchal Chandiok":"chanchal.chandiok@northgateps.com",
"Chandan Gambhir":"chandan@noida.interrasystems.com",
"Chandan Thakur":"chandan.kashyap@mysenseinc.com",
"Chandini Davies":"chandinid@saglobal.com",
"Chandini Mokthar":"chandini@moolya.com",
"Chandni Chopra":"chandnic@lambdatest.com",
"Chandni Yadav":"chandniyadav@ucreate.co.in",
"Chandra Prakash":"chandra.prakash@innoverdigital.com",
"Chandra Ratra":"chandra.ratra@navigaglobal.com",
"Chandrakanth K":"chandra@srivensys.com",
"Chandrasekhar Gv":"cgv@eclinicalsol.com",
"Chandrashekar R":"chandrashekarr@softura.com",
"Chandresh Kumar":"chandresh.kumar@jagrannewmedia.com",
"Charan Singh":"charan@srinipharma.com",
"Charles Timothy":"charles.t@palni.com",
"Charmaine Pinto":"charmaine@streamoid.com",
"Cheryl Anjelo":"cheryl.anjelo@colortokens.com",
"Chetan Verma":"cverma@fcsltd.com",
"Chetna Gogia":"chetna@gokwik.co",
"Chhavi Bhatnagar":"chhavi.bhatnagar@acnovate.com",
"Chinmoy Roy":"chinmoy.roy@catalyst-us.com",
"Chintan Bhatt":"b.chintan@introlligent.com",
"Chirag Patel":"chirag.patel1@rangtech.com",
"Chirag Shah":"chirag.shah@iflair.com",
"Chiranjeevi Pannem":"chiranjeevip@byteridge.com",
"Chitra Markale":"chitram@zconsolutions.com",
"Chitra Ravi":"chitra.ravi@ample.co.in",
"Cireesha Mailavarapu":"cireesha.m@etisbew.com",
"Crp Saurabh":"saurabh@caastle.com",
"Cynthia Rodrigues":"cynthia@netcore.co.in",
"Damayanti Ghosh":"damayanti.ghosh@getvymo.com",
"Daniel Shaw":"daniel.shaw@kpipartners.com",
"Dathree Javvadi":"dathree.javvadi@vncservices.in",
"Debashish Bhattacharya":"debashishb@interrait.com",
"Debdutta Bhowmick":"debdutta.bhowmick@atidiv.com",
"Debojit Das":"debojit.das@betterplace.co.in",
"Deborah Passanha":"dpassanha@everydayhealth.com",
"Deep Ambike":"deep@thinkbridge.in",
"Deep Patel":"deep.patel@ics-global.in",
"Deepa Baburaj":"bdeepa@zeomega.com",
"Deepa Dand":"deepa@prdxn.com",
"Deepa Makhija":"deepa.makhija@gupshup.io",
"Deepa Mukherjee":"deepa.mukherjee@esri.in",
"Deepa Palaniswamy":"deepa.palaniswamy@ducenit.com",
"Deepa Sripathi":"deepa.sripathi@konicaminolta.com",
"Deepak Babu":"deepak.babu@appviewx.com",
"Deepak Chavan":"deepak.chavan@visiblealpha.com",
"Deepak Deshpande":"deepak.deshpande@netmagicsolutions.com",
"Deepak Gelda":"deepak@uchicago.edu",
"Deepak Khanna":"dkhanna@ishir.com",
"Deepak Melwani":"deepak.melwani@galaxyweblinks.co.in",
"Deepak Pawar":"deepak.pawar@accutech.co.in",
"Deepak Ramakrishnan":"deepak.ramakrishnan@csquare.in",
"Deepak Singh":"deepak@dixitindia.com",
"Deepali":"deepali@proximity.tech",
"Deepali Verdi":"deepali.verdi@genzeon.com",
"Deepashree V":"deepashree.v@skience.com",
"Deepika Pandita":"deepika@appinessworld.com",
"Deepika Singh":"deepika@webkul.com",
"Deepthi Kesireddy":"deepthi.kesireddy@smartims.com"


  
}


# Email content template
SUBJECT = f"Application for Java Developer | 5 Years Experience"

EMAIL_BODY = """ 
Dear Hiring Manager,
I am applying for the Java Developer position. I have 5 years of experience in Java backend development, including Spring Boot, Microservices, REST APIs, Hibernate, SQL, and Java 8 to Java 17 migration. Currently, I am working as a Senior Software Engineer on US-based enterprise projects.

Below is my skill summary:

Category:	Skills
Languages:	Java, Python (Learning)
Backend:	Spring Boot, Spring MVC, JPA, Hibernate,Microservices	REST APIs, Eureka, Feign, API Gateway
Database:	MySQL, Oracle, PostgreSQL
Frontend:	javaScript,AngularJS
Tools:	    Maven, Gradle, Git,Cloud / DevOps	Docker, CI/CD basics
Other:	Design Patterns, Stream API, Exception Handling
Migration:	Java 8 → Java 17

I have attached my resume for your review. I would appreciate the opportunity to interview.
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
        msg['Subject'] = f"Application for Java Developer | 5 Years Experience"
        
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