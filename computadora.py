from enlazadorCargador import enlazador_cargador
from utils.programas import codigo_entrada_enlazador


class Computadora:
    def __init__(self, tamano_memoria=2048):
        # Simula la memoria (cada celda de memoria almacena un entero de 32 bits)
        self.memoria = ["0" * 32 for _ in range(tamano_memoria)]
        self.registros = [0] * 8

        """---------------------------------------------------------------------------------
        BANDERAS DE DREAMCHASER
        ------------------------------------------------------------------------------------"""
        # Bandera para carry
        self.bandera_carry = 0
        # Bandera para zero
        self.bandera_zero = 0
        # Bandera para negativo
        self.bandera_neg = 0
        # Bandera para par
        self.bandera_par = 0
        # Bandera para desbordamiento
        self.bandera_desb = 0
        # Puntero de instrucción (PC)
        self.pc = 0

    """
    -------------------------
    ENLAZADOR - CARGADOR
    -------------------------
    """

    # Carga el código binario proporcionado por el ensamblador de manera contigua en memoria
    # Comenzando desde el 0
    def cargar_codigo(self, codigo_entrada, direccion_de_inicio=0x0000):
        mapa_memoria = enlazador_cargador(codigo_entrada, direccion_de_inicio)
        for direccion, instr in mapa_memoria.items():
            self.memoria[direccion] = instr
        return self.memoria

    def mostrar_memoria(self):
        memoria_ocupada = []

        for direccion, instr in enumerate(self.memoria):
            if instr != 0:
                memoria_ocupada.append(
                    (f"{direccion}", instr)
                )  # Dirección en Hex, valor binario

        if not memoria_ocupada:
            return [("No hay instrucciones en memoria", "")]  # Mensaje en la tabla

        return memoria_ocupada  # Retorna la lista de tuplas
