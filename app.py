from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Dummy Property Data
# properties = [
#     {"id": 1, "name": "Luxury Villa", "location": "Mumbai", "price": 200000000, "display_price": "₹2 Cr", "type": "Villa", "image": "house1.jpg", "description": "A luxury villa in the heart of Mumbai."},
#     {"id": 2, "name": "3BHK Apartment", "location": "Pune", "price": 90000000, "display_price": "₹80 Lakh", "type": "Apartment", "image": "house2.png", "description": "A modern 3BHK apartment with great amenities."},
#     {"id": 3, "name": "Beach House", "location": "Goa", "price": 150000000, "display_price": "₹1.5 Cr", "type": "Villa", "image": "house3.jpg", "description": "A beautiful beach house with an ocean view."}
# ]
# Dummy Property Data with Key Features
properties = [
    # {
    #     "id": 1,
    #     "name": "3BHK Apartment",
    #     "location": "Pune",
    #     "price": 80000000,
    #     "display_price": "₹80 Lakh",
    #     "type": "Apartment",
    #     "image": "house2.png",
    #     "floor_plans_2bhk" : "floor_plan_2bhk.png",
    #     "floor_plans_3bhk" : "floor_plan_3bhk.png",
    #     "description": "A modern 3BHK apartment with great amenities.",
    #     "parking": "Yes",
    #     "security": "Gated Community",
    #     "size": "1800",
    #     "garden": "No",
    #     "pool": "Yes"
    # }
    {
        "id": 1,
        "name": "3BHK Apartment",
        "location": "Pune",
        "price": 80000000,
        "display_price": "₹80 Lakh",
        "type": "Apartment",
        "image": "house2.png",
        "floor_plans_2bhk": "floor_plan_2bhk.png",
        "floor_plans_3bhk": "floor_plan_3bhk.png",
        "description": "A modern 3BHK apartment with great amenities.",
        "parking": "Yes",
        "security": "Gated Community",
        "size": "1800",
        "garden": "No",
        "pool": "Yes",
        "connectivity": {
            "inner_ring_road": "Just 50 mts from Inner Ring Road.",
            "sangam": "Just 8 km from Sangam.",
            "civil_lines": "Just 12 km from Civil Lines.",
            "jhunsi_railway_station": "Just 4 km from Jhunsi Railway Station.",
            "nidaan_hospital": "Just 2.6 km from Nidaan Hospital."
        }
    }

    # {
    #     "id": 2,
    #     "name": "Luxury Villa",
    #     "location": "Mumbai",
    #     "price": 200000000,
    #     "display_price": "₹2 Cr",
    #     "type": "Villa",
    #     "image": "house1.jpg",
    #     "description": "A luxury villa in the heart of Mumbai.",
    #     "parking": "Yes",
    #     "security": "24/7 Security",
    #     "size": "4500",
    #     "garden": "Yes",
    #     "pool": "Yes"
    # },
    # {
    #     "id": 3,
    #     "name": "Beach House",
    #     "location": "Goa",
    #     "price": 150000000,
    #     "display_price": "₹1.5 Cr",
    #     "type": "Villa",
    #     "image": "house3.jpg",
    #     "description": "A beautiful beach house with an ocean view.",
    #     "parking": "Yes",
    #     "security": "Private Security",
    #     "size": "3500",
    #     "garden": "Yes",
    #     "pool": "Yes"
    # }
]


# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'ramnamahconstructions@gmail.com'
app.config['MAIL_PASSWORD'] = 'tefo ewqt tqzo vfqm'  # Use Google App Password
app.config['MAIL_DEFAULT_SENDER'] = 'ramnamahconstructions@gmail.com'

mail = Mail(app)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

#from flask import url_for
# Handle Contact Form Submission (Send Inquiry + Thank You Email)
@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        name = request.form['name']
        mobile = request.form['number']
        email = request.form['email']
        message = request.form['message']

        # ✅ Send Inquiry Email to Business
        msg = Message(subject="New Inquiry from Contact Form", recipients=["ramnamahconstructions@gmail.com"])
        msg.body = f"Name: {name}\nMobile: {mobile}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        # ✅ Send Thank You Email to the User (Professional HTML Email)
        thank_you_msg = Message(subject="Thank You for Contacting Us!", recipients=[email])
        thank_you_msg.html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
            <table style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <tr>
                    <td align="center">
                        <img src="https://i.imgur.com/4MnFeXe.png" alt="Company Logo" width="150" />
                    </td>
                </tr>
                <tr>
                    <td>
                        <h2 style="color: #333;">Hello {name},</h2>
                        <p>Thank you for reaching out to <b>RAM NAMAH CONSTRUCTION PVT. LTD.</b></p>
                        <p>We have successfully received your inquiry and will get back to you as soon as possible.</p>
                        <hr>
                        <p><b>Your Submitted Details:</b></p>
                        <p>Name: {name} <br> Mobile: {mobile} <br> Email: {email} <br> Message: {message}</p>
                        <hr>
                        <p>Our team will contact you shortly.</p>
                        <p style="font-size: 14px; color: #777;">Best Regards, <br> <b>RAM NAMAH CONSTRUCTION PVT. LTD.</b></p>
                    </td>
                </tr>
                <tr>
                    <td align="center" style="padding: 10px; background: #222; border-radius: 5px;">
                        <p style="margin: 0; color: white;">Follow us on social media</p>
                        <a href="https://www.instagram.com/invites/contact/?igsh=dv4rd43woflq&utm_content=wvvm0a1">
                            <img src="https://i.imgur.com/FGkFuxX.png" alt="Instagram" width="24" />
                        </a>
                    </td>
                </tr>
            </table>
            <p align="center" style="font-size: 10px; color: #777;">
                © 2024 RAM NAMAH CONSTRUCTION PVT. LTD. All Rights Reserved.
            </p>
        </body>
        </html>
        """
        mail.send(thank_you_msg)

        return jsonify({"success": True, "message": "Message sent successfully! A Thank You email has also been sent."})

    except Exception as e:
        print(f"Error: {e}")  # Logs the error to the console for debugging
        return jsonify({"success": False, "error": str(e)})





# Properties Page
@app.route('/properties')
def properties_page():
    return render_template('properties.html', properties=properties)

# Property Details Page
@app.route('/property/<int:property_id>')
def property_details(property_id):
    property_data = next((p for p in properties if p["id"] == property_id), None)
    if property_data:
        return render_template('property_details.html', property=property_data)
    else:
        return "<h1>Property Not Found</h1>", 404

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
