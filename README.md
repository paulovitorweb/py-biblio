# py-biblio

Uma aplicação escrita em Python com dataclasses para gerenciar referências bibliográficas.

## Build

### Requisitos

- Python >= 3.8

### Crie um ambiente virtual e ative

```
python3 -m venv venv
source venv/bin/activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Suba a API

```
make dev
```

Ou, sem Makefile:

```
uvicorn src.pybiblio.api.main:app --reload
```

### Documentação

- Com Swagger: http://127.0.0.1:8000/docs
- Com ReDoc: http://127.0.0.1:8000/redoc

### Teste

Um conjunto de testes pode ser encontrado em `/tests`. Para executá-los, instale também as dependências de desenvolvimento:

```
pip install -r dev-requirements.txt
```

E, em seguida, execute:

```
pytest
```
