API para Transcrição de Áudio usando modelos OpenAI Whisper.

Observação: Caso a API seja executada em ambiente Windows, se faz necessário instalar o ffmpeg: 
https://ffmpeg.org/download.html#build-windows

Windows:

Vá para o site oficial do FFmpeg: https://ffmpeg.org/download.html
Baixe a versão mais recente para Windows (geralmente um arquivo .zip).
Extraia o conteúdo do arquivo .zip para uma pasta no seu computador (por exemplo, C:\ffmpeg).
Adicionar ao PATH: É crucial adicionar o diretório bin dentro da pasta do FFmpeg às variáveis de ambiente do seu sistema. Isso permite que o sistema encontre o executável ffmpeg de qualquer lugar no terminal.
Pesquise por "variáveis de ambiente" no menu Iniciar.
Clique em "Editar as variáveis de ambiente do sistema".
Na janela "Propriedades do Sistema", clique no botão "Variáveis de Ambiente...".
Na seção "Variáveis do1 Usuário" ou "Variáveis do Sistema", encontre a variável chamada Path e selecione-a.   
Clique no botão "Editar...".
Clique em "Novo" e adicione o caminho completo para o diretório bin do FFmpeg (por exemplo, C:\ffmpeg\bin).
Clique em "OK" em todas as janelas para salvar as alterações.
Reinicie o Terminal/Prompt de Comando: Feche e abra novamente qualquer terminal ou prompt de comando que você estiver usando para executar a API, para que as alterações no PATH sejam aplicadas.
