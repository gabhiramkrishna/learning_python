from twilio import rest

account_sid="ACbeeae95beaa6c8fb88f350dc7f7d3106"
auth_token="35dbac7dcc1ab1622a95884b2fd350c1"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body = "Hey Akki! My python code says Yo!", to="+18475256202", from_="+14083291964")
print message.sid
