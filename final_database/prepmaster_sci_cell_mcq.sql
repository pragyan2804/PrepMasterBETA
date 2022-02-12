CREATE DATABASE  IF NOT EXISTS `prepmaster` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `prepmaster`;
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
-- Table structure for table `sci_cell_mcq`
--

DROP TABLE IF EXISTS `sci_cell_mcq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sci_cell_mcq` (
  `Question` varchar(300) DEFAULT NULL,
  `CorrectAnswer` varchar(30) DEFAULT NULL,
  `WrongAnswer1` varchar(30) DEFAULT NULL,
  `WrongAnswer2` varchar(30) DEFAULT NULL,
  `WrongAnswer3` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sci_cell_mcq`
--

LOCK TABLES `sci_cell_mcq` WRITE;
/*!40000 ALTER TABLE `sci_cell_mcq` DISABLE KEYS */;
INSERT INTO `sci_cell_mcq` VALUES ('What is the smallest unit of life often called the \'Building Blocks Of Life\'?','cell','organ','nucleous','mitochondria'),('What is known as the \'Power House\' of the cell?','mitochondria','golgi bodies','lysosomes','ribosomes'),('What is the covering which maintains the cell body?','cell membrane','cell wall','lamina','cell coating'),('What acts as control centre of all cell activities?','nucleous','ribosomes','golgi bodies','mitochondria'),('What are the units of inheritance which transfer hereditary characteristics from parents to offsprings?','genes','chromosomes','nucleic acid','RNA'),('Who discovered cell?','Robert Hooke','Charles Darwin','George Mendel','Alexander Fleming'),('What are the organisms made up of more than one cells?','multicellular','unicellular','bicellular','polycellular'),('What are the organisms made up of a single cell?','unicellular','multicellular','bicellular','polycellular'),('What are thread-like structures on the nucleus which carry genes?','chromosomes','genes','RNA','nucleic acid'),('Where does protein synthesis take place?','ribosomes','nucleic acid','mitochondria','golgi bodies');
/*!40000 ALTER TABLE `sci_cell_mcq` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-12 22:55:51
