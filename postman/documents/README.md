# 🚀 Postman - Taskify API Demos

Bem-vindo à pasta de testes e documentação do projeto **Taskify**. Este diretório contém as coleções e ambientes do Postman para que você possa testar, validar e consumir nossa API rapidamente.

---

## 📂 Estrutura de Pastas

* **`collections/`**: Contém as coleções de requisições de referência (endpoints de backend estruturados por recursos).
* **`environments/`**: Contém as variáveis de ambiente (como a URL base) configuradas para os contextos de desenvolvimento.

---

## ⭐️ Melhores Práticas

* 🔐 **Segurança de Credenciais:** Certifique-se de que nenhuma chave de API ou token seja exposto ao commitar alterações. Sempre use as **variáveis de ambiente** locais do Postman no campo *Current Value* para autenticação.
* 🚫 **Dados Sensíveis:** Ao exportar ambientes para atualizar esta pasta, certifique-se de limpar os campos de chaves privadas ou senhas do repositório público/compartilhado.

---

## 🛠️ Como Começar

1. Abra o seu aplicativo do **Postman**.
2. Clique no botão **Import** no topo esquerdo.
3. Arraste e solte os arquivos `.json` localizados em `postman/collections/` e `postman/environments/`.
4. Selecione o ambiente **Taskify** no seletor do canto superior direito para apontar as requisições para `http://localhost:8000`.
