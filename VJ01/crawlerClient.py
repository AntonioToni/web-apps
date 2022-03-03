import socket, time, re

list_link= []
j=0

def connect_to_server(ip,port,retry=3):
    s=socket.socket()
    try:
        s.connect((ip,port))
    except Exception as e:
        print (e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       
    
    return s

def get_source(s,ip,page):
    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    print (response)
    return response

def get_all_images(response,s,ip):
    global list_link
    beg = 0
    while True:
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return list_link  
        end_str = response.find('"', beg_str + 6)      
        img = response[beg_str + 6:end_str]
        global j
        j=j+1
        if '.html' in img and 'http' not in img:
            if img not in list_link:
                list_link.append(img)
        beg = end_str + 1

            
        

for j in range(7):          
    ip = 'www.optimazadar.hr'
    port = 80
    page = '1280/djelatnost1280.html'
    s = connect_to_server(ip, port)
    response = get_source(s, ip, page)
    link_lists=get_all_images(response,s,ip)
    for i in link_lists:
        page= ip+"/"+ i
        s = connect_to_server(ip, port)
        response=get_source(s,ip,page)
print (get_all_images(response,s,ip))