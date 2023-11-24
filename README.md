# scrapymovie
抓取链家的数据


1.遇到的坑   describe 加上``，不然写入一直报错describe是mysql关键字。
2.item和pipeline的关系。
3.抓取翻页的问题。

数据库表设计：
CREATE TABLE `movie`.`movie`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `describe` varchar(255) CHARACTER SET gbk COLLATE gbk_bin NOT NULL,
  `price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `m3` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `floor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `arear` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

