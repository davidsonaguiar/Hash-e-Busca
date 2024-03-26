# Miniprojeto - Aplicações de Hashing e Busca 

## Objetivo:
Aplicar o conhecimento sobre a estrutura de dados "Hashing", bem como sobre as técnicas de busca sequencial e binária em uma aplicação com cadastro de pessoas. 

## Critérios de Avaliação:

1. Executar sem erros 
2. Utilizar implementação do TAD Map (Hashing) 
3. Realizar a especificação solicitada 
4. Indicar qualquer material consultado (codigo, livro, site, etc.) para realização  do trabalho 
 
## Descrição 

Este projeto tem como objetivo avaliar o desempenho de algoritmos e estruturas de dados para inserir dados e realizar buscas de registros no contexto do cadastro nacional de pessoas. O cadastro é composto pelos seguintes campos: CPF (identificador único), nome, telefone e senha. 

**Deve-se desenvolver três estruturas de dados que permitam inserir e pesquisar dados utilizando as seguintes técnicas:**

- Hashing: Utiliza uma tabela hash para armazenar os registros de pessoas, onde o CPF é utilizado como chave de busca. 
- Busca Binária: Os registros são armazenados em uma lista ordenados pelo CPF e utiliza a busca binária para pesquisar os registros. 
- Busca Sequencial: Os registros são armazenados em uma lista não ordenada e a busca é realizada de forma sequencial. 

Para avaliar o desempenho de cada estrutura de dados e dos algoritmos relacionados, realizem testes de inserção e pesquisa com conjuntos de dados de tamanhos variados: 10.000, 100.000 e 1.000.000 de elementos. Em cada teste, registre o tempo médio para inserção e buscar registros. 

## Atividade 

Para executar o projeto sugere-se seguir as seguintes atividades: 

1. **Implementação das Estruturas de Dados:**

- Desenvolva as três estruturas de dados de acordo com as especificações fornecidas. 

- Garanta que as estruturas de dados sejam capazes de inserir registros, buscar registros por CPF e garantir a unicidade do CPF. 

2. **Implementação dos Testes de Desempenho:** 

- Crie funções para gerar CPFs aleatórios e dados de pessoas para inserção nos conjuntos de dados. 

- Implemente testes de inserção para medir o tempo necessário para inserir os registros em cada estrutura de dados. 

- Implemente testes de pesquisa para medir o tempo médio necessário para buscar registros por CPF em cada estrutura de dados. 

3. **Execução dos Testes:**

- Realize os testes com os conjuntos de dados de diferentes tamanhos (10.000, 100.000 e 1.000.000 de elementos). 

- Registre os tempos de inserção e pesquisa para cada estrutura de dados e conjunto de dados. 

4. **Análise de Resultados:**

- Compare os resultados dos testes para cada estrutura de dados e conjunto de dados. 

- Identifique padrões de desempenho e analise como cada estrutura se comporta em diferentes cenários. 

- Interprete os resultados em relação aos objetivos do projeto e aos critérios de avaliação estabelecidos. 

5. **Documentação e Apresentação:** 

- Documente os resultados obtidos, incluindo gráficos e tabelas comparativas. 

- Crie um relatório final descrevendo o projeto, as atividades realizadas, os resultados obtidos e as conclusões alcançadas. 

- Acrescente no relatório uma discussão sobre a seguinte questão: quais considerações devem ser levadas em conta ao decidir por utilizar a busca sequencial, busca binária e hashing nesse projeto. 