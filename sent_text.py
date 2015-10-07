from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC587f678626e382789e67496fe5153167"
auth_token  = "b3ccfa1a322eb284577abdca6f2765a6"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Who are you?! I love you <3",
    to="+886911507360",    # Replace with your phone number
    from_="+18452622275") # Replace with your Twilio number
print message.sid
