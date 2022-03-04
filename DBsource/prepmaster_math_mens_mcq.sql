-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: prepmaster
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `math_mens_mcq`
--

DROP TABLE IF EXISTS `math_mens_mcq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `math_mens_mcq` (
  `Question` varchar(200) DEFAULT NULL,
  `RightAnswer` varchar(20) DEFAULT NULL,
  `WrongAnswer1` varchar(20) DEFAULT NULL,
  `WrongAnswer2` varchar(20) DEFAULT NULL,
  `WrongAnswer3` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `math_mens_mcq`
--

LOCK TABLES `math_mens_mcq` WRITE;
/*!40000 ALTER TABLE `math_mens_mcq` DISABLE KEYS */;
INSERT INTO `math_mens_mcq` VALUES ('What is the surface covered by the boundary of an object?','Area','Perimeter','Volume','Space'),('What is the length of boundary covered by a plane shape?','Perimeter','Area','Volume','Space'),('What is the total surface area of a cuboid?','2*(lb+bh+hl)','2*h*(l+b)','4*side*side','6*side*side'),('What is the total surface area of a cylinder?','2*pi*r*(r+h)','3*pi*r*r','4*pi*r*r','pi*r*(r+l)'),('What is the area of a triangle?','(1/2)*base*height','pi*radius*radius','height*altitude','side+side+side'),('What is the area of a square?','side*side','length*breadth','2*pi*radius','6*side*side'),('What is the total surface area of a cube?','6*side*side','2*(lb+bh+hl)','2*h*(l+b)','4*side*side'),('What is the perimeter of a square?','4*side','side*side','2*pi*radius','(1/2)*base*height'),('What is the area of a circle?','pi*radius*radius','2*pi*radius','3*pi*radius*radius','2*pi*radius*radius'),('What is the perimeter of circle?','2*pi*radius','pi*radius*radius','2*pi*radius*radius','3*pi*radius*radius');
/*!40000 ALTER TABLE `math_mens_mcq` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-13 22:32:07

