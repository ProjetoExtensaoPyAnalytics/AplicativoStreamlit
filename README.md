## Deploy no Streamlit Cloud

A aplicação foi implementada no **Streamlit Cloud** para facilitar o acesso via web. Este guia descreve os passos para realizar o deploy e resolver problemas comuns.

### Passos para o Deploy

1. **Criação do Repositório:**
   - Certifique-se de que todos os arquivos do projeto estão no repositório do GitHub, incluindo:
     - O script principal (por exemplo, `app.py`).
     - O arquivo de dependências (`requirements.txt`).
     - Os datasets necessários (ou links para download se forem muito grandes).

2. **Configuração no Streamlit Cloud:**
   - Acesse o [Streamlit Cloud](https://streamlit.io/cloud).
   - Clique em **Deploy an app** e conecte sua conta do GitHub.
   - Escolha o repositório e o branch desejado.
   - No campo `Main file path`, insira o caminho correto para o script principal (exemplo: `app.py`).
   - Clique em **Deploy**.

3. **Gerenciamento de Arquivos:**
   - Se a aplicação utiliza datasets, garanta que:
     - Eles estejam no mesmo diretório que o script principal **OU**
     - Seus caminhos estejam corretamente definidos no código.
   - Para arquivos grandes, considere o uso de links ou sistemas de armazenamento como AWS S3 ou Google Drive.

### Erros Comuns e Como Resolver

#### 1. **Erro de Caminho para Datasets**
   - **Descrição:** O Streamlit Cloud não consegue encontrar os arquivos devido a caminhos relativos mal configurados.
   - **Solução:**
     - Use caminhos relativos baseados no diretório do script principal.
     - Exemplo de correção:
       ```python
       import os
       file_path = os.path.join(os.path.dirname(__file__), 'data/dataset.csv')
       df = pd.read_csv(file_path)
       ```

#### 2. **Erro no Arquivo `requirements.txt`**
   - **Descrição:** O deploy falha devido a dependências ausentes ou versões incompatíveis.
   - **Solução:**
     - Verifique se todas as bibliotecas utilizadas no código estão listadas no `requirements.txt`.
     - Gere automaticamente o arquivo com:
       ```bash
       pip freeze > requirements.txt
       ```
     - Para versões específicas, defina manualmente (exemplo: `pandas==1.5.3`).

#### 3. **Erros no Cache do Streamlit**
   - **Descrição:** Alterações recentes no código ou datasets não aparecem no deploy.
   - **Solução:**
     - Acesse o painel do Streamlit Cloud e clique em **Manage app**.
     - Selecione **Clear cache** e reinicie a aplicação.

