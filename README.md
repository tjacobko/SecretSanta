# SecretSanta
This one goes out to all of those who wished the process of picking names for Secret Santa was cooler and more efficient.

## What it does
TL;DR this program randomly assigns a group of people a secret santa and anonymously texts each person who they recieved along with their wish list.

From a list of people, each person is randomly assigned another person to be their secret santa according to these **rules**:
1. A person CAN NOT be a secret santa for someone within their own family (e.g. John Doe cannot get Jane Doe)
2. A person CAN NOT be chosen more than once
3. A person CAN NOT be their own secret santa
After each person is assigned a secret santa, they are texted the name of the person that they will be giving a gift to, along with that person's wish list.

## How it works
A connected Google Sheet document containing the First Name, Last Name, Wish List, and Phone Numbers of each person is read, and corresponding *Person* objects are created.
These *Person* objects are pushed into a list called *personList*. Each *person* object in *personList* will randomly be assigned another *person* object following the rules
specified above. After all *person* objects have been assigned, each *person* is texted the information of the person they have been assigned.

## Usability
To use the program, you must have a working Twilio account that you can set up [here](https://www.twilio.com/docs/sms). When set up, you can enter your *account_sid*, *auth_token*, and *from_* into the corresponding spots in **main.py**.

Additionally, you will need to set up Google Sheets to work with your program with instructions [here](https://www.youtube.com/watch?v=bu5wXjz2KvU&ab_channel=PrettyPrinted).
When set up, you need to format a worksheet in the following manner:
- Column 1: **First Name**
- Column 2: **Last Name**
- Column 3: **Wish List**
- Column 4: **Phone Number**
Additionally, all rows below the last row with information must be deleted.

Here is an example of a properly formatted worksheet:
![SecretSanta_worksheet](https://user-images.githubusercontent.com/56098325/149064533-5a772b79-753f-4c35-859e-60521d00ecf8.png)
