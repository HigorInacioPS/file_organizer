# 📚 Análise de Reviews de Livros da Amazon

Este projeto é uma aplicação web interativa desenvolvida com **Streamlit**, com o objetivo de visualizar, explorar e analisar **avaliações de livros da Amazon**. 

Foi desenvolvido durante o curso da **Asimov Academy** e utiliza gráficos e filtros dinâmicos para facilitar a interpretação dos dados.

---

## 🧠 Objetivo

A aplicação apresenta análises detalhadas de reviews e dados de livros em duas abas principais, oferecendo:

- Filtro por **faixa de preço** com slider lateral.
- Visualização de **gráficos interativos** (histogramas e barras) com `plotly`.
- Exibição de **tabelas e métricas** com base nos livros selecionados.
- Interface clean e funcional desenvolvida com Streamlit.

---

## 📂 Estrutura do Projeto

- `app.py` – Script com carregamento de dados e exibição de gráficos.
- `1_book_reviews.py` – Página com informações detalhadas por livro e chat com reviews.
- `project.py` – Versão combinada com filtros, gráficos e exibição de dados.
- `customer_reviews.csv` – Base de dados com avaliações de clientes.
- `top_100_trending_books.csv` – Lista com os 100 livros mais populares no período analisado.

---

## 🛠️ Bibliotecas Utilizadas

| Biblioteca     | Finalidade                                 |
|----------------|---------------------------------------------|
| `pandas`       | Manipulação e leitura de dados tabulares    |
| `streamlit`    | Criação da aplicação web interativa         |
| `plotly.express` | Visualizações interativas e responsivas |

> ✅ Recomendação: utilizar **Python 3.12.3** para garantir a compatibilidade com todas as bibliotecas.

---

## 🚀 Como Executar Localmente

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o app com Streamlit:
```bash
streamlit run app.py
```

> 🧪 Você também pode executar os outros arquivos (`project.py` ou `1_book_reviews.py`) individualmente com o mesmo comando `streamlit run`.

---

## ✍️ Observações

- As informações são fictícias e utilizadas para fins educacionais.
- As abas e gráficos foram desenvolvidos com foco em responsividade e boa experiência visual.
- Os dados são fornecidos em CSV e processados localmente pelo app.

---

## 🎓 Créditos

Projeto desenvolvido durante o curso da **Asimov Academy**.