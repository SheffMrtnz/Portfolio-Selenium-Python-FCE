import requests
import urllib3
import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ejecutar_prueba_2_caido():
    try:
        
        url_falsa = "https://arca.gov.ar"
        
        prox_nro = 1
        neto = 1000.0
        iibb = 35.0
        total = neto + iibb

        xml_request = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://w3.org" xmlns:xsd="http://w3.org" xmlns:soap="http://xmlsoap.org">
  <soap:Body>
    <FECAESolicitar xmlns="http://dif.fev1">
      <Auth>
        <Token>SIMULACION</Token>
        <Sign>SIMULACION</Sign>
        <Cuit>20000000001</Cuit>
      </Auth>
      <FeCAEReq>
        <FeCabReq><CantReg>1</CantReg><PtoVta>1</PtoVta><CbteTipo>11</CbteTipo></FeCabReq>
        <FeDetReq>
          <FECAEDetRequest>
            <Concepto>1</Concepto><DocTipo>99</DocTipo><DocNro>0</DocNro>
            <CbteDesde>{prox_nro}</CbteDesde><CbteHasta>{prox_nro}</CbteHasta>
            <CbteFch>{datetime.datetime.now().strftime('%Y%m%d')}</CbteFch>
            <ImpTotal>{total}</ImpTotal><ImpTotConc>0</ImpTotConc><ImpNeto>{neto}</ImpNeto>
            <ImpOpEx>0</ImpOpEx><ImpTrib>{iibb}</ImpTrib><ImpIVA>0</ImpIVA>
            <MonId>PES</MonId><MonCotiz>1</MonCotiz>
          </FECAEDetRequest>
        </FeDetReq>
      </FeCAEReq>
    </FECAESolicitar>
  </soap:Body>
</soap:Envelope>"""

        headers = {'Content-Type': 'text/xml; charset=utf-8', 'SOAPAction': 'http://dif.fev1FECAESolicitar'}

        print("--- PRUEBA 2: Simulacion de caida ---")
       
        response = requests.post(url_falsa, data=xml_request, headers=headers, verify=False, timeout=3)

    except requests.exceptions.ConnectionError:
        print("RESULTADO: Éxito en prueba 2")
        print("ESTADO: Arca caido (ConnectionError detectado)")
        print("ACCIÓN: El sistema debe activar el modo de facturación offline/contingencia")
    except Exception as e:
        print(f"RESULTADO: ERROR NO ESPERADO | {str(e)}")

if __name__ == "__main__":
    ejecutar_prueba_2_caido()
