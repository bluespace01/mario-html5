import http.server
import ssl

# 设置监听端口
PORT = 9090

# 设置服务器地址和目录
Handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('0.0.0.0', PORT), Handler)

# 加载证书和私钥文件
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile="server.cert",
    keyfile="server.key",
    server_side=True
)

print(f"Serving HTTPS on https://0.0.0.0:{PORT}")
httpd.serve_forever()

