# CNAB Reader
<p>Aplicação com objetivo de interpretar arquivos .txt com informações financeiras (CNAB)!</p>

## Instruções para rodar localmente

### Requisito:

<ul>
    <li>Python</li>
</ul>

### Clone este repositório 

```
git clone git@github.com:Kenzie-Academy-Brasil-Developers/m6-s2-renatosuzuki.git
```

### Crie o ambiente virtual em seu terminal

```
python -m venv venv
```

### Inicie o ambiente virtual

#### Windows

###### Abra o PowerShell

```
.\venv\Scripts\activate
```

#### Linux

```
source venv/bin/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Execute as migrações

```
python manage.py migrate
```

### Inicie o servidor

```
python manage.py runserver
```