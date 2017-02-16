Limiting the number of requests and wrap traffic

NGINX. Create a virtual host

geo $exclusions {
        default 1;
        include /etc/nginx/conf.d/ban;
}

upstream app {
        least_conn;
	server 192.168.1.1;
	server 192.168.1.2;
	server 192.168.1.3;
	...
  }



if ($uri !~ /ban/$){

        set $block "A";

}

if ($uri ~ /ban/$){

        set $block "B";

}

if ($exclusions = "0"){

        set $block "${block}C";

}

if ($block = "AC"){

     rewrite ^(.*)$ http://ban.info-linux.ru:8080/ban/ last;

}



location = /ban/ {

	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_pass http://192.168.1.4:8080;
}




Following is an example on php and bash script in the folder ban



																
