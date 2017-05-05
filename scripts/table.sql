ALTER TABLE `evaluation_data`
ADD COLUMN `volume`  int NULL COMMENT '交易量',
ADD COLUMN `position_time_str`  varchar(100) NULL;