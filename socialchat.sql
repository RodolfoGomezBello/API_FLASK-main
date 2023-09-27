CREATE DATABASE  IF NOT EXISTS `socialchat` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `socialchat`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: socialchat
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `canales`
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `id_canal` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `servidor_id` int NOT NULL,
  `creador_id` int NOT NULL,
  `icono` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_canal`),
  KEY `servidor_id` (`servidor_id`),
  KEY `creador_id` (`creador_id`),
  CONSTRAINT `canales_ibfk_1` FOREIGN KEY (`servidor_id`) REFERENCES `servidores` (`id_servidor`),
  CONSTRAINT `canales_ibfk_2` FOREIGN KEY (`creador_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
INSERT INTO `canales` VALUES (1,'Jaque Pastor',1,1,NULL),(2,'Ventajas del enroque en menos de 10 movimientos',1,2,NULL),(3,'Reglas de la Dama China',2,1,NULL),(4,'La mejor estrategia de juego',2,2,NULL),(5,'Cuestion Malvinas',3,1,NULL),(6,'Comercio Exterior, quienes son nuestros socios',3,2,NULL),(7,'Primeros pasos en Machine Learning',4,1,NULL),(8,'Las mejores erramientas A.I.',4,2,NULL),(9,'CONICET-Proyectos de desarrollo agricola',5,2,NULL),(10,'Proyectos espaciales Argentinos',5,1,NULL),(11,'Escalabilidad en proyectos de Redes Sociales',6,1,NULL),(12,'MongoDB. Primeros pasos',6,1,NULL),(13,'Pueden aprender las computadoras?',7,2,NULL),(14,'Modelos de Redes Neuronales',7,1,NULL),(15,'Remotorizacion del Pucara Fenix',5,1,NULL),(16,'Resumen de los campeones del futbol Argentino en los ultimos años',8,1,'/assets/icono6.png'),(17,'Goleadores Historicos del Futbol Argentino',8,1,'/assets/icono6.png'),(18,'Cual fue la final mas epica de este torneo',10,3,'/assets/icono6.png'),(19,'Distribucion de puntos a exponer',12,1,'/assets/icono1.png'),(20,'Codigos para recursos en Age Of Empires I',9,1,'/assets/icono6.png'),(21,'Documentacion',13,1,'/assets/icono2.png');
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensajes`
--

DROP TABLE IF EXISTS `mensajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensajes` (
  `id_mensaje` int NOT NULL AUTO_INCREMENT,
  `contenido` text NOT NULL,
  `canal_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `fecha_envio` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mensaje`),
  KEY `canal_id` (`canal_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `mensajes_ibfk_1` FOREIGN KEY (`canal_id`) REFERENCES `canales` (`id_canal`),
  CONSTRAINT `mensajes_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensajes`
--

