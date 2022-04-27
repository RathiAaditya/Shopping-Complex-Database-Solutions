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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-04-18 17:05:40.374942'),(2,'auth','0001_initial','2022-04-18 17:05:42.027497'),(3,'admin','0001_initial','2022-04-18 17:05:42.455672'),(4,'admin','0002_logentry_remove_auto_add','2022-04-18 17:05:42.501381'),(5,'admin','0003_logentry_add_action_flag_choices','2022-04-18 17:05:42.555391'),(6,'contenttypes','0002_remove_content_type_name','2022-04-18 17:05:42.924485'),(7,'auth','0002_alter_permission_name_max_length','2022-04-18 17:05:43.312981'),(8,'auth','0003_alter_user_email_max_length','2022-04-18 17:05:43.451395'),(9,'auth','0004_alter_user_username_opts','2022-04-18 17:05:43.491411'),(10,'auth','0005_alter_user_last_login_null','2022-04-18 17:05:43.681481'),(11,'auth','0006_require_contenttypes_0002','2022-04-18 17:05:43.697535'),(12,'auth','0007_alter_validators_add_error_messages','2022-04-18 17:05:43.743895'),(13,'auth','0008_alter_user_username_max_length','2022-04-18 17:05:43.984294'),(14,'auth','0009_alter_user_last_name_max_length','2022-04-18 17:05:44.213512'),(15,'auth','0010_alter_group_name_max_length','2022-04-18 17:05:44.395582'),(16,'auth','0011_update_proxy_permissions','2022-04-18 17:05:44.451014'),(17,'auth','0012_alter_user_first_name_max_length','2022-04-18 17:05:44.581278'),(18,'mall','0001_initial','2022-04-18 17:05:47.766801'),(19,'sessions','0001_initial','2022-04-18 17:05:47.904397'),(20,'mall','0002_alter_contracts_type_alter_customer_mobile_id_and_more','2022-04-19 03:32:25.253482'),(21,'mall','0003_alter_booking_options_alter_bound_by_options_and_more','2022-04-25 17:12:25.330406'),(22,'mall','0004_invoice_totalamount','2022-04-25 19:09:31.188311'),(23,'mall','0005_remove_invoice_totalamount','2022-04-25 19:24:31.292906'),(24,'mall','0006_adminmodel_alter_booking_in_time_and_more','2022-04-26 06:48:29.206710'),(25,'mall','0007_alter_invoice_date_paid_alter_invoice_invoice_id','2022-04-26 09:14:04.944831'),(26,'mall','0007_alter_services_type','2022-04-26 13:17:15.831819'),(27,'mall','0008_merge_20220426_1847','2022-04-26 13:17:15.843188'),(28,'mall','0008_merge_20220426_1923','2022-04-26 13:53:51.835617'),(29,'mall','0008_contracts_id_alter_contracts_contract_id','2022-04-26 15:52:08.155274'),(30,'mall','0009_remove_contracts_id_alter_contracts_contract_id','2022-04-26 15:52:08.165094'),(31,'mall','0010_contracts_id_alter_contracts_contract_id','2022-04-26 15:52:08.175234'),(32,'mall','0011_remove_contracts_id_alter_contracts_contract_id','2022-04-26 15:52:08.184811'),(33,'mall','0012_company_contact_no_id_and_more','2022-04-26 15:52:08.195507'),(34,'mall','0013_alter_contracts_type','2022-04-26 15:52:08.203973'),(35,'mall','0014_alter_bound_by_contract_alter_provides_contract','2022-04-26 15:52:08.213884'),(36,'mall','0015_merge_20220426_2035','2022-04-26 15:52:08.223100'),(37,'mall','0016_remove_company_contact_no_id_and_more','2022-04-26 15:55:46.514783'),(38,'mall','0017_remove_company_contact_no_comp_cont_id_and_more','2022-04-26 16:07:59.921847'),(39,'mall','0018_remove_company_contact_no_comp_cont_id_and_more','2022-04-26 16:33:01.848888'),(40,'mall','0019_remove_company_contact_no_comp_cont_id_and_more','2022-04-26 19:23:33.663598');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:50:20
