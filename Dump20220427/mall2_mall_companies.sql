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
-- Table structure for table `mall_companies`
--

DROP TABLE IF EXISTS `mall_companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mall_companies` (
  `Company_id` varchar(40) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(70) NOT NULL,
  PRIMARY KEY (`Company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mall_companies`
--

LOCK TABLES `mall_companies` WRITE;
/*!40000 ALTER TABLE `mall_companies` DISABLE KEYS */;
INSERT INTO `mall_companies` VALUES ('100000','Agarwal Shopping Complex','shopping@hyderabad.bits-pilani.ac.in'),('100001','Hamleys Ltd.','hamleyadmin@hamley.com'),('100002','Johnson&Johnson','jjadmin@hotmail.com'),('100003','Secure Security Solutions','sss@gmail.com'),('100004','McDonald\'s','mcd@gmail.com'),('100005','KFC','kfc@kfcadmin.com'),('100006','Shine Cleaning Services','scs@rocketmail.com'),('100007','Germclean Services','germ@germservices.com'),('100008','Peter England','peter@hotmail.com'),('100009','Bajaj LED','led@bajajled.com'),('100010','Apple Inc','apple@appleadmin.com'),('100011','TSSPDCL','telenganaelec@tsspdcl.com'),('100012','Vendikin','vm@vendikin.com'),('100013','JioFiber','ambani@jio.com'),('100014','MaintainEasy','easy@maintain.com'),('100015','LiftAll','lift@elevation.com'),('100016','Lookool','kul@lol.com'),('100017','FirstCry','firstcry@gmail.com');
/*!40000 ALTER TABLE `mall_companies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:50:18
