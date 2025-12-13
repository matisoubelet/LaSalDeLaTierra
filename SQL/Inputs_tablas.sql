USE LaSalDeLaTierra;

INSERT INTO TERRENOS (NOMBRE, DESCRIPCION)
VALUES
('Tierra yerma', 'Casilla de tierra donde sólo puede construirse un fuerte. Suelen ser de color amarillo, blanco, gris o marrón – nunca verde. Las unidades se trasladan con normalidad.'),
('Montaña', 'Casilla de tierra, nada puede ser construido en esta ubicación. Tiene distintos colores pero la forma es siempre la misma - triangular, termina en punta. Las unidades que entren en esta casilla sufren un penalizador de -1 a su movimiento y -30% fuerza por lo arduo y peligroso de atravesar montañas.'),
('Cerro', 'Casilla de tierra donde sólo puede construirse un fuerte. Tiene distintos colores pero la forma es siempre la misma - tierra elevada, cuadrada, no termina en punta. Las unidades que entren en esta casilla sufren un penalizador de -1 a su movimiento – al mismo tiempo ofrece un bonificador al Impacto de +10. Si un Fuerte es construido, éste tiene un bonificador al Impacto de +20.'),
('Mar', 'Casilla de agua donde nada puede ser construido. Las unidades se mueven 1 casilla extra si su movimiento es sólo por Mar – Para que una unidad entre en esta casilla (desde tierra) debe gastarse 2R + 2T, representando la construcción o búsqueda improvisada de barcas.'),
('Costa', 'Casilla de tierra, de cualquier tipo, conectada a una de agua adyacente. Esto se denota por una línea celeste clara en la parte de agua, y una línea clara color arena en la de tierra.'),
('Yacimiento', 'Montes y bosques donde puede construirse un asentamiento para generar +1 Industria.'),
('Tierra fertil', 'Casilla de tierra donde puede construirse un asentamiento para generar +1 Población. Su color es de un verde fuerte o claro.');

SELECT * FROM TERRENOS;


INSERT INTO EDIFICACIONES (NOMBRE, DESCRIPCION, EFECTO)
VALUES
('Mercado','Permite comerciar con otra Ciudad que también tenga un mercado. +1 Estabilidad.', 1),
('Espacio Público','El espacio público genera +2 Estabilidad y puede ser lo que el jugador desee: un templo, jardines, teatros, estadios, etc.', 2),
('Cuarteles','Podes entrenar unidades militares en esta construcción.', 0),
('Forja','Crea armas, armaduras y artefactos para tu civilización.', 0),
('Almacenes','Bonificación de +1 a la producción de Población', 2),
('Talleres','Bonificación de +1 a la producción de Industria', 1),
('Base de Organización','Base de operaciones para una Organización y su Líder.', 0),
('Producto','Elabora un producto nuevo de uno existente para comercio.', 0);

SELECT * FROM EDIFICACIONES;

	
INSERT INTO COSTOS_EDIFICACIONES(ID_EDIFICACION, INDUSTRIA, RIQUEZA, RIQ_X_TURNO)
VALUES
(1, 2, 0, 0),
(2, 4, 1, 1),
(3, 2, 0, 0),
(4, 2, 0, 0),
(5, 4, 2, 0),
(6, 2, 4, 0),
(7, 2, 1, 1),
(8, 6, 1, 1);

SELECT * FROM COSTOS_EDIFICACIONES;