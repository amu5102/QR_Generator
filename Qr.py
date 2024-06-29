import qrcode

upi_id = input("Enter your UPI ID: ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Nmae&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Nmae&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Nmae&mc=1234"

# Create QR Code for each app
phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

# Save QR Codes
phonepe_qr.save("phonepe_qr.png")
google_pay_qr.save("google_pay_qr.png")
paytm_qr.save("paytm_qr.png")

# Display QR Codes 
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()





