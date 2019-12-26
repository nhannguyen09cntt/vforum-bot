# vforum-bot
pip3 install -r requirements.txt

# Pull docker-selenium
docker pull elgalu/selenium

# Pull Zalenium
docker pull dosel/zalenium
      
docker run --rm -ti --name zalenium -p 4444:4444 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/videos:/home/seluser/videos \
  --privileged dosel/zalenium start


curl -d '{"title": "How can I render markdown to a golang template(html or tmpl) with blackfriday", "url": "https://4rum.vn/t/how-can-i-render-markdown-to-a-golang-template-html-or-tmpl-with-blackfriday/2310"}' http://localhost:8080


curl -d '{"title": "Create a Certificate Signing Request (CSR) with an email address in Go", "url": "https://4rum.vn/t/create-a-certificate-signing-request-csr-with-an-email-address-in-go/2309"}' http://localhost:8080
