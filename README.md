# Simular HTTPS

#### Requisitos
- Python 3.7+


#### Instalação (Linux e macOS)
```sh
$ pip install -r requirements.txt
```

Ou utilizando [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```sh
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

#### Execução

**Geração da chave**

```sh
$ python3 gen_key.py
``` 

**Descriptografar mensagem a partir da chave e criptografar invertida**


```sh
$ python3 crypt.py dbe7faf1ab231dacd141938bae0143d8 5D127C2131EB42E7DF9C553C070B0D9B428027BFA53CF1D56ABC8C60F241455E1EC2BA506FB81410252953C600AE192F0EB04AAE4BFEBF123FA5EC962A625A46B0DC5AFB1933DCE5FDB4CEDB258237CFB2719315EE8152C300F9C4F85B2E2AA3
``` 