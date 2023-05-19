# Automação de Coleta de Informações com Nmap e Aquatone

## Descrição Geral
Este repositório contém um script Python que automatiza a coleta de informações de um site usando as ferramentas Nmap e Aquatone. O objetivo é facilitar o processo de execução dessas ferramentas e organizar os resultados em uma estrutura de pasta adequada. É necessário ter o Nmap e o Aquatone instalados no sistema operacional Linux para utilizar este script.

## Instalação das Dependências
Certifique-se de ter o Nmap e o Aquatone instalados no seu sistema operacional Linux. Para instalar o Nmap, visite o site oficial em https://nmap.org e siga as instruções de instalação fornecidas. Para instalar o Aquatone, acesse https://github.com/michenriksen/aquatone e siga as instruções fornecidas no repositório.

## Funcionalidades
O script permite especificar um site-alvo e uma flag para o comando Nmap. Ele executa o Nmap com a flag fornecida, salvando os resultados em formato XML. Em seguida, os resultados XML são fornecidos ao Aquatone para a geração de um relatório HTML detalhado.

O script cria automaticamente uma pasta com o nome do site-alvo e move o relatório Aquatone para essa pasta. Além disso, ele pode mover todos os arquivos e pastas (exceto o próprio script) para a pasta do site, a fim de manter uma estrutura organizada.

## Uso
1. Certifique-se de ter o Nmap e o Aquatone instalados no seu sistema operacional Linux.
2. Clone este repositório: git clone https://github.com/seu-usuario/nmap-aquatone-automation.git
3. Acesse o diretório do projeto: cd nmap-aquatone-automation
4. Execute o script, fornecendo o site-alvo e a flag do Nmap como argumentos:
* Exemplo: 
```python script.py --site example.com --flag -sV```
5. Substitua "example.com" pelo site que deseja pesquisar e "-sV" pela flag desejada.
6. O script executará o Nmap e o Aquatone, gerando o relatório Aquatone na pasta do site-alvo.
7. Todos os arquivos e pastas (exceto o script) serão movidos para a pasta do site para organização.
