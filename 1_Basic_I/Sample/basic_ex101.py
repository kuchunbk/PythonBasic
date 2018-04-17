'''Question: 
Write a Python program to access and print a URL's content to the console.
'''

# Python code: 

from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)


'''Output sample: 
b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title
>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-ty
pe" content="text/html; charset=utf-8" />\n    <meta name="viewport
" content="width=device-width, initial-scale=1" />\n    <style type
="text/css">\n    body {\n        background-color: #f0f0f2;\n     
   margin: 0;\n        padding: 0;\n        font-family: "Open Sans
", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }
\n    div {\n        width: 600px;\n        margin: 5em auto;\n    
    padding: 50px;\n        background-color: #fff;\n        border
-radius: 1em;\n    }\n    a:link, a:visited {\n        color: #3848
8f;\n        text-decoration: none;\n    }\n    @media (max-width: 
700px) {\n        body {\n            background-color: #fff;\n    
    }\n        div {\n            width: auto;\n            margin:
 0 auto;\n            border-radius: 0;\n            padding: 1em;\
n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    
<h1>Example Domain</h1>\n    <p>This domain is established to be us
ed for illustrative examples in documents. You may use this\n    do
main in examples without prior coordination or asking for permissio
n.</p>\n    <p><a href="http://www.iana.org/domains/example">More i
nformation...</a></p>\n</div>\n</body>\n</html>\n'
'''