from Assign import assign
from twilio.rest import Client

account_sid = 'ACbb50c29ed79dbf578cc268bb3e805634'
auth_token = 'a39275efe65263910e6e9248d7e8421e'
client = Client(account_sid, auth_token)

masterList = assign()
for x in masterList:
    phone = x.getPhone()
    myMessage = "Merry Christmas " + x.getName() + "!\n" + \
                    "For Secret Santa 2021, you have " + x.getGifteeName() + "!"
                    # "\n" + x.getName() + "'s wish list: " + x.getGifts()

    message = client.messages \
        .create(
             body=myMessage,
             from_='+19284400812',
             to=phone
         )

    print(message.sid)

for i in masterList:
    printMaster = i.getName() + " has " + i.getGifteeName()
    print(printMaster)