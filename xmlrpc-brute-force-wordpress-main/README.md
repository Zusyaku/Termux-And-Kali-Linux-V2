# Xmlrpc Brute Force
![Logo](images/Screenshot_2020-10-15-02-18-11-179_com.termux.png)
![Contoh](images/IMG_20201015_022023.jpg)

## Usage
Single user
```
php xmlrpc.php -t|--target https://site.go.id -u|--username user -p|--password password.txt
```

Multi user
```
php xmlrpc.php -t|--target https://site.go.id -u|--username user1:user2:user3 -p|--password password.txt
```

## Note
If you want to use the timeout during the request, please enter the ```-o|--timeout``` parameter and the value is in seconds.
