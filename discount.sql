USE TTTS;

INSERT INTO storeApp_discount VALUES(1,500,now(),"2019-03-31","冬季特賣");
INSERT INTO storeApp_seasoningdiscount VALUES(1);

INSERT INTO storeApp_discount VALUES(2,0,now(),"2019-03-31","滿額免運費");
INSERT INTO storeApp_shippingdiscount VALUES(2,499);

INSERT INTO storeApp_discount VALUES(3,50,now(),"2019-03-31","紅茶好喝");
INSERT INTO storeApp_productdiscount VALUES(3,1);