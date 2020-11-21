
from pyngrok import ngrok
# kill ngrok
ngrok.kill()

# open HTTP tunnel on default port 80
public_url = ngrok.connect(port = '80')

# Open ssh tunnel
# ssh_url = ngrok.connect(22, "tcp")

print(public_url)


    
    
