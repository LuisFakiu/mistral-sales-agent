# Documento de Referencia: Analisis de Ventas

## Resumen General del Dataset

Este documento contiene informacion de referencia sobre el dataset de ventas `sales_data_sample.csv`. Contiene 2,823 registros de ventas de una empresa de modelos a escala y productos coleccionables.

**Periodo:** 2003 a 2005
**Total de registros:** 2,823 lineas de venta
**Moneda:** Dolares estadounidenses (USD)

---

## Lineas de Producto

La empresa maneja 5 lineas de producto principales:

### Classic Cars
- Automoviles clasicos y vintage a escala
- Incluye modelos de diferentes epocas (anos 1930-1970)
- Productos de alta gama, precios elevados
- Codigo de producto: S10_, S12_, S18_, S24_

### Motorcycles
- Motocicletas a escala
- Modelos deportivos y clasicos
- Codigo de producto: S10_

### Planes
- Aviones a escala, tanto civiles como militares
- Modelos historicos y modernos
- Codigo de producto: S18_, S24_, S700_

### Ships
- Barcos y embarcaciones a escala
- Buques de guerra, veleros historicos
- Codigo de producto: S32_, S700_, S72_

### Trucks and Buses
- Camiones y autobuses a escala
- Vehiculos comerciales y de carga
- Codigo de producto: S18_, S24_, S32_

### Vintage Cars
- Automoviles vintage y de coleccion
- Modelos de los anos 1950-1960
- Codigo de producto: S10_, S18_, S24_, S50_

---

## Tamano de Deals (Deal Size)

Las ventas se clasifican en tres categorias segun el monto:

- **Small:** Ventas menores, generalmente pedidos pequenos de pocos items
- **Medium:** Ventas de monto intermedio
- **Large:** Ventas grandes, pedidos de alto valor

---

## Estados de Pedidos (Status)

Los pedidos pueden tener los siguientes estados:

- **Shipped:** Pedido enviado y completado (la mayoria)
- **Resolved:** Pedido resuelto (posible devolucion resuelta)
- **Cancelled:** Pedido cancelado por el cliente o la empresa
- **On Hold:** Pedido en espera, pendiente de accion
- **Disputed:** Pedido en disputa, posible problema de pago
- **In Process:** Pedido en proceso de preparacion

---

## Paises y Territorios

Las ventas se realizan en multiples paises organizados por territorio:

### Norteamerica (NA)
- **USA:** Principal mercado, mayor volumen de ventas
- **Canada:** Segundo mercado en Norteamerica

### Europa (EMEA)
- **France:** Paris, Nantes, Lyon, Reims, Marsella, Toulouse
- **UK:** London, Manchester, Cambridge
- **Germany:** Frankfurt, Berlin, Munich, Stuttgart
- **Spain:** Madrid, Barcelona
- **Italy:** Milan, Turin, Reggio Emilia
- **Sweden:** Goteborg, Stockholm
- **Norway:** Oslo
- **Denmark:** Kobenhavn, Aarhus
- **Netherlands:** Amsterdam, Rotterdam, Utrecht, Zaan
- **Belgium:** Bruxelles, Charleroi
- **Switzerland:** Lausanne, Geneve, Bern
- **Austria:** Graz, Wien, Salzburg
- **Finland:** Helsinki
- **Ireland:** Dublin
- **Portugal:** Lisboa

### Japon (Japan)
- **Japan:** Tokyo, Osaka, Yokohama

### Australia (APAC)
- **Australia:** Sydney, Melbourne, Perth

---

## Precios y Descuentos

- **MSRP:** Precio sugerido de venta al publico (Manufacturer Suggested Retail Price)
- **PRICEEACH:** Precio real pagado por unidad (generalmente menor al MSRP)
- **Descuento:** La diferencia entre MSRP y PRICEEACH representa el descuento otorgado
- Los descuentos varian segun el volumen del pedido y la linea de producto

---

## Metricas Clave de Negocio

### Calculo de Ventas Totales
`SALES = QUANTITYORDERED × PRICEEACH`

### Volumen de Ventas
- Se mide por cantidad de unidades vendidas (QUANTITYORDERED)
- Se mide por valor monetario (SALES)

### Rentabilidad
- La diferencia entre MSRP y PRICEEACH indica el margen de descuento
- Descuentos mas altos pueden indicar negociaciones de volumen

### Tendencias Temporales
- Las ventas se pueden analizar por mes y ano
- Permite identificar estacionalidad y tendencias de crecimiento

---

## Clientes

- Los clientes son empresas coleccionistas, tiendas de juguetes y distribuidores
- Ejemplos de nombres: "Land of Toys Inc.", "Reims Collectables", "Lyon Souveniers"
- Cada cliente tiene informacion de contacto: nombre, telefono, direccion, ciudad, pais

---

## Preguntas Frecuentes que se Pueden Responder

1. Cual es el total de ventas?
2. Cual es la linea de producto mas vendida?
3. Que pais genera mas ingresos?
4. Cual es el promedio por venta?
5. Cuantos pedidos cancelados hay?
6. Cual es el descuento promedio?
7. Quien es el cliente que mas compra?
8. Como evolucionaron las ventas por mes?
9. Que tamano de deal es mas comun?
10. Cual fue el mes con mas ventas?
