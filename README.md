# Domain-Based-Filtering
Filtering Third Party Domains from FLD's (Full Legth Domains)  

## Third Party Domains
Third Party Domains are defined as web pages or url’s visited on through the main page that is accessed by a user. In this context, a user’s end device is often called as the second party, and the main page where the ,’third party is parked’, is called the first party.

## Filtering
It refers to separating the first party or the intended page that is being visited by the user, from the third party url’s. 

## HTTP archive format
It refers to the HAR format which contains information about third party domains visited for a particular page, which in our example would be the official Macy’s and CNN websites.

## Raw Rules
It refers to the rules generated to achieve Ad-blocking. They are implemented as a list, with each list being implemented as an and-or statements of simple statements, such as given as:

<img width="740" alt="image" src="https://user-images.githubusercontent.com/83748468/208290826-e102e578-9b29-4774-ac9d-040c31a40658.png">

*Source [Filter-Rules](https://adblockplus.org/filter-cheatsheet)*
 

## How to run the project

1. Make sure to have Python 3.X installed (Here X represents any variant of Python 3, such as Python 3.11)
2. To check what version of python your system has, open a command line tool such as terminal or cmd and type:

''' $ python --version '''

and you should get the following output:
<img width="571" alt="image" src="https://user-images.githubusercontent.com/83748468/208292479-c0aa936b-4fe5-4af8-8b4b-8acef3ebce4a.png">





