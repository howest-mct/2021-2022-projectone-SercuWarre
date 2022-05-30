CREATE DATABASE  IF NOT EXISTS `project_1` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `project_1`;
-- MySQL dump 10.13  Distrib 5.7.37, for Win64 (x86_64)
--
-- Host: localhost    Database: project_1
-- ------------------------------------------------------
-- Server version	5.5.5-10.5.15-MariaDB-0+deb11u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Acties`
--

DROP TABLE IF EXISTS `Acties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Acties` (
  `actieid` int(11) NOT NULL AUTO_INCREMENT,
  `actieomschrijving` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`actieid`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Acties`
--

LOCK TABLES `Acties` WRITE;
/*!40000 ALTER TABLE `Acties` DISABLE KEYS */;
INSERT INTO `Acties` VALUES (1,'Laudantium aut quis asperiores eum qui impedi'),(2,'Soluta et laudantium et aperiam ratione nostr'),(3,'Odio laudantium porro sapiente molestias nece'),(4,'Commodi et quia et omnis. Culpa veritatis opt'),(5,'Maiores et autem dolores perspiciatis placeat'),(6,'Laborum aperiam quia sequi quaerat provident.'),(7,'Omnis repellendus placeat et labore et laudan'),(8,'Quo voluptatem blanditiis et ut assumenda. Na'),(9,'Sed repellat ea voluptatibus totam eos. Velit'),(10,'Et autem dolorem non eaque vel pariatur est m'),(11,'Laudantium molestiae enim ipsam ut. Amet omni'),(12,'Eos exercitationem sit eum consequatur archit'),(13,'Labore est occaecati voluptatibus quas nemo.'),(14,'Ut voluptate repellat deserunt nobis molestia'),(15,'Debitis ipsam ab animi non sed et. Veritatis'),(16,'Explicabo illo quia vero quam eum. Ut delectu'),(17,'Quia vitae est nihil culpa sunt eveniet venia'),(18,'Doloremque quod fuga sint distinctio vel ea.'),(19,'Qui ad beatae blanditiis est. Consequatur cor'),(20,'Et non dolorem ut et. Consequuntur excepturi'),(21,'Sit enim sit similique aut. Corrupti aliquam'),(22,'Esse provident sit corrupti maxime. Sint dign'),(23,'Rerum distinctio natus tenetur animi aspernat'),(24,'Est minima quo corporis voluptas in rerum duc'),(25,'Nihil qui exercitationem minima eaque sint do'),(26,'Voluptatem iure dolore exercitationem quia ip'),(27,'Blanditiis et qui quod cumque. Autem sed adip'),(28,'Est officiis explicabo sunt hic optio sit occ'),(29,'Ut voluptatem dolorem rerum sed iure ducimus.'),(30,'Aliquid dolores consequatur odio excepturi od'),(31,'Omnis vel voluptatem reiciendis laboriosam co'),(32,'Voluptas temporibus aliquid sunt tempora dolo'),(33,'Quos et doloremque repellendus et. Et similiq'),(34,'Veritatis delectus non eos fugiat ipsum est u'),(35,'Et sapiente ratione quaerat dolorum fugit dol'),(36,'Est commodi corporis pariatur animi ducimus.'),(37,'Ipsam cumque consequatur eos non. Nemo cum ut'),(38,'Quis quam vitae voluptatem consequuntur. Nost'),(39,'Ea minus sunt ad omnis quae architecto eum. V'),(40,'Est odio saepe tempora unde qui fuga soluta a'),(41,'Reiciendis quibusdam ducimus officia est reru'),(42,'Qui et corporis temporibus quae. Sunt impedit'),(43,'Unde fugiat magnam non et veniam nisi. Eos op'),(44,'Est explicabo porro et assumenda sed numquam'),(45,'Molestiae quia odit quibusdam pariatur earum'),(46,'Sint eos nihil eligendi voluptatibus vel eos'),(47,'At sed velit dolores ut sed quo. Et dolor opt'),(48,'Et deserunt nulla autem vero quae. Veniam vol'),(49,'Rem quidem eligendi nemo perferendis molestia'),(50,'Rerum sequi qui eum praesentium');
/*!40000 ALTER TABLE `Acties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Device`
--

DROP TABLE IF EXISTS `Device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Device` (
  `Deviceid` int(11) NOT NULL AUTO_INCREMENT,
  `naam` varchar(45) DEFAULT NULL,
  `merk` varchar(45) DEFAULT NULL,
  `beschrijving` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `aankoopkost` int(11) DEFAULT NULL,
  `meeteenheid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Deviceid`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Device`
--

LOCK TABLES `Device` WRITE;
/*!40000 ALTER TABLE `Device` DISABLE KEYS */;
INSERT INTO `Device` VALUES (1,'quia','consequatur','Fuga asperiores et cumque sit.','quas',95,'quia'),(2,'omnis','ut','Praesentium quaerat in molestias quia.','suscipit',7,'sapiente'),(3,'quibusdam','est','Fugit et voluptas consequatur sapiente distin','deleniti',5990,'est'),(4,'autem','consequatur','Recusandae eligendi laudantium corrupti maior','repellendus',254,'officia'),(5,'fuga','sint','Non est et ipsum et nam.','consequuntur',618264,'dolores'),(6,'eveniet','et','Recusandae sit voluptatem dolore qui at digni','repellendus',5,'minus'),(7,'autem','laudantium','Vitae voluptatibus voluptates fugiat.','necessitatibus',6621,'harum'),(8,'earum','labore','Sequi voluptatem id amet dolorum enim quis di','omnis',1583187,'voluptatem'),(9,'repudiandae','voluptatem','Quo saepe adipisci sed mollitia optio.','tempora',13,'consequatur'),(10,'omnis','repellendus','Eaque tenetur culpa velit quas iusto.','at',7062556,'est'),(11,'soluta','ducimus','Sint magni et quia.','aut',0,'officia'),(12,'tempore','iste','Rerum ipsum iusto odio accusamus ipsa dolores','unde',0,'quae'),(13,'tenetur','non','Dolor et alias dolor iusto et temporibus.','impedit',0,'consequatur'),(14,'hic','expedita','Doloremque consequatur quis officia architect','omnis',8888,'eos'),(15,'dolore','omnis','Officiis earum modi dolores maiores qui ducim','ratione',426672392,'sint'),(16,'excepturi','facilis','Dolores consequuntur atque ut molestiae enim','recusandae',38908604,'quibusdam'),(17,'dolores','voluptatibus','Sapiente quibusdam rem quos sit ullam et volu','necessitatibus',59803,'rerum'),(18,'quia','aut','Ut harum rerum aut ut.','consequatur',98,'est'),(19,'blanditiis','eum','Harum ad dignissimos et similique sequi magna','voluptas',313,'dolorem'),(20,'iste','fuga','Deserunt ut cum ducimus consequatur.','est',981354,'aliquid'),(21,'necessitatibus','qui','Voluptates fuga et repudiandae adipisci.','et',3360,'temporibus'),(22,'id','sequi','Et architecto ut consequatur harum inventore','soluta',191968572,'sapiente'),(23,'consequuntur','laborum','Laborum qui dolor maiores voluptatibus.','eius',0,'omnis'),(24,'quisquam','magnam','Ratione exercitationem suscipit quo consequat','sed',67,'suscipit'),(25,'ut','quisquam','Amet eum soluta doloremque non officia.','qui',36,'nihil'),(26,'ab','soluta','Vel quas debitis qui sapiente excepturi est v','illo',7171698,'voluptatum'),(27,'autem','esse','Expedita est aut quae rerum.','voluptas',309161,'recusandae'),(28,'temporibus','architecto','Sed labore facilis harum et ipsam non pariatu','quod',274533,'dolorem'),(29,'ea','cum','Omnis laudantium non et accusamus error.','est',0,'ratione'),(30,'id','sed','Nobis velit omnis eos earum itaque optio reru','iusto',43,'nemo'),(31,'asperiores','autem','Assumenda ut quisquam repellat non soluta dic','enim',0,'reiciendis'),(32,'perspiciatis','autem','Nisi nesciunt et dolorem qui beatae magnam co','ut',748,'sapiente'),(33,'dicta','nihil','Quasi consequuntur nostrum qui repellat quo.','enim',67,'omnis'),(34,'autem','totam','Assumenda ducimus error in ut.','quas',0,'eos'),(35,'sit','dicta','Nesciunt eveniet ut voluptatem praesentium.','nobis',732756,'aut'),(36,'sit','quaerat','Rerum sapiente et natus quis vero.','nulla',82543490,'optio'),(37,'ea','placeat','Accusamus consequuntur sit qui debitis conseq','sed',0,'tenetur'),(38,'dolores','nemo','Quos quaerat cumque et labore doloribus quo.','ut',170772,'doloribus'),(39,'qui','non','Possimus reiciendis nulla sit unde voluptatem','dicta',5,'id'),(40,'sed','quod','Est reprehenderit exercitationem reprehenderi','aut',1,'nihil'),(41,'et','et','Ea et animi autem fuga possimus expedita accu','ut',896,'doloribus'),(42,'corrupti','nostrum','Id quam quia alias inventore.','qui',268,'tempora'),(43,'ad','maxime','Ab repudiandae voluptas ad quis.','nam',2,'mollitia'),(44,'id','cum','Vel consequuntur nostrum deleniti consequatur','repellat',0,'et'),(45,'recusandae','distinctio','Molestiae in nihil non est possimus nulla vel','non',5143,'eum'),(46,'cum','amet','Placeat molestias temporibus ex animi neque e','ut',889538,'officiis'),(47,'fugit','tenetur','Omnis aut et dolore voluptatem laboriosam.','mollitia',35872,'consequatur'),(48,'ea','autem','Autem debitis tempore et praesentium qui perf','illo',54499596,'esse'),(49,'possimus','sed','Qui saepe ad tenetur est.','impedit',90,'corrupti'),(50,'voluptatem','aliquid','Sint neque qui ipsum quaerat vel.','qui',192,'et');
/*!40000 ALTER TABLE `Device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frigo`
--

DROP TABLE IF EXISTS `frigo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frigo` (
  `idfrigo` int(11) NOT NULL,
  `frigo inhoud` int(11) NOT NULL,
  PRIMARY KEY (`idfrigo`),
  UNIQUE KEY `idfrigo_UNIQUE` (`idfrigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frigo`
--

LOCK TABLES `frigo` WRITE;
/*!40000 ALTER TABLE `frigo` DISABLE KEYS */;
INSERT INTO `frigo` VALUES (1,703),(2,219),(3,798),(4,76),(5,739),(6,515),(7,308),(8,991),(9,77),(10,214),(11,923),(12,55),(13,166),(14,919),(15,387),(16,717),(17,139),(18,332),(19,468),(20,572),(21,53),(22,184),(23,492),(24,761),(25,375),(26,78),(27,419),(28,274),(29,792),(30,792),(31,649),(32,443),(33,722),(34,191),(35,304),(36,445),(37,902),(38,858),(39,94),(40,507),(41,652),(42,609),(43,37),(44,949),(45,439),(46,613),(47,736),(48,199),(49,929),(50,176);
/*!40000 ALTER TABLE `frigo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historiek`
--

DROP TABLE IF EXISTS `historiek`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `historiek` (
  `volgnummer` int(11) NOT NULL AUTO_INCREMENT,
  `deviceid` int(11) DEFAULT NULL,
  `actieid` int(11) DEFAULT NULL,
  `actiedatum` datetime NOT NULL,
  `waarde` float NOT NULL,
  `commentaar` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`volgnummer`),
  KEY `Deviceid_idx` (`deviceid`),
  KEY `actieid_idx` (`actieid`),
  CONSTRAINT `Deviceid` FOREIGN KEY (`deviceid`) REFERENCES `Device` (`Deviceid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `actieid` FOREIGN KEY (`actieid`) REFERENCES `Acties` (`actieid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historiek`
--

LOCK TABLES `historiek` WRITE;
/*!40000 ALTER TABLE `historiek` DISABLE KEYS */;
INSERT INTO `historiek` VALUES (1,1,1,'1989-03-26 00:00:00',5097540,'Voluptas laborum rem et sunt eligendi ea. Qua'),(2,2,2,'1997-08-12 00:00:00',3540,'Atque ex repudiandae porro impedit. Veritatis'),(3,3,3,'1982-05-26 00:00:00',28968,'Necessitatibus facere quos dignissimos deleni'),(4,4,4,'2009-08-19 00:00:00',19888200,'Totam cupiditate sunt quo laborum qui digniss'),(5,5,5,'1974-10-11 00:00:00',121968000,'Dignissimos eos expedita non asperiores ducim'),(6,6,6,'1993-02-06 00:00:00',420339000,'Recusandae maxime ratione sit voluptatem. Dis'),(7,7,7,'2007-12-18 00:00:00',4,'Qui amet libero illo ab rerum illo eius. Id p'),(8,8,8,'1971-03-31 00:00:00',0,'Molestias et omnis odit occaecati dicta volup'),(9,9,9,'1973-02-14 00:00:00',623,'Vero velit nobis suscipit veniam explicabo co'),(10,10,10,'1994-02-09 00:00:00',7740280,'Modi perferendis aut dolorum officiis accusan'),(11,11,11,'1997-06-26 00:00:00',150143,'Molestiae qui ea ut mollitia. Aut ut perferen'),(12,12,12,'2006-07-14 00:00:00',7248,'Consequuntur esse ea quod voluptatem fuga vol'),(13,13,13,'1997-05-22 00:00:00',60,'Ut quis nihil nihil sit similique repudiandae'),(14,14,14,'1976-03-30 00:00:00',539639000,'Animi sed cupiditate sint. Illo optio sint ve'),(15,15,15,'2014-07-07 00:00:00',9,'Quis quisquam nihil reiciendis fugit minima.'),(16,16,16,'2002-10-23 00:00:00',7,'Quisquam sed aut qui eos blanditiis qui. Cons'),(17,17,17,'1992-08-02 00:00:00',8,'Voluptatum nisi esse vero aperiam explicabo s'),(18,18,18,'1976-10-09 00:00:00',7175890,'Aspernatur voluptates repellendus rem at est'),(19,19,19,'1993-11-30 00:00:00',4989,'Et harum aperiam in laborum sequi ullam eos.'),(20,20,20,'2012-11-18 00:00:00',229,'Ipsa ea ea fuga et enim. Deleniti incidunt ni'),(21,21,21,'2016-03-30 00:00:00',1,'Tempore debitis vero repellendus. Quod rerum'),(22,22,22,'2007-08-30 00:00:00',2022030,'Error nihil repellat eligendi nihil fugit. Ap'),(23,23,23,'1981-03-12 00:00:00',127863,'Enim id perspiciatis quia eum expedita perspi'),(24,24,24,'1987-04-30 00:00:00',4,'Similique vel qui aliquid nihil et qui et. Al'),(25,25,25,'2012-07-18 00:00:00',26824200,'Temporibus deserunt explicabo qui minima. Ess'),(26,26,26,'2016-05-05 00:00:00',652,'Porro voluptate aperiam rerum dolorem dolorib'),(27,27,27,'1995-10-25 00:00:00',97622700,'Architecto ducimus aut asperiores et accusamu'),(28,28,28,'2005-10-24 00:00:00',90539,'Rerum aut harum deleniti repellat. Omnis susc'),(29,29,29,'1997-12-02 00:00:00',0,'At esse quidem alias provident eos. Fuga rati'),(30,30,30,'1972-07-15 00:00:00',262133000,'Tempora qui quia ea est qui amet. Sapiente ut'),(31,31,31,'2018-09-24 00:00:00',350,'Earum reiciendis aut et cupiditate rerum. Fug'),(32,32,32,'1995-03-11 00:00:00',994084000,'Sequi sit nihil aut est. Omnis pariatur aut n'),(33,33,33,'1983-03-26 00:00:00',1,'Sunt velit doloremque qui eius reprehenderit.'),(34,34,34,'1995-08-07 00:00:00',3015390,'Minima nostrum voluptatem aut adipisci est vi'),(35,35,35,'2009-05-08 00:00:00',1,'Aut quam repellendus sapiente provident tempo'),(36,36,36,'1997-06-08 00:00:00',29,'Aliquid corrupti commodi earum. Non molestiae'),(37,37,37,'2021-08-07 00:00:00',9732,'Saepe omnis adipisci id amet placeat quo. Dol'),(38,38,38,'1978-09-20 00:00:00',456,'Enim et perferendis quia temporibus sit. Et q'),(39,39,39,'1992-05-12 00:00:00',3739,'Rerum et et sit dolore et nobis repellendus.'),(40,40,40,'1990-08-19 00:00:00',4110870,'Dolore quos repudiandae unde vitae. Quia ea r'),(41,41,41,'2021-11-29 00:00:00',472,'Quae quia ratione fugit excepturi porro autem'),(42,42,42,'1992-02-01 00:00:00',84,'Quas autem esse debitis. Sapiente a tempore o'),(43,43,43,'2002-09-10 00:00:00',800182000,'Ut ipsa autem ut corporis nihil. Consectetur'),(44,44,44,'2013-08-19 00:00:00',804093,'Ea ipsum unde id voluptas ipsam. Cupiditate l'),(45,45,45,'1982-02-25 00:00:00',0,'Architecto expedita fuga fugiat facere. At qu'),(46,46,46,'2012-10-02 00:00:00',623346,'Est aliquid eos quos maxime assumenda quam ma'),(47,47,47,'1983-10-07 00:00:00',41820,'Distinctio numquam consequuntur illo culpa la'),(48,48,48,'2021-01-28 00:00:00',950425,'Sunt tempore asperiores laboriosam sunt. Susc'),(49,49,49,'2010-08-18 00:00:00',840987000,'Ut eligendi et veniam quas voluptatem. Cupidi'),(50,50,50,'2017-05-18 00:00:00',7102690,'Ut est quam sit repudiandae molestiae vel. Ar');
/*!40000 ALTER TABLE `historiek` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL AUTO_INCREMENT,
  `aantal_drankjes` int(11) DEFAULT NULL,
  `RFid` varchar(45) NOT NULL,
  PRIMARY KEY (`iduser`),
  UNIQUE KEY `iduser_UNIQUE` (`iduser`),
  UNIQUE KEY `RFid_UNIQUE` (`RFid`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,409,'16'),(2,5810,'82'),(3,5017449,'8'),(4,57229,''),(5,8119,'51859'),(6,0,'99725048'),(7,19455692,'7'),(8,814645,'3753322'),(9,0,'8742'),(10,5,'168283004'),(11,562863462,'397374626'),(12,0,'40794'),(13,383,'79'),(14,0,'8745'),(15,21,'4051719'),(16,77324,'6994'),(17,3915,'78'),(18,4,'797575473'),(19,5007,'54168'),(20,5494875,'618'),(21,935,'5'),(22,692,'463465892'),(23,226693,'25'),(24,3076028,'910152924'),(25,2907,'373'),(26,920172,'268'),(27,4,'80951'),(28,262984185,'9802286'),(29,0,'55843'),(30,675,'7976117'),(31,246,'138'),(32,0,'333195299'),(33,792532,'2'),(34,79,'2272'),(35,634,'4822'),(36,170709278,'15933'),(37,66,'6465'),(38,3,'877152'),(39,96990259,'9'),(40,848,'5006'),(41,6,'3612720'),(42,47072,'9718'),(43,291167,'3859417'),(44,756,'35963'),(45,460310,'8271155'),(46,2461,'519'),(47,777659,'8769532'),(48,7206235,'19'),(49,3,'51908130'),(50,51096,'725454');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'project_1'
--

--
-- Dumping routines for database 'project_1'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-24 11:35:06
