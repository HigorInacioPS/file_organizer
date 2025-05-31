# 🗂️ Organizador de Arquivos - Projeto 02

Este é um projeto de automação simples que organiza arquivos automaticamente em pastas específicas com base em suas extensões. Ele foi desenvolvido como parte de um plano educacional voltado ao aprendizado da linguagem Python.

## 📌 Objetivo

Automatizar a organização de arquivos dentro de uma pasta do sistema, separando-os por categorias como: Imagens, Documentos, Planilhas, Vídeos, Áudios, etc.

---

## ⚙️ Funcionamento

O script varre uma pasta específica (neste caso, a subpasta `data`) e move os arquivos presentes para subpastas organizadas conforme o tipo de extensão. Se a extensão não pertencer a nenhuma das categorias predefinidas, o arquivo será movido para uma pasta chamada `Outros`.

As categorias utilizadas nesta versão inicial são:

- Imagens
- Documentos
- Planilhas
- Apresentações
- Áudios
- Vídeos
- Compactados
- Executáveis
- Outros

---

## 📚 Bibliotecas Utilizadas

- `os`: Utilizada para interagir com o sistema de arquivos, como listar diretórios, verificar se um caminho é um arquivo, e manipular caminhos.
- `shutil`: Utilizada para mover os arquivos entre pastas.

Essas bibliotecas são **nativas do Python** e não exigem instalação externa.

---

## 🧪 Versão Atual

Este é o **protótipo funcional inicial** do organizador. Ele já realiza com sucesso a organização de arquivos em categorias automaticamente, **sem necessidade de interação com o usuário**.

### ✅ Características da versão atual:

- Totalmente funcional para testes locais
- Caminho relativo configurado para a subpasta `data`
- Pastas de destino são criadas automaticamente
- Arquivos são movidos de forma segura para suas categorias

---

## 🚧 Próximas Etapas (Planejamento)

Este projeto será atualizado futuramente por meio de **commits contínuos**. As próximas melhorias previstas incluem:

- Interface de terminal com interação com o usuário
- Seleção ativa do caminho a ser organizado
- Geração de relatórios de organização (resumo por categoria)
- Interface gráfica (Streamlit ou Tkinter)

---

## 👨‍💻 Autor

Este projeto foi desenvolvido por **Higor Inácio P. Sousa**.

---

## 🎓 Contexto Educacional

Este é o **segundo projeto de um total de 20** que compõem uma trilha prática de desenvolvimento em Python, com duração prevista de **sete meses de estudos intensivos**.

Cada projeto visa consolidar os conhecimentos adquiridos por meio da prática e será versionado e publicado aqui no GitHub ao longo do processo.

OBS: o usuário pode adicionar arquivos à pasta raiz 'data' caso queira testar com mais arquivos.
---

## 📁 Estrutura do Projeto

```text
S2_Organizador_de_Arquivos/
├── organizador.py        ← Script principal
└── data/                 ← Pasta contendo os arquivos a serem organizados
