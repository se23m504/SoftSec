# Software Security

## HW1

Write a small web application in the language of your choice. Your application should  be able to calculate a given number of passwords out of a predefined alphabet and has a limit of 10 passwords per run. Implement client side checks (not backend) to ensure that limit and try to bypass your limit with OWASP ZAP Attack Proxy.

## HW2

Server: http://haklab-n1.cs.technikum-wien.at/sql

Find all information about the following properties in the SQL server:

1. ID, firstname, lastname
2. username, password
3. svnr, protected, license, salery, hobbies
4. database version, current user, server version

## HW3

Server: http://haklab-n1.cs.technikum-wien.at/xss

Challenge 1: Site Defacing / HTML Injections

Try to interfer with the site's layout:

1. Set the background to a different color
2. Display another image on the website
3. Create a link on the website

Challenge 2: JavaScript / Cross Site Scripting

1. Popup: Display a message to the client
2. Redirect the client to some other website
3. Create a session with the server and display the current sesssion ID
4. Try to load JS code from a different web source into the website

Challenge 3: Javascript / Cookie Catcher

1. Write a "Cookie Catcher", Clientside: Javascript, Backend: PHP

Save the cookie information to a log file. Give examples how this attack could be prevented.
