import datetime

facturas_pendientes = []

def ejecutar_prueba_4_contingencia():
    print("--- INICIANDO PRUEBA 4: GENERACIÓN EN CONTINGENCIA ---")
    
  
    factura_offline = {
        'nro_interno': 2,
        'fecha': datetime.datetime.now().strftime('%Y%m%d'),
        'neto': 2000.0,
        'iibb': 70.0,
        'total': 2070.0,
        'estado': 'PENDIENTE_CAE'
    }
    
    
    facturas_pendientes.append(factura_offline)
    
    print("RESULTADO: Facturacion guardada localmente")
    print(f"NRO INTERNO: {factura_offline['nro_interno']}")
    print(f"ESTADO: {factura_offline['estado']}")
    print(f"TOTAL A ENVIAR LUEGO: {factura_offline['total']}")
    print(f"COLA DE ESPERA: {len(facturas_pendientes)} comprobante(s)")

if __name__ == "__main__":
    ejecutar_prueba_4_contingencia()
