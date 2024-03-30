/*
 Navicat Premium Data Transfer

 Source Server         : Huawei-Canteen
 Source Server Type    : MySQL
 Source Server Version : 80027 (8.0.27)
 Source Host           : 139.9.41.156:3305
 Source Schema         : canteen

 Target Server Type    : MySQL
 Target Server Version : 80027 (8.0.27)
 File Encoding         : 65001

 Date: 30/03/2024 22:54:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 73 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add notifications', 6, 'add_notifications');
INSERT INTO `auth_permission` VALUES (22, 'Can change notifications', 6, 'change_notifications');
INSERT INTO `auth_permission` VALUES (23, 'Can delete notifications', 6, 'delete_notifications');
INSERT INTO `auth_permission` VALUES (24, 'Can view notifications', 6, 'view_notifications');
INSERT INTO `auth_permission` VALUES (25, 'Can add payment', 7, 'add_payment');
INSERT INTO `auth_permission` VALUES (26, 'Can change payment', 7, 'change_payment');
INSERT INTO `auth_permission` VALUES (27, 'Can delete payment', 7, 'delete_payment');
INSERT INTO `auth_permission` VALUES (28, 'Can view payment', 7, 'view_payment');
INSERT INTO `auth_permission` VALUES (29, 'Can add promotions', 8, 'add_promotions');
INSERT INTO `auth_permission` VALUES (30, 'Can change promotions', 8, 'change_promotions');
INSERT INTO `auth_permission` VALUES (31, 'Can delete promotions', 8, 'delete_promotions');
INSERT INTO `auth_permission` VALUES (32, 'Can view promotions', 8, 'view_promotions');
INSERT INTO `auth_permission` VALUES (33, 'Can add dish', 9, 'add_dish');
INSERT INTO `auth_permission` VALUES (34, 'Can change dish', 9, 'change_dish');
INSERT INTO `auth_permission` VALUES (35, 'Can delete dish', 9, 'delete_dish');
INSERT INTO `auth_permission` VALUES (36, 'Can view dish', 9, 'view_dish');
INSERT INTO `auth_permission` VALUES (37, 'Can add order', 10, 'add_order');
INSERT INTO `auth_permission` VALUES (38, 'Can change order', 10, 'change_order');
INSERT INTO `auth_permission` VALUES (39, 'Can delete order', 10, 'delete_order');
INSERT INTO `auth_permission` VALUES (40, 'Can view order', 10, 'view_order');
INSERT INTO `auth_permission` VALUES (41, 'Can add shop', 11, 'add_shop');
INSERT INTO `auth_permission` VALUES (42, 'Can change shop', 11, 'change_shop');
INSERT INTO `auth_permission` VALUES (43, 'Can delete shop', 11, 'delete_shop');
INSERT INTO `auth_permission` VALUES (44, 'Can view shop', 11, 'view_shop');
INSERT INTO `auth_permission` VALUES (45, 'Can add order list', 12, 'add_orderlist');
INSERT INTO `auth_permission` VALUES (46, 'Can change order list', 12, 'change_orderlist');
INSERT INTO `auth_permission` VALUES (47, 'Can delete order list', 12, 'delete_orderlist');
INSERT INTO `auth_permission` VALUES (48, 'Can view order list', 12, 'view_orderlist');
INSERT INTO `auth_permission` VALUES (49, 'Can add employee', 13, 'add_employee');
INSERT INTO `auth_permission` VALUES (50, 'Can change employee', 13, 'change_employee');
INSERT INTO `auth_permission` VALUES (51, 'Can delete employee', 13, 'delete_employee');
INSERT INTO `auth_permission` VALUES (52, 'Can view employee', 13, 'view_employee');
INSERT INTO `auth_permission` VALUES (53, 'Can add user', 14, 'add_customer');
INSERT INTO `auth_permission` VALUES (54, 'Can change user', 14, 'change_customer');
INSERT INTO `auth_permission` VALUES (55, 'Can delete user', 14, 'delete_customer');
INSERT INTO `auth_permission` VALUES (56, 'Can view user', 14, 'view_customer');
INSERT INTO `auth_permission` VALUES (57, 'Can add paycard', 15, 'add_paycard');
INSERT INTO `auth_permission` VALUES (58, 'Can change paycard', 15, 'change_paycard');
INSERT INTO `auth_permission` VALUES (59, 'Can delete paycard', 15, 'delete_paycard');
INSERT INTO `auth_permission` VALUES (60, 'Can view paycard', 15, 'view_paycard');
INSERT INTO `auth_permission` VALUES (61, 'Can add don\'t send entry', 16, 'add_dontsendentry');
INSERT INTO `auth_permission` VALUES (62, 'Can change don\'t send entry', 16, 'change_dontsendentry');
INSERT INTO `auth_permission` VALUES (63, 'Can delete don\'t send entry', 16, 'delete_dontsendentry');
INSERT INTO `auth_permission` VALUES (64, 'Can view don\'t send entry', 16, 'view_dontsendentry');
INSERT INTO `auth_permission` VALUES (65, 'Can add message', 17, 'add_message');
INSERT INTO `auth_permission` VALUES (66, 'Can change message', 17, 'change_message');
INSERT INTO `auth_permission` VALUES (67, 'Can delete message', 17, 'delete_message');
INSERT INTO `auth_permission` VALUES (68, 'Can view message', 17, 'view_message');
INSERT INTO `auth_permission` VALUES (69, 'Can add message log', 18, 'add_messagelog');
INSERT INTO `auth_permission` VALUES (70, 'Can change message log', 18, 'change_messagelog');
INSERT INTO `auth_permission` VALUES (71, 'Can delete message log', 18, 'delete_messagelog');
INSERT INTO `auth_permission` VALUES (72, 'Can view message log', 18, 'view_messagelog');

-- ----------------------------
-- Table structure for comment_notifications
-- ----------------------------
DROP TABLE IF EXISTS `comment_notifications`;
CREATE TABLE `comment_notifications`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `noti_title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `noti_content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `noti_sendtime` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `cus_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `comment_notifications_cus_id_id_61fc182c_fk_customer_customer_id`(`cus_id_id` ASC) USING BTREE,
  CONSTRAINT `comment_notifications_cus_id_id_61fc182c_fk_customer_customer_id` FOREIGN KEY (`cus_id_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of comment_notifications
-- ----------------------------
INSERT INTO `comment_notifications` VALUES (1, '你好', '欢迎使用餐饮系统', '2024-03-27 07:32:19', 21);
INSERT INTO `comment_notifications` VALUES (2, '新春特惠！', '即日起进行支付卡储值，可享受5%额外储值金额！多充多送，欢迎参加！优惠码：HAPPYNEWYEAR2024', '2024-03-02 22:01:15', 21);

-- ----------------------------
-- Table structure for comment_payment
-- ----------------------------
DROP TABLE IF EXISTS `comment_payment`;
CREATE TABLE `comment_payment`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pay_num` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `pay_time` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `pay_money` decimal(10, 2) NOT NULL,
  `pay_way` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `ord_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `comment_payment_ord_id_id_81fa8053_fk_shop_order_id`(`ord_id_id` ASC) USING BTREE,
  CONSTRAINT `comment_payment_ord_id_id_81fa8053_fk_shop_order_id` FOREIGN KEY (`ord_id_id`) REFERENCES `shop_order` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of comment_payment
-- ----------------------------
INSERT INTO `comment_payment` VALUES (1, '1710916981yMAgkz8H', '2024-03-20 14:43:01', 18.00, '支付卡', 19);

-- ----------------------------
-- Table structure for comment_promotions
-- ----------------------------
DROP TABLE IF EXISTS `comment_promotions`;
CREATE TABLE `comment_promotions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `promo_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `promo_start` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `promo_end` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `promo_code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `promo_multiple` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `promo_code`(`promo_code` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of comment_promotions
-- ----------------------------
INSERT INTO `comment_promotions` VALUES (1, '新春优惠', '2024-02-09T16:00:00.000Z', '2025-02-25T16:00:00.000Z', 'HAPPYNEWYEAR2024', 1.05);
INSERT INTO `comment_promotions` VALUES (2, '清明优惠', '2024-04-04T16:00:00.000Z', '2024-04-06T16:00:00.000Z', 'QINGMING2024', 1.10);

-- ----------------------------
-- Table structure for customer_customer
-- ----------------------------
DROP TABLE IF EXISTS `customer_customer`;
CREATE TABLE `customer_customer`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `cus_tel` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  `cus_sex` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  `cus_birth` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  `cus_address` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  `usertype` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE,
  UNIQUE INDEX `email`(`email` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of customer_customer
-- ----------------------------
INSERT INTO `customer_customer` VALUES (1, 'pbkdf2_sha256$390000$Hthk5DkJqv6m0Hgqv6uUDN$mwAqqJm1VG7JfurC5zNEDsyxHp0+xYtLeDbQcmRHvNo=', '2024-03-28 01:05:43.128183', 1, 'SuperAdminForSystem', '', '', 'SuperAdmin@system.com', 1, 1, '2024-03-20 05:34:16.178958', '', NULL, NULL, NULL, 'super');
INSERT INTO `customer_customer` VALUES (21, 'pbkdf2_sha256$390000$HfDTh0JwPNOAwN6boj8xPJ$JiB5OcnPTGcpLStaciaW5n4zJyBMnrBS25j1WSaj5Pw=', '2024-03-29 06:29:26.198489', 0, '123', '耶耶', '', 'customer@system.com', 0, 1, '2024-02-23 12:25:12.405661', '13000000000', '女', '2024-03-24T16:00:00.000Z', '广东省广州市', 'customer');
INSERT INTO `customer_customer` VALUES (25, 'pbkdf2_sha256$390000$4ewRdN1l8Q0CtMzRHnyAt9$W28X0+QHEJX6yP+A/rU88A8pz/kyKWSPd+Dd/2aiSIc=', '2024-03-29 03:21:24.946777', 0, '456', '小凌', '', 'shop@system.com', 0, 1, '2024-02-29 14:58:26.372319', '18000000000', '男', '2024-02-26T16:00:00.000Z', '广东省深圳市', 'shop');
INSERT INTO `customer_customer` VALUES (26, 'pbkdf2_sha256$390000$Fy79B8Q9f68lhz4ZFAxFH8$513CASE+RFqh0/Myaex7USOOalEvSdUSKw8yIMVujR4=', '2024-03-29 03:16:26.948979', 0, '789', '小刘', '', 'admin@system.com', 0, 1, '2024-03-04 12:51:21.171361', '17300000000', '女', '2001-08-19T16:00:00.000Z', '河南省驻马店市', 'super');

-- ----------------------------
-- Table structure for customer_customer_groups
-- ----------------------------
DROP TABLE IF EXISTS `customer_customer_groups`;
CREATE TABLE `customer_customer_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `customer_customer_groups_customer_id_group_id_7b37e958_uniq`(`customer_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `customer_customer_groups_group_id_a005825a_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `customer_customer_gr_customer_id_cc388c92_fk_customer_` FOREIGN KEY (`customer_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `customer_customer_groups_group_id_a005825a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of customer_customer_groups
-- ----------------------------

-- ----------------------------
-- Table structure for customer_customer_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `customer_customer_user_permissions`;
CREATE TABLE `customer_customer_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `customer_customer_user_p_customer_id_permission_i_d54c5202_uniq`(`customer_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `customer_customer_us_permission_id_b5679413_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `customer_customer_us_customer_id_0dffe549_fk_customer_` FOREIGN KEY (`customer_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `customer_customer_us_permission_id_b5679413_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of customer_customer_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for customer_paycard
-- ----------------------------
DROP TABLE IF EXISTS `customer_paycard`;
CREATE TABLE `customer_paycard`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `card_number` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `card_condition` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `cus_id_id` bigint NOT NULL,
  `card_balance` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `cus_id_id`(`cus_id_id` ASC) USING BTREE,
  CONSTRAINT `customer_paycard_cus_id_id_feb3fb64_fk_customer_customer_id` FOREIGN KEY (`cus_id_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of customer_paycard
-- ----------------------------
INSERT INTO `customer_paycard` VALUES (1, '1709382600y85tov', '已激活', 21, 10.00);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_customer_customer_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_customer_customer_id` FOREIGN KEY (`user_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (6, 'comment', 'notifications');
INSERT INTO `django_content_type` VALUES (7, 'comment', 'payment');
INSERT INTO `django_content_type` VALUES (8, 'comment', 'promotions');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (14, 'customer', 'customer');
INSERT INTO `django_content_type` VALUES (15, 'customer', 'paycard');
INSERT INTO `django_content_type` VALUES (16, 'mailer', 'dontsendentry');
INSERT INTO `django_content_type` VALUES (17, 'mailer', 'message');
INSERT INTO `django_content_type` VALUES (18, 'mailer', 'messagelog');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (9, 'shop', 'dish');
INSERT INTO `django_content_type` VALUES (13, 'shop', 'employee');
INSERT INTO `django_content_type` VALUES (10, 'shop', 'order');
INSERT INTO `django_content_type` VALUES (12, 'shop', 'orderlist');
INSERT INTO `django_content_type` VALUES (11, 'shop', 'shop');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 39 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2023-10-24 15:05:04.565147');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2023-10-24 15:05:04.623171');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2023-10-24 15:05:04.813300');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2023-10-24 15:05:04.861304');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2023-10-24 15:05:04.869312');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2023-10-24 15:05:04.878320');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2023-10-24 15:05:04.887353');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2023-10-24 15:05:04.892338');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2023-10-24 15:05:04.900342');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2023-10-24 15:05:04.908342');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2023-10-24 15:05:04.915343');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2023-10-24 15:05:04.931355');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2023-10-24 15:05:04.947400');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2023-10-24 15:05:04.955410');
INSERT INTO `django_migrations` VALUES (15, 'customer', '0001_initial', '2023-10-24 15:05:05.238598');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0001_initial', '2023-10-24 15:05:05.343651');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2023-10-24 15:05:05.354652');
INSERT INTO `django_migrations` VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-24 15:05:05.363662');
INSERT INTO `django_migrations` VALUES (19, 'shop', '0001_initial', '2023-10-24 15:05:05.770848');
INSERT INTO `django_migrations` VALUES (20, 'comment', '0001_initial', '2023-10-24 15:05:05.811869');
INSERT INTO `django_migrations` VALUES (21, 'comment', '0002_initial', '2023-10-24 15:05:05.948928');
INSERT INTO `django_migrations` VALUES (22, 'sessions', '0001_initial', '2023-10-24 15:05:05.980928');
INSERT INTO `django_migrations` VALUES (23, 'customer', '0002_remove_paycard_ord_number_paycard_card_balance', '2023-11-20 09:03:18.021517');
INSERT INTO `django_migrations` VALUES (24, 'customer', '0003_alter_paycard_card_condition', '2023-11-20 09:16:53.629245');
INSERT INTO `django_migrations` VALUES (25, 'shop', '0002_rename_ord_customer_order_cus_id', '2023-11-20 12:18:29.923132');
INSERT INTO `django_migrations` VALUES (26, 'shop', '0003_rename_emp_conditon_employee_emp_condition', '2023-11-24 13:46:27.538901');
INSERT INTO `django_migrations` VALUES (27, 'customer', '0004_customer_usertype', '2023-12-03 12:38:59.932397');
INSERT INTO `django_migrations` VALUES (28, 'comment', '0003_remove_promotions_promo_des_and_more', '2023-12-04 14:24:07.872457');
INSERT INTO `django_migrations` VALUES (29, 'customer', '0005_alter_paycard_card_condition', '2023-12-13 09:29:05.812365');
INSERT INTO `django_migrations` VALUES (30, 'mailer', '0001_initial', '2024-01-11 13:44:00.053431');
INSERT INTO `django_migrations` VALUES (31, 'mailer', '0002_auto_20150720_1433', '2024-01-11 13:44:00.063516');
INSERT INTO `django_migrations` VALUES (32, 'mailer', '0003_messagelog_message_id', '2024-01-11 13:44:00.078530');
INSERT INTO `django_migrations` VALUES (33, 'mailer', '0004_auto_20190920_1512', '2024-01-11 13:44:00.283986');
INSERT INTO `django_migrations` VALUES (34, 'mailer', '0005_id_bigautofield', '2024-01-11 13:44:00.378540');
INSERT INTO `django_migrations` VALUES (35, 'shop', '0004_shop_shop_cus', '2024-03-11 12:48:16.425008');
INSERT INTO `django_migrations` VALUES (36, 'shop', '0005_alter_shop_shop_cus', '2024-03-11 12:48:16.540575');
INSERT INTO `django_migrations` VALUES (37, 'shop', '0006_alter_shop_shop_cus', '2024-03-11 12:48:16.623602');
INSERT INTO `django_migrations` VALUES (38, 'shop', '0007_alter_dish_dish_shop', '2024-03-19 08:30:39.597589');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('2tbsx29aunngof87mxh5qb77entm8b2u', '.eJxVjMsOgjAUBf-la9NQ0La4dO83kPsUfFBDy8IY_11IWOj2zJx5mw7m0ndzlqkb2BxN7czud0Sgm4wr4SuMl2QpjWUa0K6K3Wi258RyP23uX6CH3C9vZOEatYrBHWJFEoKgV0_aOAGqAro2UOOCKkrLUaMnFvEe9h5QnC7RNVdeT1lqNOeSHjKZzxeKGkGm:1rg33w:_Bd1GRJLyY5omPNIZIQABlwZ0rznIxwF6Cs0ctEeMvM', '2024-03-15 13:36:32.035247');
INSERT INTO `django_session` VALUES ('5ifktlkgoig7fi6j7ureyo8q0t5fi005', 'eyIyNThiZjNjNjU3Mzk0NmYyODU4NTY2NzdjNjgwZWM3YSI6ImxhaW5zbyJ9:1rUjxN:xyIr_YcjZBzmueYN33zpAGrKqcR7r91lnAdD7Efuc1Q', '2024-02-13 08:59:01.714224');
INSERT INTO `django_session` VALUES ('6ddm6koi12od2ovidfzx41vkmof847wh', 'eyI1ZWI2N2VkNjRmMmM0MmRjODQ3ZTg4NDMwOTRmM2Q0MiI6IjMyMTIzMSJ9:1rPMuH:l5q7FFSQKNsma7o-QZBnZJh1wVhSW_fe2-AmrtzT88w', '2024-01-29 13:21:37.854447');
INSERT INTO `django_session` VALUES ('6to67lvh4jamvrh16tchuaz2za5y4rb8', '.eJxVjEEOwiAQRe_C2hBKKQwu3XuGZhgGWzVtU9qFMd5dSLrQ7X_vv7focd-Gfs-89mMUZ6GtOP2OAenBUyXxjtNtljRP2zoGWRV50Cyvc-Tn5XD_AgPmobzRIXQBnI6cFETvHVJQSaF1weimdQRMBlNjG0RS3gBp61tqXUcAyZRozW2vhUst7wuv4vMFibU-4g:1rncg2:JcDJ6PWaPoWy2xS_PnZ82Y749s4Uj0aThYtacxY_XU0', '2024-04-05 11:03:10.674929');
INSERT INTO `django_session` VALUES ('9u36yezw2pd77tp2bq7lcvq290xxlx6z', 'eyJhYzY0NzhmODExODg0YmE1OGFlZGNmZmRlYWVmOWUxOSI6ImxhaW5zbyJ9:1rUjuC:PdR13wWi6a3Sa6fzJJwCk-jBu-I0-Y8sW-WbexVNgH4', '2024-02-13 08:55:44.015873');
INSERT INTO `django_session` VALUES ('a2nevt2s2oqcacyxfvif6edd59awpadi', '.eJxVjMsOgjAUBf-la9NQ0La4dO83kPsUfFBDy8IY_11IWOj2zJx5mw7m0ndzlqkb2BxN7czud0Sgm4wr4SuMl2QpjWUa0K6K3Wi258RyP23uX6CH3C9vZOEatYrBHWJFEoKgV0_aOAGqAro2UOOCKkrLUaMnFvEe9h5QnC7RNVdeT1lqNOeSHjKZzxeKGkGm:1rmqmW:SDbWablca_TK7MRTpmTmG59C7V2MJiYVdjG1FgqN0SU', '2024-04-03 07:54:40.652916');
INSERT INTO `django_session` VALUES ('mmcujo04jbfgek5a8m1qo5zmlyo03cuk', '.eJxNzDtuAzEMBcC7qE5BSvz6NhRXDwgQJEXKIHe3O28_mL_h2adE_KKEnEW5ABGbu0LbusdjfNXn9-_P-BgFBHgyZ6iAYmfxWftabAjbcrfsyqcj3CNFmXdqlpAf9XJaerdER2nXykYKaSQsT2C27emT4m6Pm17QAKwFjIJcPRfp6xRKe9v_J0lOPMQ:1rUkCj:3lKq1zrgQBIsQwCoFoxxt1GUTLbSDwpao5sSFoJp_xw', '2024-02-13 09:14:53.158429');
INSERT INTO `django_session` VALUES ('py63z2uc4kilh8u2ro39daiuy7xlxqrz', '.eJxVjEEOwiAQRe_C2hBKKQwu3XuGZhgGWzVtU9qFMd5dSLrQ7X_vv7focd-Gfs-89mMUZ6GtOP2OAenBUyXxjtNtljRP2zoGWRV50Cyvc-Tn5XD_AgPmobzRIXQBnI6cFETvHVJQSaF1weimdQRMBlNjG0RS3gBp61tqXUcAyZRozW2vhUst7wuv4vMFibU-4g:1rp2GB:WHW82SoA3dAu39XpgmBQv6WAVXbwk4MHN_bBW-GHxMw', '2024-04-09 08:34:19.949733');
INSERT INTO `django_session` VALUES ('z16amh7gobg2yhfjurt519idosnfqbeh', '.eJxVjMsOgjAUBf-la9NQ0La4dO83kPsUfFBDy8IY_11IWOj2zJx5mw7m0ndzlqkb2BxN7czud0Sgm4wr4SuMl2QpjWUa0K6K3Wi258RyP23uX6CH3C9vZOEatYrBHWJFEoKgV0_aOAGqAro2UOOCKkrLUaMnFvEe9h5QnC7RNVdeT1lqNOeSHjKZzxeKGkGm:1rploM:GG5gNlHpmI-IW5jYf803bKT-DBY0x6NtXkmi-xdRgcc', '2024-04-11 09:12:38.149929');
INSERT INTO `django_session` VALUES ('zjha8oddn43n1vndlzf23r3w53a0s4kp', '.eJxVjMsOgjAUBf-la9NQ0La4dO83kPsUfFBDy8IY_11IWOj2zJx5mw7m0ndzlqkb2BxN7czud0Sgm4wr4SuMl2QpjWUa0K6K3Wi258RyP23uX6CH3C9vZOEatYrBHWJFEoKgV0_aOAGqAro2UOOCKkrLUaMnFvEe9h5QnC7RNVdeT1lqNOeSHjKZzxeKGkGm:1rplop:nbsT402W8QfGLnbtXJpzRa8CbRY7XBJPiNNPo32Xcxw', '2024-04-11 09:13:07.504405');

-- ----------------------------
-- Table structure for mailer_dontsendentry
-- ----------------------------
DROP TABLE IF EXISTS `mailer_dontsendentry`;
CREATE TABLE `mailer_dontsendentry`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `to_address` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `when_added` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mailer_dontsendentry
-- ----------------------------

-- ----------------------------
-- Table structure for mailer_message
-- ----------------------------
DROP TABLE IF EXISTS `mailer_message`;
CREATE TABLE `mailer_message`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `when_added` datetime(6) NOT NULL,
  `priority` smallint UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `mailer_message_priority_4f7b1370_check` CHECK (`priority` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mailer_message
-- ----------------------------

-- ----------------------------
-- Table structure for mailer_messagelog
-- ----------------------------
DROP TABLE IF EXISTS `mailer_messagelog`;
CREATE TABLE `mailer_messagelog`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `when_added` datetime(6) NOT NULL,
  `priority` smallint UNSIGNED NOT NULL,
  `when_attempted` datetime(6) NOT NULL,
  `result` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `log_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `message_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `mailer_messagelog_when_added_627461e6`(`when_added` ASC) USING BTREE,
  INDEX `mailer_messagelog_priority_5e712cf3`(`priority` ASC) USING BTREE,
  CONSTRAINT `mailer_messagelog_priority_5e712cf3_check` CHECK (`priority` >= 0)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mailer_messagelog
-- ----------------------------

-- ----------------------------
-- Table structure for shop_dish
-- ----------------------------
DROP TABLE IF EXISTS `shop_dish`;
CREATE TABLE `shop_dish`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dish_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `dish_des` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL,
  `dish_price` decimal(10, 2) NOT NULL,
  `dish_img` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NULL DEFAULT NULL,
  `dish_shop_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `shop_dish_dish_shop_id_2bd02c33_fk_shop_shop_id`(`dish_shop_id` ASC) USING BTREE,
  CONSTRAINT `shop_dish_dish_shop_id_2bd02c33_fk_shop_shop_id` FOREIGN KEY (`dish_shop_id`) REFERENCES `shop_shop` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of shop_dish
-- ----------------------------
INSERT INTO `shop_dish` VALUES (1, '大米饭', '香喷喷的大米饭', 3.00, 'https://th.bing.com/th?id=OSK.mmcola4URzVdDj_tFEHyDUJCxkrMv2WIpd8WOHnzex6QFrlo&w=130&h=100&c=8&o=6&dpr=1.3&pid=SANGAM', 1);
INSERT INTO `shop_dish` VALUES (2, '馄饨面', '鲜香可口', 15.00, 'https://www.bing.com/th?id=OIP._BDjyOoewkKkYbdTwhLX-gHaE8&w=216&h=150&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2', 1);

-- ----------------------------
-- Table structure for shop_employee
-- ----------------------------
DROP TABLE IF EXISTS `shop_employee`;
CREATE TABLE `shop_employee`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `emp_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `emp_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `emp_tel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `emp_condition` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `emp_role` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `emp_shop_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `shop_employee_emp_shop_id_be2d6446_fk_shop_shop_id`(`emp_shop_id` ASC) USING BTREE,
  CONSTRAINT `shop_employee_emp_shop_id_be2d6446_fk_shop_shop_id` FOREIGN KEY (`emp_shop_id`) REFERENCES `shop_shop` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of shop_employee
-- ----------------------------
INSERT INTO `shop_employee` VALUES (1, '小王', 'zk-002', '18022222222', '休假中', '店员', 1);
INSERT INTO `shop_employee` VALUES (2, '小李', 'zk-001', '18011111111', '值班中', '店长', 1);

-- ----------------------------
-- Table structure for shop_order
-- ----------------------------
DROP TABLE IF EXISTS `shop_order`;
CREATE TABLE `shop_order`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ord_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `ord_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `ord_condition` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `ord_money` decimal(10, 2) NOT NULL,
  `cus_id_id` bigint NOT NULL,
  `ord_shop_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ord_number`(`ord_number` ASC) USING BTREE,
  INDEX `shop_order_ord_shop_id_8fb167d8_fk_shop_shop_id`(`ord_shop_id` ASC) USING BTREE,
  INDEX `shop_order_cus_id_id_b6d11589_fk_customer_customer_id`(`cus_id_id` ASC) USING BTREE,
  CONSTRAINT `shop_order_cus_id_id_b6d11589_fk_customer_customer_id` FOREIGN KEY (`cus_id_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shop_order_ord_shop_id_8fb167d8_fk_shop_shop_id` FOREIGN KEY (`ord_shop_id`) REFERENCES `shop_shop` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of shop_order
-- ----------------------------
INSERT INTO `shop_order` VALUES (19, '1710916981ITVB6wM', '2024-03-20 14:43:01', '已完成', 18.00, 21, 1);

-- ----------------------------
-- Table structure for shop_orderlist
-- ----------------------------
DROP TABLE IF EXISTS `shop_orderlist`;
CREATE TABLE `shop_orderlist`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ordlist_num` int UNSIGNED NOT NULL,
  `dish_id` bigint NOT NULL,
  `ord_number_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `shop_orderlist_dish_id_2017a73a_fk_shop_dish_id`(`dish_id` ASC) USING BTREE,
  INDEX `shop_orderlist_ord_number_id_d642f065_fk_shop_order_ord_number`(`ord_number_id` ASC) USING BTREE,
  CONSTRAINT `shop_orderlist_dish_id_2017a73a_fk_shop_dish_id` FOREIGN KEY (`dish_id`) REFERENCES `shop_dish` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shop_orderlist_ord_number_id_d642f065_fk_shop_order_ord_number` FOREIGN KEY (`ord_number_id`) REFERENCES `shop_order` (`ord_number`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shop_orderlist_chk_1` CHECK (`ordlist_num` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of shop_orderlist
-- ----------------------------
INSERT INTO `shop_orderlist` VALUES (1, 1, 2, '1710916981ITVB6wM');
INSERT INTO `shop_orderlist` VALUES (2, 1, 1, '1710916981ITVB6wM');

-- ----------------------------
-- Table structure for shop_shop
-- ----------------------------
DROP TABLE IF EXISTS `shop_shop`;
CREATE TABLE `shop_shop`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `shop_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `shop_tel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `shop_head` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `shop_pass` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `shop_cus_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `shop_number`(`shop_number` ASC) USING BTREE,
  UNIQUE INDEX `shop_cus_id`(`shop_cus_id` ASC) USING BTREE,
  UNIQUE INDEX `shop_pass`(`shop_pass` ASC) USING BTREE,
  CONSTRAINT `shop_shop_shop_cus_id_80168578_fk_customer_customer_id` FOREIGN KEY (`shop_cus_id`) REFERENCES `customer_customer` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_520_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of shop_shop
-- ----------------------------
INSERT INTO `shop_shop` VALUES (1, '仲恺饭店', '1710162404wvLDtlpqU', '18011111111', '小李', 'zk666', 25);

SET FOREIGN_KEY_CHECKS = 1;
