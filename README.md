# ansible-simple-user-password
Simple playbook to create user and assign password

To use it you must complete the variables listed in the site.yml file.


For the variable password, it can be encrypted with the Python script "encrypt_password.py"

### Example:

```
python encrypt_password.py yourSecretPassword

```

It will show the encrypted password

```
$1$ansible$nmBf8N/RR6O1GpdHI/1Qg1
```

## RUN PLAYBOOK

```
ansible-playbook site.yml -i hosts
```
