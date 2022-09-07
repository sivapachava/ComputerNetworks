# Tool Used - 
* Python - 3.9
* Pycharm community edition
* SQlite Database
* SQlite Studio
* Draw.io for drawing the UML diagrams
* QT Designer  - For Designing the user interface
* WireShark - for checking the communication status between the nodes

# Predefined Python Modules used - 
* rsa  - For Asymmetric Encryption(need to install separately)
* Threading  - For concurrent programming - inbuilt 
* socket  - For Network programming - inbuilt
* pathlib - Get the location of files 
* SQLite - For connecting to the Sqlite database
* json -  To convert the json string to dictionary and vice versa
* PyQT5  - for creating the user interface

# Project Organization - 
We followed the SCRUM methodology for this project development.We have several sprint and after the end of each sprint we review the work done on that time and check if the target is achieved or not.

## Sprint - 1 - 
### The main objective of this sprint is write the protocol document.
 |ID|Task Name|
 |---------------|--------------|
 |#1|Understand the full requirements of this project|
 |#2|Study about the Blockchain working|
 |#3|Study about the peer to peer networking|
 |#4|Define the types of messages that are transmitted in the peer to peer network|
 |#5|Design the structure of messages that are transmitted in the peer to peer network|
 |#6|Write the protocol document according to the message types defined with format of each message|

## Sprint - 2 - 
### The main objective of this sprint is develop a working blockchain without networking.
 |ID|Task Name|
 |---------------|--------------|
 |#7|Design the structure of the Blockchain|
 |#8|Design the modules required for the creating the working BlockChain|
 |#9|Create the modules to make transactions,transaction ledger|
 |#10|Create a module to make the block as per the structure designed|
 |#11|Create a module to calculate  the Merkel Root of all transactions in the ledger|
 |#12|Create a module to Mine the created Block as per difficulty target and calculate the nonce|
 |#13|Create a module to calculate the Genesis Block(First block in the block chain)|
 |#14|Complete the testing of the above modules and make sure that all are working as per the requirement|

## Sprint - 3 - 
### The main objective of this sprint is to develop the networking aspects and test the blockchain.
 |ID|Task Name|
 |---------------|--------------|
 |#15|Learn about the socket programming and do the required test|
 |#16|Create modules to structure the message required for the sending and receiving in the network as per the protocol document|
 |#17|Design the database and identifying the table required|
 |#18|Create modules to do the CRUD operations for each tables in the database|
 |#19|Create module for receiving and sending message in the peer to peer network using the socket programming|
 |#20|Create the Tracker server as per design|
 |#21|Integrate all modules in the main program|
 |#22|So the required testing and make sure every thing is working fine|

## Sprint - 4 - 
### The main objective of this sprint is to add the additional functionalities like message queue system and automatic liveliness test of peers by tracker.
 |ID|Task Name|
 |---------------|--------------|
 |#23|Add the message queue system in the block chain to store the mined Blocks|
 |#24|Add the message queue system in the tracker to store the new peer details|
 |#25|Add the liveliness test of peers by tracker|
 |#26|Do the testing and make sure the system is working fine|
 |#27|Create the user interface for the blockchain|
 |#28|Do the testing of user interface|

# Difficulties we faced during the implementation of this application - 

|ID|Difficulties|
|---------|-----------|
|1|Designing the Asymmetric cryptography is the first difficulty we faced while implementing the block chain.We tested many modules and final found one that is "rsa",During the initial testing the module was working perfectly.But there was a problem in that module that is we can't able to double encrypt the message for achieving both Authentication and confidentiality.We already lost lot of time for testing this module.We didn't plan to change te module,instead of that we give digital signature for the authentication and encrypt the message for confidentiality(Already explain in details about our design of Asymmetric cryptography in ProjectDescription.md file)  |
|2|Understanding the concept of network programming.We do lot of testing using socket module using python to understand the concept.Finally we reached our goal |
|3|Couldn't able to send the public key in the network. Because the type of public key is ""<class 'rsa.key.PublicKey'>"".To send via network we need to convert it into string and then bytes.But after that it can't convert back to its initial datatype. So here we can't able using it for encryption or for validation.The issue is still in the system|
|4|We waste lot of time in looking for a small problem.that is buf-size.Initially our buf-size was 1024.But when try to send long messages some data are missing and thus causing error in the application .after a  long testing we found that it was caused due to the buf-size.After that it changed to 4096|
|5|Now is How to return value from a threaded function.This issue also consume lot of our time.Finally solve the issue by using the queue data structure|
|6|We did the project in mainly two different phase one is BlockChain and other is the Networking.We need to change a lot while doing in the networking part from Blockchain logic.This is occurred due to the improper planning about the whole implementation of the project and start the BlockChain programming without planning the network part |

# Lessons learned from the implementation - 

|ID|lessons learned|
|-------------|--------------|
|1|Learned the concept about blockchain and knows it importance|
|2|Learned the working of peer to peer networking|
|3|Learned about the socket programming using python|
|4|Learned about the multi-threading concept|
|5|Learned about asymmetric cryptography|
|6|Learned about SQlite database and understand its advantages|
|7|Learned about Message Queuing System|

# what you would keep for next time -

|ID|Thing keep for the next time|
|-------------|--------------|
|1|Module based development which is more robust and flexible style of coding.We can easily add things here and also troubleshoot is also very easy|
|2|Continuous testing of logic makes easier to find bugs at earlier stage|
|3|Usage of github for version control|


# what you would do differently - 

|ID|Improvements Areas|
|-------------|--------------|
|1|Project management should be improved better and also need to use tools like Trello,Confluence etc for the improved result|
|2|Have a proper plan of designing the whole system before start the coding.Learn all concepts used in the programming,do the required poc(Proof of concept) before starting the development.Also, Draw the UML diagram if required, Atleast the sequence diagram before developing|
|3|Create a user interface for the system |
|4|Create a wallet for the users outside the network.So that they can also use the full benefits and also give a user authentication system |
|5|Do the Automated testing of the application|
|6|Write the unit test to know  the bugs and stability of the system in all conditions|
|7|BlockChain validation part should be improved further like frequently calculate the hash of the each block in the chain and make sure that the data is unchanged by validating the lead zeros in each hash|
<<<<<<< HEAD
|8|Give different ports for different message for receiving  to reduce the traffic(complex programming required| 
|9|Improved message queue architecture|
|10|Synchronization of the different messages in the network should be improved.Currently some bugs like message duplication in the database , are there due to this.Need to solve|
=======
|8|Give different ports for different message for receiving  to reduce the traffic(complex programming required)| 
|9|Improved message queue architecture|
|10|Synchronization of the different messages in the network should be improved.Currently some bugs like message duplication in the database , are there due to this.Need to solve|

>>>>>>> 3d75ede89d6923fa524a3e68893927e38551a785
