# rewiser-gpt

A github action to manage your daily devlogs and help you revise them regularly.

## How it works?

1. Hook this github-action to your devlog repository
2. Mention the directory and file type where all the devlogs are stored
3. The action will figure out the order of the files and will use anki style algorithm to create your daily roster.
4. It will send the daily roster via email, for emails to work, it will require smtp hostname and credentials.
5. Each roster is powered by ai (for the following to work openAI key will be required and each of the following will be provided as parameter):
    1. To ease up memorization, the roster will be summarized by some memory technique like a limerick or a story or a visualisation.
    2. At the end of each roster, there will be a quiz and link for additional resources to learn.


For example, if following is the text for roster: 
```
"database replicas are used to enhance read scalability and guard against data loss. 
Application can write only to primary node, while the application can read from primary 
as well as replicas. Asynchronous replication (or some other) mechanism is used to keep
the replicas synchronised with primary node."
```

Chatgpt can generate the following:

1. A MCQ style question:
```
Which mechanism is used to keep the replicas synchronized with the primary node in a database setup?

A) Load balancing
B) Asynchronous replication
C) Sharding
D) Indexing
```
2. A limerick:
```
In a database, replicas do shine,
Boosting reads and keeping data in line.
Writes to the primary alone,
Reads from replicas, where they're shown.
Synced by replication, all works fine!
```
3. Using storytelling:
```
Once upon a time, in the realm of databases, there was a kingdom ruled by a powerful primary node.
The primary node had the unique ability to receive messages and updates from the kingdom's applications,
allowing it to maintain the most up-to-date information.

However, the primary node realized that it needed some assistance to handle the increasing demand for 
reading data. So, it decided to create replicas, faithful copies of itself, to enhance read scalability.
These replicas were like trusted advisors, ready to serve the applications' requests for information.

The applications, though, were only allowed to send their messages to the primary node. It was like a 
secret passage guarded by the primary node, ensuring the integrity of the data. But when it came to 
reading data, the applications had more freedom. They could seek knowledge not only from the primary 
node but also from the replicas, like exploring different corners of the kingdom.

To maintain harmony and ensure that all replicas were in sync with the primary node, a special 
mechanism called asynchronous replication was put in place. It was like a magical thread that connected 
the replicas and the primary node. Whenever a change occurred in the primary node, it sent whispers 
through this thread, informing the replicas to update themselves accordingly. This way, they stayed 
synchronized, preventing any inconsistencies or data loss.

And so, the kingdom's database thrived with the power of replicas, providing both read scalability 
and data protection. The primary node ruled over the applications, while the replicas served as 
trustworthy companions, all working together through the enchantment of asynchronous replication. 
The end.
```