LOCK TABLES `mensajes` WRITE;
/*!40000 ALTER TABLE `mensajes` DISABLE KEYS */;
INSERT INTO `mensajes` VALUES (1,'El mate pastor, es, en ajedrez, uno de los jaque mate mas corto que se conocen despues del mate del loco y que ocurre tras los cuatro primeros movimientos del blanco y los tres primeros del negro, aunque este ultimo es el menos frecuente',1,1,'2023-09-16 03:00:00'),(2,'Una vez me hicieron ese mate, fue muy desepcionante para mi',1,2,'2023-09-16 03:00:00'),(3,'No hay ninguna regla que diga que el juego se debe hacer el enroque, pero el consenso es que cuanto antes, mejor. Es imposible enrocar antes del cuarto movimiento (hay que quitar el caballo y el alfil del camino, lo que implica también un movimiento de un peón). Desde el momento en que es posible el enroque, el jugador tiene que evaluar si vale la pena proteger al rey, o si es más interesante desarrollar alguna jugada o responder a alguna amenaza.',2,2,'2023-09-16 03:00:00'),(4,'El enroque es un objetivo importante en la apertura, ya que sirve a dos propósitos valiosos: mueve al rey a una posición más segura lejos del centro del tablero, y mueve la torre a una posición más activa en el centro del tablero (en el que incluso es posible dar jaque mate con el enroque).',2,1,'2023-09-16 03:00:00'),(5,' La decisión en cuanto a qué lado del castillo generalmente depende de una evaluación del equilibrio entre la seguridad del rey y de la actividad de la torre.',2,1,'2023-09-16 18:24:15'),(6,'Se juega en un tablero con 121 casillas en forma de estrella de David, (de seis puntas). Cada una de estas casillas limita con las seis contiguas (salvo las situadas en los bordes del tablero, que limitan con dos, cuatro o cinco)',3,1,'2023-09-17 15:53:35'),(7,'Cada juego, equipo o color consta de diez fichas o piezas. Al empezar el juego, estas diez fichas de un mismo jugador están juntas, en uno de los triángulos que forman las puntas de la estrella.',3,1,'2023-09-17 15:57:50'),(8,'Cada juego de diez piezas tiene un color diferente o una característica que las distinga de las de otro jugador.',3,1,'2023-09-17 15:59:59'),(9,'Generalmente, las 121 posiciones del tablero tienen forma de agujeros en los que se encajan las piezas. Este diseño ayuda a dejar clara la regla de sólo puede haber una pieza por casilla.',3,1,'2023-09-17 16:02:06'),(10,'El objetivo del juego es llevar desde una punta hasta el triángulo opuesto',3,1,'2023-09-17 16:18:46'),(11,'Como en el clásico juego de las damas, cada jugador sólo mueve una ficha por turno.',3,1,'2023-09-17 16:31:35'),(12,'La Cuestión de las Islas Malvinas, entendida como la disputa de soberanía entre la República Argentina y el Reino Unido por las Islas Malvinas, Georgias del Sur, Sandwich del Sur y los espacios marítimos circundantes, tiene su origen el 3 de enero de 1833 cuando el Reino Unido, quebrando la integridad territorial argentina, ocupó ilegalmente las islas y expulsó a las autoridades argentinas, impidiendo su regreso así como la radicación de argentinos provenientes del territorio continental.',5,1,'2023-09-17 17:03:48'),(13,'Un movimiento válido es: 1. a una casilla adyacente libre. 2. saltando una casilla adyacente ocupada por otra ficha (sea propia o sea de un contrario), y posándola en la casilla siguiente (en la misma dirección), si está libre.',3,1,'2023-09-17 17:19:08'),(14,'El jaque pastor es una estrategia muy poco usada en la actualidad',1,1,'2023-09-17 21:44:18'),(15,'No se si realmente es una ventaja hacer el enroque despues del decimo movimiento',2,1,'2023-09-17 22:03:29'),(16,'Mirando el lado positivo de la partida que perdiste es que lo podrias haber perdido antes',1,3,'2023-09-18 03:02:01'),(17,'buenas noches, este canal es para recordar los maximos goleadores del futbol argentino',17,1,'2023-09-20 02:25:26'),(18,'Sin dudas alguna la final mas epica fue la que involucro a los equipos mas grandes del futbol argentino. River y Boca se enfrentaron en Madrid, el triunfo fue para River Plate',18,3,'2023-09-21 23:55:07'),(19,'llll',18,1,'2023-09-22 02:55:23'),(27,'MongoDB es lo mejor en cuanto escalabilidad',11,1,'2023-09-24 22:56:59'),(28,'Hola, me gustaria que comencemos con la distribucion de tareas para la exposicion del lunes',19,1,'2023-09-24 22:59:43'),(29,'Los codigos para madera: woodstock',20,1,'2023-09-26 00:10:38'),(30,'el codigo para obtener comida es pepperoni pizza',20,1,'2023-09-26 00:20:00'),(31,'el codigo para obtener oro es coinage',20,1,'2023-09-26 00:46:35'),(32,'el codigo para obtener piedra es quarry',20,1,'2023-09-26 00:57:31'),(33,'sin dudas en este listado tiene que estar el Beto Alonso',17,1,'2023-09-26 00:59:22'),(34,'Sin dudas Gitcopilot, ayuda muchisimo!!!',8,1,'2023-09-26 01:02:14'),(35,'Creo que deberia ser una politica nacional financiar nuevos proyectos espaciales, sobre todo para resguardar la sobreania nacional',10,1,'2023-09-26 01:13:23'),(36,'Toda persona que se quiera dedicar al testing, sea programador o no, debe saber que lo fundamental es llevar la documentacion y reportar todo',21,1,'2023-09-27 20:19:01');
/*!40000 ALTER TABLE `mensajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servidores`
--

DROP TABLE IF EXISTS `servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidores` (
  `id_servidor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `propietario_id` int NOT NULL,
  `icono_serv` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_servidor`),
  KEY `propietario_id` (`propietario_id`),
  CONSTRAINT `servidores_ibfk_1` FOREIGN KEY (`propietario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidores`
--

LOCK TABLES `servidores` WRITE;
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
INSERT INTO `servidores` VALUES (1,'Ajedrez',1,NULL),(2,'Damas Chinas',2,NULL),(3,'Politica exterior Argentina',1,'None'),(4,'Desarrollo A.I',1,'None'),(5,'Desarrollo Tecnologico',1,'None'),(6,'MySql vs MongoDb',2,NULL),(7,'Redes Neuronales',1,'None'),(8,'Futbol Argentino',1,'/assets/icono6.png'),(9,'Estrategias y Trucos para AGE OF EMPIRES I',3,'/assets/icono6.png'),(10,'Copa Libertadores de America',3,'/assets/icono6.png'),(11,'La logica y su aplicacion en los lenguajes computacionales',2,'/assets/icono2.png'),(12,'Exposicion 02/10/2023',1,'/assets/icono1.png'),(13,'Testing Manual',1,'/assets/icono4.png');
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'rodolfo','gomez bello','yerb26@gmail.com','123456','1977-08-22','/assets/avatar1.png'),(2,'Fernanda','Zelaya','fernandazelaya161@gmail.com','456789','1990-07-12','/assets/avatar2.png'),(3,'Josefina','Quipildor','josefinaquipildor27@gmail.com','123789','1996-02-02','/assets/avatar4.png');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_servidores`
--

DROP TABLE IF EXISTS `usuarios_servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_servidores` (
  `usuario_id` int NOT NULL,
  `servidor_id` int NOT NULL,
  PRIMARY KEY (`usuario_id`,`servidor_id`),
  KEY `servidor_id` (`servidor_id`),
  CONSTRAINT `usuarios_servidores_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `usuarios_servidores_ibfk_2` FOREIGN KEY (`servidor_id`) REFERENCES `servidores` (`id_servidor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_servidores`
--

LOCK TABLES `usuarios_servidores` WRITE;
/*!40000 ALTER TABLE `usuarios_servidores` DISABLE KEYS */;
INSERT INTO `usuarios_servidores` VALUES (1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(3,3),(1,4),(3,4),(1,5),(3,5),(1,6),(2,6),(3,6),(1,7),(3,7),(1,8),(3,8),(1,9),(3,9),(1,10),(3,10),(1,11),(2,11),(3,11),(1,12),(1,13);
/*!40000 ALTER TABLE `usuarios_servidores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-27 17:21:48
