NGINX_SERVER_CONF_TEMPLATE = """
server {{
    client_max_body_size 0m;
    listen       {port} default_server;
    listen       [::]:{port} default_server;
    server_name  _;
    {access_log_off}

    location / {{
        include         uwsgi_params;

        # change this to the location of the uWSGI socket file (set in uwsgi.ini)
        uwsgi_pass                  unix:{sock_filepath};
        uwsgi_ignore_client_abort   on;
    }}
}}

"""

NGINX_SERVER_CONF_TEMPLATE2 = """
worker_processes auto;
pid /tmp/nginx.pid;
error_log stderr;

events {{
	worker_connections 768;
	# multi_accept on;
}}

http {{

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	##
	# Gzip Settings
	##

	gzip on;

    server {{
        client_max_body_size 0m;
        listen       {port} default_server;
        listen       [::]:{port} default_server;
        server_name  _;
        {access_log_off}

        location / {{
            include         /etc/nginx/uwsgi_params;
            
            # change this to the location of the uWSGI socket file (set in uwsgi.ini)
            uwsgi_pass                  unix:{sock_filepath};
            uwsgi_ignore_client_abort   on;
        }}
    }}
}}
"""