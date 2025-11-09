import pywhatkit as pwk

phone_number = "+923361756540"  # Replace with the target phone number
message = "Hello, this is a test message sent using pywhatkit!"  # Replace with your message

# Send the WhatsApp message
pwk.sendwhatmsg(phone_number,message, 15,55)

