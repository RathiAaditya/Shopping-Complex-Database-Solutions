-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: mall2
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `mall_provides`
--

DROP TABLE IF EXISTS `mall_provides`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mall_provides` (
  `Contract_id` varchar(40) NOT NULL,
  `Service_id` int NOT NULL,
  PRIMARY KEY (`Contract_id`),
  UNIQUE KEY `mall_provides_Contract_id_Service_id_b177bfb0_uniq` (`Contract_id`,`Service_id`),
  KEY `mall_provides_Service_id_e8a83d94_fk` (`Service_id`),
  CONSTRAINT `mall_provides_Contract_id_e419eb89_fk_mall_contracts_Contract_id` FOREIGN KEY (`Contract_id`) REFERENCES `mall_contracts` (`Contract_id`),
  CONSTRAINT `mall_provides_Service_id_e8a83d94_fk` FOREIGN KEY (`Service_id`) REFERENCES `mall_services` (`Service_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mall_provides`
--

LOCK TABLES `mall_provides` WRITE;
/*!40000 ALTER TABLE `mall_provides` DISABLE KEYS */;
INSERT INTO `mall_provides` VALUES ('3300',1),('3301',1),('3302',1),('3303',2),('3304',2),('3305',2),('3306',3),('3307',3),('3308',3),('3309',4),('3310',4),('3311',4),('3312',5),('3313',5),('3314',5),('3315',6),('3316',6),('3317',6),('3318',7),('3319',7),('3320',7),('3321',8),('3322',8),('3323',8),('3324',9),('3325',9),('3326',9),('3327',10),('3328',10),('3329',10);
/*!40000 ALTER TABLE `mall_provides` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:50:22
