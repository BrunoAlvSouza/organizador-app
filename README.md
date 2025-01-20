### ReadMe.md

# Organizador de Arquivos

Este software é um organizador de arquivos que permite organizar documentos, imagens, áudios, vídeos e outros tipos de arquivos automaticamente em pastas baseadas em suas extensões. Ele também pode remover pastas vazias do diretório de origem.

---

## Funcionalidades

- **Organizar Arquivos**: Move arquivos de uma pasta de origem para uma pasta de destino específica, separando-os por extensão.
- **Renomeação Automática**: Evita conflitos de nomes, adicionando um sufixo incremental quando arquivos com o mesmo nome já existem na pasta de destino.
- **Configuração Personalizada**: Permite selecionar as extensões de arquivos a serem organizados.
- **Apagar Pastas Vazias**: Remove automaticamente pastas vazias na pasta de origem após a organização.
- **Salvar Configurações**: Armazena a pasta de destino para uso em futuras execuções.

---

## Como Usar

### Pré-requisitos

- **Python**: Certifique-se de ter o Python instalado (3.x recomendado).
- **Bibliotecas**: O software usa apenas bibliotecas padrão do Python, então não é necessário instalar pacotes adicionais.

### Passos para Executar

1. **Baixe o Arquivo**: Faça o download do código-fonte.
2. **Execute o Script**: Execute o arquivo Python no terminal ou clique duas vezes no script para abrir a interface gráfica.
   ```bash
   python organizador_arquivos.py
   ```
3. **Selecione a Pasta de Origem**:
   - Clique em "Selecionar" ao lado do campo "Pasta de origem".
   - Escolha a pasta onde os arquivos estão localizados.
4. **Defina a Pasta de Destino**:
   - Informe a pasta onde os arquivos organizados serão armazenados no campo "Pasta fixa para organização".
   - Esta configuração será salva automaticamente para futuras execuções.
5. **Escolha as Extensões**:
   - Marque as extensões que deseja organizar no painel de extensões.
   - Clique em "Selecionar Todas as Extensões" para marcar todas as opções de uma vez.
6. **Organize os Arquivos**:
   - Clique em "Organizar" para iniciar a organização.
   - Uma mensagem de sucesso será exibida ao final do processo.
7. **Remova Pastas Vazias (Opcional)**:
   - Clique no botão "Apagar Pastas Vazias" para remover automaticamente pastas vazias do diretório de origem.

---

## Estrutura de Arquivos

- **config.txt**: Salva a pasta de destino selecionada pelo usuário.
- **Interface Gráfica**: Desenvolvida em Tkinter, permitindo interação intuitiva para organizar arquivos.

---

## Extensões Suportadas

O software suporta uma ampla variedade de extensões, incluindo:

- Documentos: `.txt`, `.pdf`, `.docx`, `.odt`, `.xlsx`, `.csv`
- Imagens: `.jpg`, `.jpeg`, `.png`, `.webp`, `.psd`
- Vídeos e Áudio: `.mp4`, `.mp3`, `.m4a`
- Arquivos Compactados: `.zip`, `.rar`, `.tar`

---

## Observações

- Certifique-se de ter permissão de leitura e escrita nas pastas de origem e destino.
- O programa não processará arquivos sem a extensão especificada.

---

## Licença

Este software é de uso livre. Modifique e utilize conforme sua necessidade, dando os devidos créditos ao autor original.

---

## Suporte

Caso encontre problemas ou tenha dúvidas, sinta-se à vontade para entrar em contato por meio de bruno.alv.souza@outlook.com.
