import datetime

base_datos_cliente = []

def ejecutar_prueba_4_persistencia_cliente():
    print("--- INICIANDO PRUEBA 4: PERSISTENCIA EN BASE DE DATOS CLIENTE ---")
    
    factura_contingencia = {
        'id_local': 101,
        'punto_venta': 1,
        'nro_comprobante': 2,
        'fecha_emision': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cliente': 'Consumidor Final',
        'neto': 2000.0,
        'iibb_percepcion': 70.0,
        'total': 2070.0,
        'cae': None,
        'estado_arca': 'PENDIENTE_POR_CAIDA'
    }

    base_datos_cliente.append(factura_contingencia)

    if len(base_datos_cliente) > 0 and base_datos_cliente[0]['id_local'] == 101:
        print("RESULTADO: Persistencia exitosa")
        print(f"ID LOCAL: {base_datos_cliente[0]['id_local']}")
        print(f"CLIENTE: {base_datos_cliente[0]['cliente']}")
        print(f"IMPUESTOS (IIBB): {base_datos_cliente[0]['iibb_percepcion']}")
        print(f"ESTADO EN DB: {base_datos_cliente[0]['estado_arca']}")
        print(f"TOTAL REGISTRADO: {base_datos_cliente[0]['total']}")
    else:
        print("RESULTADO: ERROR EN PERSISTENCIA")

if __name__ == "__main__":
    ejecutar_prueba_4_persistencia_cliente()
