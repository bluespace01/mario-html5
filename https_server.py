import http.server
import ssl
import os

# 设置监听端口
PORT = 9090

# 切换当前工作目录到 dist 目录
os.chdir("dist")

# 设置服务器地址和目录
Handler = http.server.SimpleHTTPRequestHandler

# 创建 HTTPServer 实例
httpd = http.server.HTTPServer(('0.0.0.0', PORT), Handler)

# 创建 SSL 上下文
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="../ssl/localhost.pem", keyfile="../ssl/localhost-key.pem")

# 将 SSL 上下文应用到服务器的 socket 上
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on https://0.0.0.0:{PORT}")
httpd.serve_forever()

