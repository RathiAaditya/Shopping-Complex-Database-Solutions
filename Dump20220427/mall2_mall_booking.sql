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
-- Table structure for table `mall_booking`
--

DROP TABLE IF EXISTS `mall_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mall_booking` (
  `Booking_id` varchar(40) NOT NULL,
  `in_time` datetime(6) NOT NULL,
  `out_time` datetime(6) NOT NULL,
  `Invoice_id` int NOT NULL,
  `Slot_id` int NOT NULL,
  `mobile_id` bigint NOT NULL,
  PRIMARY KEY (`Booking_id`),
  KEY `mall_booking_Slot_id_24cbd759_fk_mall_slots_Slot_id` (`Slot_id`),
  KEY `mall_booking_mobile_id_48494224_fk` (`mobile_id`),
  KEY `mall_booking_Invoice_id_880b1f6c_fk` (`Invoice_id`),
  CONSTRAINT `mall_booking_Invoice_id_880b1f6c_fk` FOREIGN KEY (`Invoice_id`) REFERENCES `mall_invoice` (`Invoice_id`),
  CONSTRAINT `mall_booking_mobile_id_48494224_fk` FOREIGN KEY (`mobile_id`) REFERENCES `mall_customer` (`mobile_id`),
  CONSTRAINT `mall_booking_Slot_id_24cbd759_fk_mall_slots_Slot_id` FOREIGN KEY (`Slot_id`) REFERENCES `mall_slots` (`Slot_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mall_booking`
--

LOCK TABLES `mall_booking` WRITE;
/*!40000 ALTER TABLE `mall_booking` DISABLE KEYS */;
/*!40000 ALTER TABLE `mall_booking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:50:17
