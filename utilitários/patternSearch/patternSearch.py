####    IMPORTS

import os as __os

####    FUNCAO INTERNA

def __funcao_que_recebe_os_bytes_de_um_arquivo_e_o_retorna(arquivo_a_ser_lido) -> bytes:
    if not __os.path.exists(arquivo_a_ser_lido): return
    try:
        with open(arquivo_a_ser_lido, "rb") as leitor_do_arquivo:
            resultado_da_leitura_em_hex = leitor_do_arquivo.read()
            leitor_do_arquivo.close()
        return resultado_da_leitura_em_hex
    except:
        return

def __funcao_que_recebe_o_texto_de_um_arquivo_e_o_retorna(arquivo_a_ser_lido) -> str:
    bytes_do_arquivo = __funcao_que_recebe_os_bytes_de_um_arquivo_e_o_retorna(arquivo_a_ser_lido)
    try:
        resultado_da_conversao = bytes_do_arquivo.decode(errors="ignore")
        return resultado_da_conversao
    except:
        return

def __funcao_que_recebe_os_bytes_de_um_arquivo_e_retorna_em_hex(arquivo_a_ser_lido) -> str:
    try:
        return bytes.hex(__funcao_que_recebe_os_bytes_de_um_arquivo_e_o_retorna(arquivo_a_ser_lido))
    except:
        return

def __funcao_que_recebe_os_bytes_de_um_arquivo_e_retorna_em_binario(arquivo_a_ser_lido) -> int:
    try:
        local_com_os_bytes_em_hex = __funcao_que_recebe_os_bytes_de_um_arquivo_e_retorna_em_hex(arquivo_a_ser_lido)
        bin_list = ''
        for hex_byte in local_com_os_bytes_em_hex:
            hex_byte_to_int = int(hex_byte, base=16)
            hex_byte_int_to_bin = bin(hex_byte_to_int).lstrip('0b')
            bin_list += hex_byte_int_to_bin
        return bin_list
    except:
        return

def __funcao_recursiva_de_pattern(dados_a_serem_escaneados, byte_atual, pattern_atual, tamanho_inicial_pattern) -> dict:
        if len(dados_a_serem_escaneados) < (byte_atual + tamanho_inicial_pattern): return
        try:
            if dados_a_serem_escaneados[byte_atual] == pattern_atual[0] or pattern_atual[0] == "?":
                if len(pattern_atual) > 1:
                    return __funcao_recursiva_de_pattern(dados_a_serem_escaneados, (byte_atual + 1), pattern_atual[1:], tamanho_inicial_pattern)
                elif len(pattern_atual) == 1:
                    return {(byte_atual - tamanho_inicial_pattern + 1): dados_a_serem_escaneados[(byte_atual - tamanho_inicial_pattern + 1):(byte_atual + 1)]}
        except:
            return

def __funcao_gera_um_dicionario_de_patterns_achados(dados_a_serem_escaneados, pattern_a_ser_encontrado):
    dicionario_para_armazenar_patterns_achados = {}
    tamanho_do_pattern = len(pattern_a_ser_encontrado)
    try:
        for index_byte_atual in range(len(dados_a_serem_escaneados)):
            resultado_da_funcao_recursiva = __funcao_recursiva_de_pattern(dados_a_serem_escaneados, index_byte_atual, pattern_a_ser_encontrado, tamanho_do_pattern)
            if resultado_da_funcao_recursiva:
                dicionario_para_armazenar_patterns_achados.update(resultado_da_funcao_recursiva)
        return dicionario_para_armazenar_patterns_achados
    except:
        return

####    FUNCAO PUBLICA

def bytesFromFile(file):
    return __funcao_que_recebe_os_bytes_de_um_arquivo_e_o_retorna(file)

def textFromFile(file):
    return __funcao_que_recebe_o_texto_de_um_arquivo_e_o_retorna(file)

def hexFromFile(file):
    return __funcao_que_recebe_os_bytes_de_um_arquivo_e_retorna_em_hex(file)

def binaryFromFile(file):
    return __funcao_que_recebe_os_bytes_de_um_arquivo_e_retorna_em_binario(file)

def patternSearch(data, pattern):
    return __funcao_gera_um_dicionario_de_patterns_achados(data, pattern)

####    END OF FILE
