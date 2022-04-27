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
-- Table structure for table `mall_bound_by`
--

DROP TABLE IF EXISTS `mall_bound_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mall_bound_by` (
  `Contract_id` varchar(40) NOT NULL,
  `Shop_id` varchar(40) NOT NULL,
  PRIMARY KEY (`Contract_id`),
  UNIQUE KEY `mall_bound_by_Contract_id_Shop_id_7c9da798_uniq` (`Contract_id`,`Shop_id`),
  KEY `mall_bound_by_Shop_id_190ddce7_fk_mall_shops_Shop_id` (`Shop_id`),
  CONSTRAINT `mall_bound_by_Contract_id_e749f2e0_fk_mall_contracts_Contract_id` FOREIGN KEY (`Contract_id`) REFERENCES `mall_contracts` (`Contract_id`),
  CONSTRAINT `mall_bound_by_Shop_id_190ddce7_fk_mall_shops_Shop_id` FOREIGN KEY (`Shop_id`) REFERENCES `mall_shops` (`Shop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mall_bound_by`
--

LOCK TABLES `mall_bound_by` WRITE;
/*!40000 ALTER TABLE `mall_bound_by` DISABLE KEYS */;
/*!40000 ALTER TABLE `mall_bound_by` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:50:19
