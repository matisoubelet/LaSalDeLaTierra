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


INSERT INTO ACCIONES_DE_CIUDAD(NOMBRE, REQUISITO, DESCRIPCION, EFECTO)
VALUES
('Construir Asentamiento', 'El asentamiento debe ser construido adyacente a tu ciudad.', 'El asentamiento genera +1 Industria en un yacimiento o +1 Población en tierra fértil.', 1),
('Mejorar Asentamiento: Ciudad', 'No tiene.', 'Convertí un asentamiento existente en una ciudad.', 0),
('Mejorar Asentamiento: Fuerte', 'No tiene.', 'Convertí un asentamiento existente en un fuerte.', 0),
('Construir Edificación', 'No tiene.', 'Consultar tabla de Edificaciones', 0),
('Construir Rutas', 'Asentamiento o Ciudad destino controlado por tu Civ.', 'Conecta una ciudad o asentamiento con otra. ', 0),
('Conducir Espionaje', 'No tiene.', 'Revela las órdenes del líder de la civilización para su próximo turno.', 0),
('Reclutar Soldados', 'No tiene.', 'Unidad con Fuerza 25. Impacto 0', 0),
('Reclutar Caravana', 'No tiene.', 'Unidad caravanera, usada para construir asentamientos lejos de la ciudad.', 0),
('Reclutar Exploradores', 'No tiene.', 'Unidad exploradora', 0),
('Entrenar Elite', 'No tiene.', 'Similar a Reclutar Soldados, pero posee una habilidad especial.', 0),
('Entregar Ciudad/Asentamiento', 'No tiene.', 'Otorgas tu ciudad o asentamiento a quien elijas.', 0),
('Reparar Daños', 'La edificacion debe haber sufrido daños.', 'Si un asentamiento o ciudad fue saqueada, debe ser reparada o no dará ninguna producción.', 0);

SELECT * FROM ACCIONES_DE_CIUDAD;


INSERT INTO COSTOS_ACCIONES_DE_CIUDAD(ID_ACCION, INDUSTRIA, POBLACION, RIQUEZA)
VALUES
(1, 2, 6, 0),
(2, 6, 6, 4),
(3, 6, 0, 4),
(4, 0, 0, 0),
(5, 1, 0, 0),
(6, 0, 0, 4),
(7, 0, 4, 0),
(8, 0, 2, 0),
(9, 0, 1, 0),
(10, 0, 4, 4),
(11, 0, 0, 0),
(12, 2, 0, 0);

SELECT * FROM COSTOS_ACCIONES_DE_CIUDAD;

# 0 Militar, 1 Caravana, 2 Explorador, 3 Cualquiera
INSERT INTO ACCIONES_DE_UNIDAD(NOMBRE, TIPO, DESCRIPCION)
VALUES
('Marcha/Retirada', 0, 'Move tu Unidad de nuevo, la mitad de su velocidad normal, redondeado abajo. Esta acción puede hacerse incluso si estás al lado de una casilla ocupada por un enemigo. Si terminás en una pelea después de esta acción, estarás en desventaja (-10 Impacto)'),
('Dividir/Reforzar', 0, 'Traslada una cantidad de Fuerza a una Unidad adyacente, o crea una nueva Unidad, o Unidades, con una cantidad de Fuerza que desees, disponible. Los activos como artefactos o u.d.élite pueden trasladarse también.'),
('Embarcar', 3, 'Tu unidad pasa de ubicarse en un casillero de tierra a uno de agua. El costo representa a tu unidad buscando o construyendo barcas.'),
('Explorar', 0, 'Tu unidad revisa los casilleros adyacentes en búsqueda de cosas secretas.'),
('Entregar Activo', 0, 'Tu unidad entrega el numero de elites y reliquias que quieras a otra unidad'),
('Conquistar Ciudad de Jugador', 0, 'Esta accion representa el tiempo requerido para establecer una nueva politica en una ciudad. No es requerido para los NPCs'),
('Construir Asentamiento', 1, 'Construí cualquier asentamiento válido para la casilla donde la Unidad está situada. (Granja, aserradero, mina, pueblo, fuerte, puerto, etc.)'),
('Entregar Activo', 1, 'Tu unidad entrega el numero de elites y reliquias que quieras a otra unidad'),
('Construir Guarida', 2, 'Los exploradores construyen una guarida para estacionarse y detectar unidades ocultas.'),
('Explorar', 2, 'Revela información sobre el casillero donde se encuentra la unidad, y adyacente.');

SELECT * FROM ACCIONES_DE_UNIDAD;


