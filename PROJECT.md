```json
desafio-itau-backend-em-python/
├── api/                      # Camada de entrada (HTTP)
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── transacao.py
│   │   │   └── estatistica.py
│   │   └── schemas/
│   │       ├── transacao.py
│   │       └── estatistica.py
│   └── deps.py
├── core/                     # Configurações e inicialização
│   ├── config.py
│   ├── logger.py
│   └── settings.py
├── domain/                   # Lógica de negócio e entidades puras
│   ├── models/
│   │   └── transacao.py
│   └── services/
│       └── estatistica_service.py
├── infrastructure/           # Implementações concretas (armazenamento em memória)
│   └── repositories/
│       └── transacao_mem_repo.py
├── main.py                   # Entry point
├── tests/
│   ├── unit/
│   └── integration/
└── README.md

```
