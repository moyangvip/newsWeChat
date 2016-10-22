create database WeChatDB default character set 'utf8' collate 'utf8_general_ci';

use WeChatDB;

create table ContentInfo
(
	id  int(5) NOT NULL primary key auto_increment,
	contentMsg  varchar(255),	#内容			
	weight  int unsigned,	#权值
	valid int(1) DEFAULT 1,	#是否使用
    updateTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	UNIQUE KEY `msgIndex` (`contentMsg`)		
)engine=InnoDB default charset=utf8;

insert into ContentInfo(contentMsg,weight) values("呵呵",10);
insert into ContentInfo(contentMsg,weight) values("啊？",10);
insert into ContentInfo(contentMsg,weight) values("嗯啊",15);
insert into ContentInfo(contentMsg,weight) values("......",13);
insert into ContentInfo(contentMsg,weight) values("哦好",5);
insert into ContentInfo(contentMsg,weight) values("然后？",5);
insert into ContentInfo(contentMsg,weight) values("?",12);
insert into ContentInfo(contentMsg,weight) values("好吧",7);
insert into ContentInfo(contentMsg,weight) values("do not talk to me",5);
insert into ContentInfo(contentMsg,weight) values("你猜呢~",3);
insert into ContentInfo(contentMsg,weight) values("那我就没什么好说的了",2);
insert into ContentInfo(contentMsg,weight) values("厉害",8);


create table KeyInfo
(
	id  int(5) NOT NULL primary key auto_increment,
	keyWord varchar(100),	#关键字
	contentMsg text,	#回复内容
	valid int(1) DEFAULT 1,	#是否使用
    updateTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	UNIQUE KEY `keyIndex` (`keyWord`)
)engine=InnoDB default charset=utf8;

insert into KeyInfo(keyWord,contentMsg) values("天气","今天天气不错，东风转西南北风");
insert into KeyInfo(keyWord,contentMsg) values("笑话","一位记者要去南极访问100只企鹅。他就问第一只企鹅他平时的兴趣是什么。第一只企鹅说：吃饭、睡觉、打豆豆。记者疑惑的问说什么是打豆豆啊？那只企鹅没说什么就走了。那位记者想：好吧，不讲就不讲。他又访问第二只企鹅它平时的兴趣是什么。第二只企鹅说：吃饭、睡觉、打豆豆。怎麼又是打豆豆？记者在心里嘀咕着。接二连三的从访问第一只企鹅到第99只企鹅它们平时的兴趣都是“吃饭、睡觉、打豆豆”。直到第100只企鹅。记者问他说你平时的兴趣是什么？ 第100只企鹅：吃饭、睡觉。 记者觉得很奇怪，便问它：“你怎么不打豆豆呢？” 第100只企鹅：“因为我就是豆豆啊。”");
insert into KeyInfo(keyWord,contentMsg) values("帮助","1、请输入\"新闻\"获取所有最新新闻列表\n2、请输入具体网站名(如\"猎云网\")获取该站点最新新闻列表\n3、输入具体新闻编号获得详细资讯\n");

create table NewsInfo
(
	id  int(5) NOT NULL primary key auto_increment,	#新闻id
	webName varchar(20),	#网站名
	sectionName varchar(20),	#版块名
	newsUrl  varchar(255),	#链接地址
	newsTitle varchar(255),	#标题
	newsSummary  text,	#摘要
	valid int(1) DEFAULT 1,	#是否使用
    updateTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	UNIQUE KEY `titleIndex` (`newsTitle`)
)engine=InnoDB default charset=utf8;


