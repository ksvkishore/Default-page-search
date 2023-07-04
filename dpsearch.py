import requests
import argparse
import time

def check_default_pages(url, filter_status_codes=None, rate_limit=None, check_all=False):
    base_url = url.rstrip('/')  # Remove trailing slash from the URL if present

    common_paths = [
        "",  # Root path
        "/index.php",
        "/index.html",
        "/login.php",
        "/login.html",
        "/admin/",
        "/admin/index.php",
        "/admin/index.html",
        "/admin/login.php",
        "/admin/login.html",
        "/administrator/",
        "/administrator/index.php",
        "/administrator/index.html",
        "/administrator/login.php",
        "/administrator/login.html",
        "/wp-admin/",
        "/wp-login.php",
        "/wp-login.html",
        "/wp-admin.php",
        "/wp-admin.html",
        "/wp/wp-admin/",
        "/wp/wp-login.php",
        "/wp/wp-login.html",
        "/wp/wp-admin.php",
        "/wp/wp-admin.html",
        "/wordpress/",
        "/wordpress/index.php",
        "/wordpress/index.html",
        "/wordpress/login.php",
        "/wordpress/login.html",
        "/wp-content/",
        "/wp-content/index.php",
        "/wp-content/index.html",
        "/wp-content/themes/",
        "/wp-content/plugins/",
        "/phpmyadmin/",
        "/phpmyadmin/index.php",
        "/phpmyadmin/index.html",
        "/phpmyadmin/login.php",
        "/phpmyadmin/login.html",
        "/pma/",
        "/pma/index.php",
        "/pma/index.html",
        "/pma/login.php",
        "/pma/login.html",
        "/adminer/",
        "/adminer/index.php",
        "/adminer/index.html",
        "/adminer/login.php",
        "/adminer/login.html",
        "/MyAdmin/",
        "/MyAdmin/index.php",
        "/MyAdmin/index.html",
        "/MyAdmin/login.php",
        "/MyAdmin/login.html",
        "/dbadmin/",
        "/dbadmin/index.php",
        "/dbadmin/index.html",
        "/dbadmin/login.php",
        "/dbadmin/login.html",
        "/database_administration/",
        "/database_administration/index.php",
        "/database_administration/index.html",
        "/database_administration/login.php",
        "/database_administration/login.html",
        "/administer/",
        "/administer/index.php",
        "/administer/index.html",
        "/administer/login.php",
        "/administer/login.html",
        "/webadmin/",
        "/webadmin/index.php",
        "/webadmin/index.html",
        "/webadmin/login.php",
        "/webadmin/login.html",
        "/useradmin/",
        "/useradmin/index.php",
        "/useradmin/index.html",
        "/useradmin/login.php",
        "/useradmin/login.html",
        "/sysadmin/",
        "/sysadmin/index.php",
        "/sysadmin/index.html",
        "/sysadmin/login.php",
        "/sysadmin/login.html",
        "/systemadmin/",
        "/systemadmin/index.php",
        "/systemadmin/index.html",
        "/systemadmin/login.php",
        "/systemadmin/login.html",
        "/sysadmins/",
        "/sysadmins/index.php",
        "/sysadmins/index.html",
        "/sysadmins/login.php",
        "/sysadmins/login.html",
        "/administrators/",
        "/administrators/index.php",
        "/administrators/index.html",
        "/administrators/login.php",
        "/administrators/login.html",
        "/admins/",
        "/admins/index.php",
        "/admins/index.html",
        "/admins/login.php",
        "/admins/login.html",
        "/logins/",
        "/logins/index.php",
        "/logins/index.html",
        "/logins/login.php",
        "/logins/login.html",
        "/administration/",
        "/administration/index.php",
        "/administration/index.html",
        "/administration/login.php",
        "/administration/login.html",
        "/secureadmin/",
        "/secureadmin/index.php",
        "/secureadmin/index.html",
        "/secureadmin/login.php",
        "/secureadmin/login.html",
        "/siteadmin/",
        "/siteadmin/index.php",
        "/siteadmin/index.html",
        "/siteadmin/login.php",
        "/siteadmin/login.html",
    ]

    backup_paths = [
        "/backup/",
        "/backup.zip",
        "/backup.tar.gz",
        "/backup.sql",
        "/backup.bak",
        "/backup.old",
        "/backup.db",
        "/backup.txt",
        "/backup.rar",
        "/backup.7z",
        "/backup.tar",
        "/backup.tgz",
        "/backup.zip",
        "/backup.tar.gz",
        "/backup.sql",
        "/backup.bak",
        "/backup.old",
        "/backup.db",
        "/backup.txt",
        "/backup.rar",
        "/backup.7z",
        "/backup.tar",
        "/backup.tgz",
    ]

    server_paths = [
        "/cgi-bin/",
        "/cgi-bin/index.cgi",
        "/cgi-bin/php/",
        "/cgi-bin/php/index.php",
        "/cgi-bin/php5/",
        "/cgi-bin/php5/index.php",
        "/cgi-bin/php-cgi/",
        "/cgi-bin/php-cgi/index.php",
        "/cgi-bin/php7/",
        "/cgi-bin/php7/index.php",
        "/php/",
        "/php/index.php",
        "/php5/",
        "/php5/index.php",
        "/php-cgi/",
        "/php-cgi/index.php",
        "/php7/",
        "/php7/index.php",
        "/phpmyadmin/",
        "/phpmyadmin/index.php",
        "/phpmyadmin/index.html",
        "/phpmyadmin/login.php",
        "/phpmyadmin/login.html",
        "/pma/",
        "/pma/index.php",
        "/pma/index.html",
        "/pma/login.php",
        "/pma/login.html",
        "/adminer/",
        "/adminer/index.php",
        "/adminer/index.html",
        "/adminer/login.php",
        "/adminer/login.html",
        "/MyAdmin/",
        "/MyAdmin/index.php",
        "/MyAdmin/index.html",
        "/MyAdmin/login.php",
        "/MyAdmin/login.html",
        "/dbadmin/",
        "/dbadmin/index.php",
        "/dbadmin/index.html",
        "/dbadmin/login.php",
        "/dbadmin/login.html",
        "/oracle/",
        "/oracle/index.php",
        "/oracle/index.html",
        "/oracle/login.php",
        "/oracle/login.html",
        "/cpanel/",
        "/cpanel/index.php",
        "/cpanel/index.html",
        "/cpanel/login.php",
        "/cpanel/login.html",
        "/whm/",
        "/whm/index.php",
        "/whm/index.html",
        "/whm/login.php",
        "/whm/login.html",
        "/webmin/",
        "/webmin/index.php",
        "/webmin/index.html",
        "/webmin/login.php",
        "/webmin/login.html",
        "/directadmin/",
        "/directadmin/index.php",
        "/directadmin/index.html",
        "/directadmin/login.php",
        "/directadmin/login.html",
    ]

    if check_all:
        all_paths = set(common_paths + backup_paths + server_paths)
        for path in all_paths:
            full_url = base_url + path
            response = requests.get(full_url)
            status_code = response.status_code
            content_length = len(response.content)
            if filter_status_codes is None or status_code in filter_status_codes:
                output = f"{status_code} | {content_length} | {full_url}"
                print(output)
            if rate_limit:
                time.sleep(rate_limit)

    else:
        for path in common_paths:
            full_url = base_url + path
            response = requests.get(full_url)
            status_code = response.status_code
            content_length = len(response.content)
            if filter_status_codes is None or status_code in filter_status_codes:
                output = f"{status_code} | {content_length} | {full_url}"
                print(output)
            if rate_limit:
                time.sleep(rate_limit)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Website URL to test')
parser.add_argument('-f', '--filter', nargs='+', type=int, help='Filter by status codes')
parser.add_argument('-rl', '--rate-limit', type=float, help='Request rate limit (in seconds)')
parser.add_argument('-a', '--all', action='store_true', help='Check all paths (common, backup, and server default)')
args = parser.parse_args()

# Check if URL is provided
if args.url:
    url = args.url
else:
    url = input("Enter the website URL: ")

# Check if filter status codes are provided
filter_status_codes = args.filter if args.filter else None

# Check if rate limit is provided
rate_limit = args.rate_limit if args.rate_limit else None

# Check if check all paths option is enabled
check_all = args.all

check_default_pages(url, filter_status_codes, rate_limit, check_all)
