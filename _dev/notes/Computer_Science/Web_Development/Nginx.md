---
title: Nginx
---

For Ubuntu 18.04+

## Installation

```sh
sudo apt update
sudo apt install nginx
```

Start the service

```sh
sudo service nginx start
sudo service nginx status
```

If the firewall is set up, you can access the server at `localhost`, your public IP address, or your domain name if your router has forwarded port 80.

## Firewall

Nginx provides the following applications to the firewall,

```
Nginx Full
Nginx HTTP
Nginx HTTPS
```

Allow the Nginx application  you use through the firewall:

```sh
sudo ufw allow 'Nginx HTTP'
```

## Virtual Host / Server Block
The equivalent of virtual host on Nginx is called server blocks. There already exists one by default at `/var/www/html`. To support multiple domains you need to have multiple server blocks. Regardless, it's highly recommended to create another one for each web application (i.e., leave `/var/www/html` when you want to manually write and serve HTML which is rare).

Replace `example.com` with your own domain name (without `www`).

```sh
sudo mkdir -p /var/www/example.com/html/
sudo chown -R $USER:$USER /var/www/example.com/html/
sudo chmod -R 755 /var/www/example.com/
```

For testing, you may add `index.html` to `/var/www/example.com/html/`. Here is a boilerplate:

```html
<html>
    <head>
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Success! Hello, World!</h1>
    </body>
</html>
```

This particular web page will not be accessible until we register the server block in configurations on the next section.

### Configuration
Server block configuration are located at `/etc/nginx/sites-available/` and enabled at `/etc/nginx/sites-enabled/`. We will first add the server block configuration to `/etc/nginx/sites-available/example.com`

```nginx
# /etc/nginx/sites-available/example.com
server {
        listen 80;
        listen [::]:80;

        root /var/www/example.com/html;
        index index.html index.htm index.nginx-debian.html;

        server_name example.com www.example.com;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

Then register by symbolic link:

```sh
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```

On Nginx configuration file `/etc/nginx/nginx.conf`, uncomment the hash bucket size

```nginx
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
```

Check for syntax error:

```sh
sudo nginx -t
```

Fix any error and restart Nginx server:

```sh
sudo systemctl restart nginx
```

## Nginx Configurations

### Gunicorn
For a gunicorn hosted project with the project folder at `/path/to/project`, the application program is `app.py` with WSGI also named `app`.

```sh
gunicorn -b 0.0.0.0:8000 app:app
```

 the Nginx configuration should look something like this:

```nginx
server {
	listen 80;
	server_name example.com www.example.com;

	# Root of project to access static
	root /path/to/project;

	# Optional, ignore favicon error
	# location = /favicon.ico {access_log off; log_not_found off;}


	location / {
		proxy_pass http://0.0.0.0:8000 ;
	}
}
```