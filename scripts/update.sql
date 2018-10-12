ALTER TABLE `evaluation_data`
ADD COLUMN `direction_type`  int NULL COMMENT '多空类型' AFTER `postion_time_str`;