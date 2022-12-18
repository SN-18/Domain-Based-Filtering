# Domain-Based-Filtering
Filtering Third Party Domains from FLD's (Full Legth Domains)  

##Third Party Domains
Third Party Domains are defined as web pages or url’s visited on through the main page that is accessed by a user. In this context, a user’s end device is often called as the second party, and the main page where the ,’third party is parked’, is called the first party.

##Filtering
It refers to separating the first party or the intended page that is being visited by the user, from the third party url’s. 

##HTTP archive format
It refers to the HAR format which contains information about third party domains visited for a particular page, which in our example would be the official Macy’s and CNN websites.

##Raw Rules
It refers to the rules generated to achieve Ad-blocking. They are implemented as a list, with each list being implemented as an and-or statements of simple statements, such as given as:
 

#How to run the project