INSERT INTO COSTOS_ACCIONES_DE_UNIDAD(ID_ACCION, INDUSTRIA, RIQUEZA)
VALUES
(1, 0, 0),
(2, 0, 0),
(3, 2, 0),
(4, 1, 0),
(5, 0, 0),
(6, 2, 2),
(7, 4, 0),
(8, 0, 0),
(9, 2, 0),
(10, 0, 0);

SELECT * FROM COSTOS_ACCIONES_DE_UNIDAD;

# 0 Primavera, 1 Verano, 2 Otoño.
INSERT INTO CULTIVOS (NOMBRE, ESTACION)
VALUES
('Ajo', 0),
('Zanahorias', 0),
('Arroz', 0),
('Chirivía', 0),
('Coliflor', 0),
('Frutillas', 0),
('Chauchas', 0),
('Papa', 0),
('Cafeto', 0),
('Tulipán', 0),
('Soja', 0),
('Sorgo', 0),
('Arándano', 1),
('Amapola', 1),
('Ají', 1),
('Girasol', 1),
('Repollo', 1),
('Lúpulo', 1),
('Choclo', 1),
('Tomate', 1),
('Trigo', 1),
('Rabanito', 1),
('Melón', 1),
('Mandioca', 1),
('Batata', 2),
('Alcachofa', 2),
('Berenjena', 2),
('Calabaza', 2),
('Brócoli', 2),
('Grosella', 2),
('Remolacha', 2),
('Aceitunas', 2),
('Espinaca', 2),
('Uvas', 2),
('Acelga', 2),
('Cebolla', 2);

SELECT * FROM CULTIVOS;


INSERT INTO BOSQUES(NOMBRE, GRUPO)
VALUES
('Abacá', 0),
('Acacia', 0),
('Alerce', 0),
('Bananero', 0),
('Naranjo', 0),
('Candil', 0),
('Cajú', 0),
('Limonero', 0),
('Palmera de Azaí', 0),
('Cacaotero', 0),
('Manzanero', 1),
('Durio', 1),
('Duraznero', 1),
('Olivo', 1),
('Tabaco', 1),
('Pomelo', 1),
('Caucho', 1),
('Árbol de té', 1),
('Cannabis', 1),
('Hongos', 1),
('Manglar', 2),
('Sauce', 2),
('Aliso', 2),
('Almendro', 2),
('Cedro', 2),
('Abedul', 2),
('Cerezo', 2),
('Castaño', 2),
('Ginko', 2),
('Arces', 2),
('Palo borracho', 3),
('Ciruela', 3),
('Palta', 3),
('Pino', 3),
('Palosanto', 3),
('Caoba', 3),
('Bocote', 3),
('Palisandro', 3),
('Amaranto', 3),
('Árbol de laca', 3);

SELECT * FROM BOSQUES ORDER BY GRUPO, NOMBRE;


INSERT INTO ANIMALES(NOMBRE, DOMESTICO, GRUPO)
VALUES
('Águila', 0, 0),
('Alce', 0, 0),
('Anaconda', 0, 0),
('Bisonte', 0, 0),
('Buho', 0, 0),
('Buitre', 0, 0),
('Caimán', 0, 0),
('Caballo', 0, 0),
('Carpincho', 0, 0),
('Cebra', 0, 0),
('Chacal', 0, 1),
('Ciervo', 0, 1),
('Cobra', 0, 1),
('Cocodrilo', 0, 1),
('Culebra', 0, 1),
('Chimpancé', 0, 1),
('Elefante', 0, 1),
('Gato montés', 0, 1),
('Guepardo', 0, 1),
('Guacamayo', 0, 1),
('Halcón', 0, 2),
('Harpía', 0, 2),
('Hipopótamo', 0, 2),
('Iguana', 0, 2),
('Jaguar', 0, 2),
('Jirafa', 0, 2),
('Koala', 0, 2),
('Lobo', 0, 2),
('León', 0, 2),
('Manatí', 0, 2),
('Marmota', 0, 3),
('Mono caí', 0, 3),
('Oso', 0, 3),
('Pantera', 0, 3),
('Paloma', 0, 3),
('Puma', 0, 3),
('Tapir', 0, 3),
('Tigre', 0, 3),
('Tortuga', 0, 3),
('Zorro', 0, 3);

SELECT * FROM ANIMALES;

SELECT 
	B.ID, B.NOMBRE AS BOSQUE,
    GROUP_CONCAT(A.NOMBRE ORDER BY A.NOMBRE SEPARATOR ', ') AS `ANIMALES POR BOSQUE`,
    B.GRUPO
	FROM BOSQUES B JOIN ANIMALES A ON B.GRUPO = A.GRUPO
	GROUP BY B.ID, B.NOMBRE, B.GRUPO;