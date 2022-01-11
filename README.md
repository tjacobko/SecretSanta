# SecretSanta
This one goes out to all of those who wished the process of picking names for Secret Santa was more efficient.

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
