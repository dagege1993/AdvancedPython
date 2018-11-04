# requests -> urllib ->socket
import socket
from urllib.parse import urlparse  # 用来做url解析的


def get_url(url):
    # 通过socket请求Html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    print('解析的url:', host, path)
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))  # http端口都是80

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    html_data = data.split("\r\n\r\n")[1]
    # print(data)
    print(html_data)
    client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
