def validar_numero_entero(mensaje_para_usuario):
    try:
        valor_del_usuario = int(input(mensaje_para_usuario))
        return valor_del_usuario

    except ValueError:
        pass
