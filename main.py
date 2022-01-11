from Assign import assign
from twilio.rest import Client

account_sid = 'enter account_sid here'
auth_token = 'enter auth_token here'
client = Client(account_sid, auth_token)

masterList = assign()
for x in masterList:
    phone = x.getPhone()
    myMessage = "Merry Christmas " + x.getName() + "!\n" + \
                    "For Secret Santa 2021, you have " + x.getGifteeName() + "!" + "\n" + x.getName() + "'s wish list: " + x.getGifts()

    message = client.messages \
        .create(
             body=myMessage,
             from_='enter number here',
             to=phone
         )

    print(message.sid)

for i in masterList:
    printMaster = i.getName() + " has " + i.getGifteeName()
    print(printMaster)