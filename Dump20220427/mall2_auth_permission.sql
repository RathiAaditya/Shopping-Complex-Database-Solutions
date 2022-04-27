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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add companies',1,'add_companies'),(2,'Can change companies',1,'change_companies'),(3,'Can delete companies',1,'delete_companies'),(4,'Can view companies',1,'view_companies'),(5,'Can add contracts',2,'add_contracts'),(6,'Can change contracts',2,'change_contracts'),(7,'Can delete contracts',2,'delete_contracts'),(8,'Can view contracts',2,'view_contracts'),(9,'Can add customer',3,'add_customer'),(10,'Can change customer',3,'change_customer'),(11,'Can delete customer',3,'delete_customer'),(12,'Can view customer',3,'view_customer'),(13,'Can add services',4,'add_services'),(14,'Can change services',4,'change_services'),(15,'Can delete services',4,'delete_services'),(16,'Can view services',4,'view_services'),(17,'Can add shops',5,'add_shops'),(18,'Can change shops',5,'change_shops'),(19,'Can delete shops',5,'delete_shops'),(20,'Can view shops',5,'view_shops'),(21,'Can add slots',6,'add_slots'),(22,'Can change slots',6,'change_slots'),(23,'Can delete slots',6,'delete_slots'),(24,'Can view slots',6,'view_slots'),(25,'Can add invoice',7,'add_invoice'),(26,'Can change invoice',7,'change_invoice'),(27,'Can delete invoice',7,'delete_invoice'),(28,'Can view invoice',7,'view_invoice'),(29,'Can add booking',8,'add_booking'),(30,'Can change booking',8,'change_booking'),(31,'Can delete booking',8,'delete_booking'),(32,'Can view booking',8,'view_booking'),(33,'Can add company_contact_no',9,'add_company_contact_no'),(34,'Can change company_contact_no',9,'change_company_contact_no'),(35,'Can delete company_contact_no',9,'delete_company_contact_no'),(36,'Can view company_contact_no',9,'view_company_contact_no'),(37,'Can add provides',10,'add_provides'),(38,'Can change provides',10,'change_provides'),(39,'Can delete provides',10,'delete_provides'),(40,'Can view provides',10,'view_provides'),(41,'Can add bound_by',11,'add_bound_by'),(42,'Can change bound_by',11,'change_bound_by'),(43,'Can delete bound_by',11,'delete_bound_by'),(44,'Can view bound_by',11,'view_bound_by'),(45,'Can add log entry',12,'add_logentry'),(46,'Can change log entry',12,'change_logentry'),(47,'Can delete log entry',12,'delete_logentry'),(48,'Can view log entry',12,'view_logentry'),(49,'Can add permission',13,'add_permission'),(50,'Can change permission',13,'change_permission'),(51,'Can delete permission',13,'delete_permission'),(52,'Can view permission',13,'view_permission'),(53,'Can add group',14,'add_group'),(54,'Can change group',14,'change_group'),(55,'Can delete group',14,'delete_group'),(56,'Can view group',14,'view_group'),(57,'Can add user',15,'add_user'),(58,'Can change user',15,'change_user'),(59,'Can delete user',15,'delete_user'),(60,'Can view user',15,'view_user'),(61,'Can add content type',16,'add_contenttype'),(62,'Can change content type',16,'change_contenttype'),(63,'Can delete content type',16,'delete_contenttype'),(64,'Can view content type',16,'view_contenttype'),(65,'Can add session',17,'add_session'),(66,'Can change session',17,'change_session'),(67,'Can delete session',17,'delete_session'),(68,'Can view session',17,'view_session'),(69,'Can add admin model',18,'add_adminmodel'),(70,'Can change admin model',18,'change_adminmodel'),(71,'Can delete admin model',18,'delete_adminmodel'),(72,'Can view admin model',18,'view_adminmodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:50:23
