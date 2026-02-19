# 🔢 Calculadora Python

Uma calculadora completa desenvolvida em Python com interface de linha de comando e interface web usando Streamlit.

## 📋 Descrição do Projeto

Este projeto oferece duas formas de usar a calculadora:
- **calculadora.py**: Versão de linha de comando com menu interativo
- **calculadora_view.py**: Interface web moderna e amigável usando Streamlit

## 📁 Arquivos do Projeto

### calculadora.py

Arquivo principal da calculadora de linha de comando. Oferece um menu interativo onde o usuário pode escolher entre diversas operações matemáticas.

#### Operações Disponíveis:

1. **Adição (+)** - Soma dois números
2. **Subtração (-)** - Subtrai o segundo número do primeiro
3. **Multiplicação (×)** - Multiplica dois números
4. **Divisão (÷)** - Divide o primeiro número pelo segundo (com validação de divisão por zero)
5. **Potenciação (^)** - Eleva a base ao expoente
6. **Radiciação - Raiz Quadrada (√)** - Calcula a raiz quadrada de um número positivo
7. **Raiz Cúbica (∛)** - Calcula a raiz cúbica de um número
8. **Raiz N-ésima (ⁿ√)** - Calcula a raiz de qualquer índice
9. **Módulo/Resto da Divisão (%)** - Retorna o resto da divisão entre dois números
10. **Logaritmo Natural (ln)** - Calcula o logaritmo natural (base e)
11. **Logaritmo na Base 10 (log)** - Calcula o logaritmo na base 10
12. **Seno (sin)** - Calcula o seno de um ângulo em radianos
13. **Cosseno (cos)** - Calcula o cosseno de um ângulo em radianos
14. **Tangente (tan)** - Calcula a tangente de um ângulo em radianos
15. **Fatorial (!)** - Calcula o fatorial de um número inteiro não negativo

#### Como Executar:

```bash
python3 calculadora.py
```

O programa exibirá um menu interativo onde você pode escolher a operação desejada, inserir os valores e obter o resultado.

### calculadora_view.py

Interface web moderna e amigável desenvolvida com Streamlit. Oferece uma experiência visual agradável com cores pastéis e design responsivo.

#### Características:

- **Interface Visual**: Design moderno com cores pastéis (azul, rosa, verde)
- **Layout Responsivo**: Interface adaptável com colunas e containers
- **Validação de Erros**: Tratamento adequado de erros (divisão por zero, números negativos, etc.)
- **Todas as Operações**: Inclui todas as 15 operações disponíveis na versão CLI
- **Resultados Destacados**: Exibição clara e destacada dos resultados
- **Navegação Lateral**: Menu lateral para fácil seleção de operações

#### Operações Disponíveis:

As mesmas 15 operações da versão CLI, organizadas em uma interface gráfica intuitiva:
- ➕ Adição
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- 🔺 Potenciação
- √ Raiz Quadrada
- ∛ Raiz Cúbica
- ⁿ√ Raiz N-ésima
- 📊 Módulo
- 📈 Logaritmo Natural
- 📉 Logaritmo Base 10
- 📐 Seno
- 📐 Cosseno
- 📐 Tangente
- ❗ Fatorial

#### Como Executar:

```bash
streamlit run calculadora_view.py
```

A aplicação abrirá automaticamente no navegador padrão.

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Criar Ambiente Virtual

É recomendado usar um ambiente virtual para isolar as dependências do projeto:

```bash
# 1. Criar o ambiente virtual
python3 -m venv venv

# 2. Ativar o ambiente virtual
source venv/bin/activate

# 3. Atualizar o pip (recomendado)
pip install --upgrade pip

# 4. Instalar as dependências do requirements.txt
pip install -r requirements.txt
```

### Desativar Ambiente Virtual

Quando terminar de usar o projeto, você pode desativar o ambiente virtual:

```bash
deactivate
```

## 📦 Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

- `streamlit>=1.28.0` - Framework para criação da interface web

## 🎯 Uso

### Versão CLI (calculadora.py)

1. Execute o arquivo:
   ```bash
   python3 calculadora.py
   ```

2. Escolha uma operação do menu (0-15)
3. Insira os valores solicitados
4. Visualize o resultado
5. Pressione Enter para continuar ou escolha 0 para sair

### Versão Web (calculadora_view.py)

1. Execute com Streamlit:
   ```bash
   streamlit run calculadora_view.py
   ```

2. A interface abrirá automaticamente no navegador
3. Selecione a operação desejada no menu lateral
4. Insira os valores nos campos
5. Clique em "Calcular" para ver o resultado

## 📝 Notas

- Para operações trigonométricas (seno, cosseno, tangente), os ângulos devem ser inseridos em **radianos**
- Para converter graus em radianos: `radianos = graus × π / 180`
- O fatorial está limitado a números até 170 devido a limitações computacionais
- A raiz quadrada requer números não negativos

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

---

Desenvolvido com ❤️ usando Python e Streamlit
