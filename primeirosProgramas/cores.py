# MUDANDO CORES NO TERMINAL
"""
CÓDIGO DE INÍCIO = \033[m
entre o colchete e o "m" há a especificação de 3 tipos: estilo, texto e fundo
***tipos e referências para o estilo:
-> 0 (normal)
-> 1 (negrito)
-> 4 (sublinhado)
-> 7 (negativo - inverte as cores do texto e do fundo)
***tipos e referências para o texto:
-> 30 (branco)
-> 31 (vermelho)
-> 32 (verde)
-> 33 (amarelo)
-> 34 (azul)
-> 35 (magenta)
-> 36 (ciano)
-> 37 (cinza)
***tipos e referências para o fundo:
-> É análogo ao do texto porém começa com 4, ex.: 41 (vermelho)
+As especificações podem ocorrer em qualquer ordem, são separadas com ponto e vírgula
+e a sua omissão acarreta na escolha padrão. Ex.: \033[1;33;45m (letra amarela em negrito em um fundo magenta)
\033[32m (letra verde em estilo normal com fundo padrão- preto)
\033[m (configurações padrão)
print('\033[1;31;43mOlá mundo!\033[m')
(printará 'Olá mundo!' em negrito com letra vermelha e fundo amarelo- O fundo vai apenas até a "!"
"""