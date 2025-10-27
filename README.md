# 🏥 Sistema de Triagem Manchester

Este projeto implementa uma **simulação do protocolo de triagem Manchester** em Python, utilizado em emergências médicas para classificar pacientes de acordo com a gravidade de seus sintomas.  

O sistema organiza os pacientes em **filas de prioridade** (Vermelha, Laranja, Amarela, Verde e Azul) e realiza o gerenciamento das filas — cadastrando, chamando e listando pacientes.

---

## 📋 Funcionalidades

- Perguntas sequenciais de triagem baseadas no **Protocolo de Manchester**.  
- Classificação automática do paciente em uma das **cinco categorias de prioridade**:  
  - 🔴 **Vermelha** – Emergência  
  - 🟠 **Laranja** – Muito urgente  
  - 🟡 **Amarela** – Urgente  
  - 🟢 **Verde** – Pouco urgente  
  - 🔵 **Azul** – Não urgente  
- Sistema de **filas encadeadas** para armazenar e chamar pacientes.  
- Menu interativo no terminal.

---

## ⚙️ Estrutura do Projeto

```
├── Simulador_Protocolo_Manchester.py   # Código principal do sistema
└── README.md               # Este arquivo
```

O sistema é composto por quatro principais classes:

- **NodeArvore** – Representa os nós da árvore de decisão do protocolo.  
- **Protocolo** – Responsável por realizar as perguntas e determinar a prioridade.  
- **Fila/Node** – Implementa a estrutura de filas encadeadas.  
- **GerenciadorFila** – Centraliza e gerencia todas as filas por prioridade.

---

## 💻 Exemplo de Uso

Ao executar o programa, o menu principal será exibido:

```
=== SISTEMA DE TRIAGEM MANCHESTER ===
1 - Cadastrar paciente
2 - Chamar paciente
3 - Mostrar status das filas
0 - Sair
```

### 🔹 1 - Cadastrar paciente
O sistema faz perguntas baseadas no protocolo e classifica o paciente automaticamente.

```
Qual o nome do paciente? João
O paciente está inconsciente ou não responde a estímulos? (s/n) n
Está com falta de ar moderada a grave (s/n)? s
```

> 🟠 Resultado: Paciente João classificado como **Muito Urgente (Laranja)**.

---

### 🔹 2 - Chamar paciente
Chama o próximo paciente da **fila de maior prioridade** disponível.

```
Chamando paciente da fila Vermelha - Emergência: Maria
```

---

### 🔹 3 - Mostrar status das filas
Lista todos os pacientes e suas posições em cada fila:

```
FILA: Vermelha - Emergência
Posição 1: João

FILA: Laranja - Muito Urgente
Não há ninguém esperando!
==========
```

---

## 🧠 Conceitos Envolvidos

- Estruturas de dados dinâmicas (listas encadeadas e árvores binárias)
- Controle de fluxo com condicionais
- Entrada e saída interativa no terminal
- Simulação de processos de triagem médica

---

## 📄 Licença

Este projeto é de código aberto sob a licença MIT.  
Sinta-se livre para estudar, modificar e aprimorar o sistema.

---

## 👨‍⚕️ Autor

**Mateus Grandel**  
💡 Projeto desenvolvido para fins educacionais, demonstrando lógica e estruturas de dados aplicadas à simulação de um sistema real.
