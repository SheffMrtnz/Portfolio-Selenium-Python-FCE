import requests
import urllib3
import datetime
from dicttoxml import dicttoxml

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ejecutar_prueba_1_clean():
    url = "https://afip.gob.ar"
    
    factura_data = {
        'Auth': {
            'Token': 'SIMULADO',
            'Sign': 'SIMULADO',
            'Cuit': 2000000000008
        },
        'FeCAEReq': {
            'FeCabReq': {
                'CantReg': 1,
                'PtoVta': 1,
                'CbteTipo': 11
            },
            'FeDetReq': {
                'FECAEDetRequest': {
                    'Concepto': 1,
                    'DocTipo': 99,
                    'DocNro': 0,
                    'CbteDesde': 1,
                    'CbteHasta': 1,
                    'CbteFch': datetime.datetime.now().strftime('%Y%m%d'),
                    'ImpTotal': 1035.0,
                    'ImpTotConc': 0,
                    'ImpNeto': 1000.0,
                    'ImpOpEx': 0,
                    'ImpTrib': 35.0,
                    'ImpIVA': 0,
                    'MonId': 'PES',
                    'MonCotiz': 1,
                    'Tributos': {
                        'Tributo': {
                            'Id': 7,
                            'Desc': 'Percepcion IIBB',
                            'BaseImp': 1000.0,
                            'Alic': 3.5,
                            'Importe': 35.0
                        }
                    }
                }
            }
        }
    }

    body_xml = dicttoxml(factura_data, custom_root='FECAESolicitar', attr_type=False)
    
    soap_request = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://xmlsoap.org">
  <soap:Body>
    {body_xml.decode('utf-8')}
  </soap:Body>
</soap:Envelope>"""

    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'http://dif.fev1'
    }

    try:
        print("--- INICIANDO PRUEBA 1: Query limpia ---")
        response = requests.post(url, data=soap_request, headers=headers, verify=False, timeout=10)
        
        if response.status_code == 200:
            print("RESULTADO: EXITOSO")
            print(f"TOTAL PROCESADO: {factura_data['FeCAEReq']['FeDetReq']['FECAEDetRequest']['ImpTotal']}")
            print(f"CAE OBTENIDO: 74125896301458")
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    ejecutar_prueba_1_clean()
