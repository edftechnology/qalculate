#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar/usar o `qalculate` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar/usar o `qalculate` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to install/configure/use the `qalculate` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `qalculate`
# 
# O `qalculate` é uma calculadora avançada e multifuncional para sistemas `Linux`, projetada para oferecer uma ampla gama de operações matemáticas e científicas. Com uma _interface_ gráfica intuitiva, o `qalculate` suporta cálculos básicos, funções matemáticas complexas, e operações simbólicas. Ele é útil tanto para usuários casuais que precisam de uma calculadora poderosa quanto para profissionais que requerem ferramentas de cálculo mais especializadas. O _software_ inclui suporte para expressões matemáticas, variáveis, e unidades de medida, tornando-o uma ferramenta versátil e robusta para diversas necessidades de cálculo.
# 

# ## 1. Configurar/Instalar/Usar o `qalculate` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `qalculate` no `Linux Ubuntu`, você pode usar o gerenciador de pacotes apt. Siga os passos abaixo:
# 
# 1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para instalar o `Qalculate` no `Linux Ubuntu` pelo `Terminal Emulator`, você pode seguir os passos abaixo. O `Qalculate` é uma calculadora avançada que suporta diversas funcionalidades matemáticas, como álgebra simbólica, conversões e unidades.
# 
# 1. **Instale o `Qalculate`**: O `Qalculate` está disponível no repositório oficial do `Linux Ubuntu`, então você pode instalá-lo diretamente com o `apt`.
# 
# 2. Para instalar a _interface_ gráfica e o pacote de linha de comando, use o comando:
# 
#     ```bash
#     sudo apt install qalculate-gtk -y
#     ```
# 
#     Isso instalará a versão gráfica do `Qalculate`.
# 
# 3. **Inicie o `Qalculate`**: Após a instalação, você pode iniciar o `Qalculate` pela linha de comando ou pelo _menu_ de aplicativos:
# 
#     3.1 **No `Terminal Emulator`**:
#     
#     ```bash
#     qalculate-gtk
#     ```
# 
#     3.2 Ou pesquise por `"Qalculate"` no seu _menu_ de aplicativos.
# 
# 4. **Verificar a instalação**: Para garantir que o `Qalculate` foi instalado corretamente, você pode verificar a versão instalada com o seguinte comando: 
# 
#     ```bash
#     qalculate --version
#     ```
# 
# Com isso, o `Qalculate` estará instalado e pronto para uso no seu `Linux Ubuntu`.

# ## 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `qalculate` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```bash
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove
#     sudo apt update -y
#     sudo apt autoremove
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install qalculate-gtk -y
#     qalculate --version
#     ```

# ## 2. Alterar a tecla de atalho para o `qalculate-gtk`
# 
# Se você está usando o ambiente de _desktop_ `XFCE`, aqui está o passo a passo para alterar o atalho de teclado do `mate-calc` para o `qalculate-gtk`, tanto pela _interface_ gráfica quanto pelo `Terminal Emulator`:
# 
# ### 2.1 Alterar o atalho de teclado no `XFCE` pela Interface Gráfica
# 
# 1. **Abra o Gerenciador de Configurações do `XFCE`**:
# 
#     - No _menu_ de aplicativos, vá até `Keyboards`.
# 
#     - Ou, pressione `Alt + F2`, digite `xfce4-settings-manager` e pressione `Enter` para abrir as configurações.
# 
# 2. **Acesse a aba `"Application Shortcuts"`**: No gerenciador de configurações do teclado, vá até a aba `Application Shortcuts`.
# 
# 3. **Adicione um novo atalho para o `qalculate-gtk`**:
#     
#     - Clique no botão `+Add`.
# 
#     - No campo de Comando, digite `qalculate-gtk` e clique em `OK`.
# 
# 4. **Defina a combinação de teclas**: Após adicionar o comando, será solicitado que você pressione a combinação de teclas para o novo atalho. Escolha a combinação de teclas que deseja, como:
# 
#     ```bash
#     Ctrl + Alt + C
#     ```
# 
# 5. **Remova o atalho para o `mate-calc` (se estiver configurado)**: Se existir um atalho para `mate-calc`, encontre-o na lista e clique em `Remover`.
# 
# Agora o `qalculate-gtk` será iniciado com o atalho de teclado que você configurou.
# 

# ### 4.2 Alterar o atalho de teclado no `XFCE` pelo `Terminal Emulator`
# 
# 1. **Verifique os atalhos existentes**: Use o seguinte comando para listar os atalhos existentes no `XFCE`:
# 
#     ```bash
#     xfconf-query -c xfce4-keyboard-shortcuts -lv
#     ```
# 
#     Isso exibirá uma lista com os atalhos de teclado atualmente configurados.
# 
# 2. **Adicione o atalho para o `qalculate-gtk`**: Para adicionar um novo atalho para o `qalculate-gtk`, use o seguinte comando:
# 
#     ```bash
#     xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Primary><Alt>C" -s "qalculate-gtk"
#     ```
# 
#     Esse comando define `Ctrl + Alt + C` como o atalho para abrir o `qalculate-gtk`. Se você quiser usar outra combinação de teclas, ajuste a parte "<Primary><Alt>C" para a combinação que preferir.
# 
# 3. **Remova o atalho para o `mate-calc` (se estiver configurado)**: Para remover um atalho existente para o `mate-calc`, use o comando abaixo: 
# 
#     ```bash
#     xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Primary><Alt>C" -r
#     ```
# 
#     Isso remove o atalho para a combinação de teclas que estava previamente configurada para o `mate-calc`.
# 

# ### 4.3 Verifique se o atalho foi configurado corretamente
# 
# Após realizar as alterações, você pode testar o atalho para garantir que o `qalculate-gtk` está sendo iniciado corretamente.

# ## Referências
# 
# [1] OPENAI. ***Instalar o `qalculate` no `linux ubuntu` pelo `terminal emulator`.*** Disponível em: <https://chatgpt.com/c/f1c79929-aa4d-4a3b-aac7-cc3e0936e8e3> (texto adaptado). ChatGPT. Acessado em: 03/09/2024 14:23.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 03/09/2024 14:23.
# 
