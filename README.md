# mcd

proyecto para Mac de proyectos de enviar emails masivops

## clone repo
clone use git
```
git clone git@github.com:Yursksf1/mcd.git
```

## create and active virtualenv
### windows
```
virtualenv test
source venv/bin/activate
.\test\Scripts\activate
```

### mac or linux
```
virtualenv -p python3 venv
source venv/bin/activate
```

### to deactivate use
```
deactivate
```

## install requirements
install use pip
```
pip install -r requirements.txt
```


### Credential
update data in local_data.py
```
information = {
    'username': 'my_email@mail.com',
    'password': 'super_secure_password'
}

datas = [[]]

text = "Hi!\n{name}\nHere is the link you wanted:\n{url}"

html = '''
<h1> Hello! </h1>
'''
...
```


### Run File 
```
python run_all.py
```