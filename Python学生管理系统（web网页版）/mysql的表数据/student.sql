/*
Navicat MySQL Data Transfer

Source Server         : MySQL
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : zs

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-11-02 11:17:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(255) DEFAULT NULL,
  `ssex` varchar(255) DEFAULT NULL,
  `sage` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('24', '米兔', '男', '15');
INSERT INTO `student` VALUES ('25', '李俊基', '男', '12');
INSERT INTO `student` VALUES ('43', '简力', '女', '44');
INSERT INTO `student` VALUES ('64', '肖兔', '男', '12');
INSERT INTO `student` VALUES ('65', '小红', '男', '13');
INSERT INTO `student` VALUES ('66', '李俊基', '男', '12');
INSERT INTO `student` VALUES ('68', '肖兔', '男', '17');
