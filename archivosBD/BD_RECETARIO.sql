-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: recetario
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
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id_ing` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id_ing`),
  UNIQUE KEY `id_ing` (`id_ing`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Papa'),(2,'Zanahoria'),(3,'Arbejas'),(4,'Salmon fresco'),(5,'Mayonesa'),(6,'Clara de huevo'),(7,'Diente de ajo'),(8,'Limón'),(9,'Sal'),(10,'Pollo entero'),(11,'Cebolla'),(12,'Hierbas'),(13,'Manteca de cerdo'),(14,'Trigo burgol'),(15,'Carne molida'),(16,'tomate'),(17,'Lechuga'),(18,'Perejil'),(19,'Pimiento Rojo'),(20,'Huevos'),(21,'Sémola'),(22,'Azucar'),(23,'Poroto'),(24,'Maiz Pelado'),(25,'Queso Tybo'),(26,'Zapallo'),(27,'Pan rallado');
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preparacion`
--

DROP TABLE IF EXISTS `preparacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preparacion` (
  `id_preparacion` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(255) DEFAULT NULL,
  `orden` tinyint DEFAULT NULL,
  `receta_id` int DEFAULT NULL,
  PRIMARY KEY (`id_preparacion`),
  UNIQUE KEY `id_preparacion` (`id_preparacion`),
  KEY `fk_receta_p` (`receta_id`),
  CONSTRAINT `fk_receta_p` FOREIGN KEY (`receta_id`) REFERENCES `recetas` (`id_receta`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preparacion`
--

LOCK TABLES `preparacion` WRITE;
/*!40000 ALTER TABLE `preparacion` DISABLE KEYS */;
INSERT INTO `preparacion` VALUES (1,'Cortar las verduras en cubos',1,1),(2,'Cocinar',2,1),(3,'Unir y mezclar',3,1),(4,'Encender el horno a 200° C',1,2),(5,'Secar los lomos de salmonasegurando que no quedan escamas en la piel.',2,2),(6,'Sazonamos, colocamos en una fuente de horno y reservamos.',3,2),(7,'Pelamos el diente de ajo, rallamos la mitad y lo mezclamos con la mayonesa.',4,2),(8,'Añadimos un poco de ralaldura de limon y removemos.',5,2),(9,'Batimos la clara de huevo a punto nieve.',6,2),(10,'Mezclamos con la mayonesa suavemente y con movimientos envolventes.',7,2),(11,'Extendemos una capa de la espuma de mayonesa sobre los lomos de salmon, introducimos en el horno y cocemos durante 10 miuntos.',8,2),(12,'Si una vez hecho el salmon la superficie no se dorara y quisieramos darle un poco de color, añadimos un toque de grill final.',9,2),(13,'Salpimentamos el pollo por dentro y metemos en el interior media cebolla, medio limon y una buena rama de cada una de las hierbas.',1,3),(14,'Preparamos una  \"cama\" con papas cortadas en rodajas gruesas yu cebolla cortada en juliana, dispuestas en una bandeja de horno.',2,3),(15,'Sobre las papas repartimos algunas hierbas aromaticas.',3,3),(16,'Sobre esa cama ponemos el pollo, untando su exterior con manteca de cerdo.',4,3),(17,'Encima ponemos algunas hojitas de tomillo y de romero y lo metemos al horno precalentado a 90° C.',5,3),(18,'Asamos durante 80 minutos, dando la vuelta al pollo cada 20 minutos.',6,3),(19,'Al final, gratinamos durante 5 minutos para dar color.',7,3),(20,'Remojar el trigo por 10 min con agua tibia',1,21),(23,'Hervir los huevos',2,21),(25,'Calentar una cacerola con agua',1,23),(28,'Remojar el poroto y el maiz la noche anterior',1,24),(29,'Cortar las papas en rodajas',1,25),(30,'Poner a hervir agua en una cacerola',2,25),(31,'Cortar la carne',2,24),(32,'picar las verduras',3,24),(33,'Verter la carne en un bols',1,26),(34,'Colocar los huevos y los condimentos y mexclar',2,26);
/*!40000 ALTER TABLE `preparacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receta_ingrediente`
--

DROP TABLE IF EXISTS `receta_ingrediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receta_ingrediente` (
  `id_rxi` int NOT NULL AUTO_INCREMENT,
  `receta_id` int DEFAULT NULL,
  `ing_id` int DEFAULT NULL,
  `unidad` varchar(30) DEFAULT NULL,
  `cantidad` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_rxi`),
  UNIQUE KEY `id_rxi` (`id_rxi`),
  KEY `fk_receta` (`receta_id`),
  KEY `fk_ingrediente` (`ing_id`),
  CONSTRAINT `fk_ingrediente` FOREIGN KEY (`ing_id`) REFERENCES `ingredientes` (`id_ing`),
  CONSTRAINT `fk_receta` FOREIGN KEY (`receta_id`) REFERENCES `recetas` (`id_receta`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receta_ingrediente`
--

LOCK TABLES `receta_ingrediente` WRITE;
/*!40000 ALTER TABLE `receta_ingrediente` DISABLE KEYS */;
INSERT INTO `receta_ingrediente` VALUES (1,1,1,'kg','2'),(2,1,2,'kg','1'),(3,1,3,'kg','1'),(4,2,4,'un.','2'),(5,2,5,'gr','80'),(6,2,6,'un.','1'),(7,2,7,'un.','0.5'),(8,2,8,'un.','1'),(9,2,9,'a','gusto'),(10,3,10,'un.','1'),(11,3,8,'un.','1'),(12,3,11,'un.','1'),(13,3,12,'al','gusto'),(14,3,13,'gr','10'),(15,3,1,'un.','3'),(16,21,14,'grs.','400'),(17,21,15,'grs.','800'),(28,21,19,'unidades','1'),(29,1,5,'grs.','100'),(30,2,1,'kg','1'),(31,21,20,'docena','05'),(32,23,21,'grs.','250'),(33,23,8,'unidades','1'),(34,23,22,'grs.','200'),(38,24,23,'grs.','250'),(39,24,24,'grs.','250 '),(40,25,1,'kg','2'),(41,25,25,'grs.','800'),(42,24,26,'kg','1'),(43,26,15,'grs.','500'),(44,26,20,'unidades','1'),(45,26,27,'grs.','250');
/*!40000 ALTER TABLE `receta_ingrediente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `id_receta` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  `t_preparacion` smallint DEFAULT NULL,
  `t_coccion` smallint DEFAULT NULL,
  `creacion` date DEFAULT NULL,
  `etiqueta` varchar(60) DEFAULT NULL,
  `favorito` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_receta`),
  UNIQUE KEY `id_receta` (`id_receta`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (1,'Ensalada rusa',20,20,'2023-03-15','Ensaladas',1),(2,'Salmon al horno',20,10,'2023-07-10','Al horno',1),(3,'Pollo al horno con finas hierbas',90,80,'2023-07-09','Al horno',0),(21,'Keppe',40,40,'2023-07-22','Comida Arabe',0),(23,'Anchi',20,30,'2023-08-01','Postre Regional',0),(24,'Locro',60,240,'2023-08-01','Comida Regional',1),(25,'Papa con Queso',30,30,'2023-08-01','tipica',0),(26,'Albóndigas',30,30,'2023-08-01','tipica',0);
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01 22:49:54
