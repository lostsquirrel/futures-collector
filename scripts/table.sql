/*
Navicat MySQL Data Transfer

Source Server         : n
Source Server Version : 50505
Source Host           : 192.168.19.66:3306
Source Database       : futures

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-06-27 22:51:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for evaluation_data
-- ----------------------------
DROP TABLE IF EXISTS `evaluation_data`;
CREATE TABLE `evaluation_data` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `trade_date` date DEFAULT NULL,
  `profit` float DEFAULT NULL,
  `commission` float DEFAULT NULL,
  `evaluation_score` int(11) DEFAULT NULL,
  `volume` int(11) DEFAULT NULL,
  `position_time` int(11) DEFAULT NULL,
  `postion_time_str` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for node
-- ----------------------------
DROP TABLE IF EXISTS `node`;
CREATE TABLE `node` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `open` float DEFAULT NULL,
  `close` float DEFAULT NULL,
  `highest` float DEFAULT NULL,
  `lowest` float DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;

