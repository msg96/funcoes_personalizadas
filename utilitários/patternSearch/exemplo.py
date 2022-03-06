#

from .patternSearch import *

####    COLOQUE O CAMINHO COMPLETO -> AQUI É SÓ UM EXEMPLO

arquivo_a_ser_lido = "/Series.lst"

#

texto_do_arquivo = textFromFile(arquivo_a_ser_lido)
bytes_do_arquivo = bytesFromFile(arquivo_a_ser_lido)
hex_do_arquivo = hexFromFile(arquivo_a_ser_lido)
bin_do_arquivo = binaryFromFile(arquivo_a_ser_lido)

#### PODE PASSAR UMA PATTERN COM PARTES NÃO ESTATICAS NO LUGAR DO CHAR, BYTE, HEX, BIN QUE VC NÃO SABE USE UM '?'

pattern_texto_do_arquivo = "Oquevoc?desej?acharn?arquivo"
pattern_bytes_do_arquivo = b"x04\\x02\\xfe\\x06\\x12\\x00\\x00\\x06s@\\x00\\x00\\noA\\x00\\x00\\"
pattern_hex_do_arquivo = "4f717565766f6??5646573656a6161??6861726e6f61727?756976?f"
pattern_bin_do_arquivo = "0100111101110001??11010101100101011101100110111101?000110110010101100100011?10101110011011001010110101001??00010110000101100011011?100001100001011100100???11100110111101100001?111?010011100010111?101011010010111011001101111"

###

lista_Com_Pattern_do_texto_do_arquivo = patternSearch(texto_do_arquivo, pattern_texto_do_arquivo)
lista_Com_Pattern_do_bytes_do_arquiv = patternSearch(bytes_do_arquivo, pattern_bytes_do_arquivo)
lista_Com_Pattern_do_hex_do_arquivo = patternSearch(hex_do_arquivo, pattern_hex_do_arquivo)
lista_Com_Pattern_do_bin_do_arquivo = patternSearch(bin_do_arquivo, pattern_bin_do_arquivo)

### output = {'digito onde começa no arquivo': 'pattern completa com as letras no lugar dos ? tambem'}
### pode retornar varias pattern dentro do dicionario, dependendo do tamanho do seu arquivo e quão menos especifica ela é
