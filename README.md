# Upload file to Mega.nz
## Step 1: Account
You must need an `Mega` account. If you don't have one go to (https://mega.nz/register)

## Step 2: Pip
You need to install a `Python` package through `pip` by using following command:
```
pip install mega.py
```
## Step 3: Usage
It's time to make an magic from a small file by using command line:
```
python3 test.py -e "<your email>" -p "<your password>" -d "<folder path>" -f "<file path>"
```
- *-e* : your login email, eq: `xxxx@gmail.com`. (Required)
- *-p* : your login password, eq: `123456789`. (Required)
- *-d* : your folder's path on your Mega, eq: `folder1`. (optional)
- *-f* : your file path in your local, eq: `backup/file.txt`. (Required)
