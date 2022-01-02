select * from author;
insert into author (first_name, last_name) values ("Ken", "Blanchard");
commit;
select count(distinct first_name) from author;
delete from author where id >= 4;

DROP TABLE account;
CREATE TABLE IF NOT EXISTS `account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` varchar(26) NOT NULL,
  `balance` decimal(20,2) NOT NULL,
  PRIMARY KEY (`id`)
);


DROP TABLE transaction;
CREATE TABLE IF NOT EXISTS `transaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account_id` int NOT NULL,
  `time` timestamp NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_tran_account` FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE
);

INSERT INTO account (`number`, balance)
VALUES ('15102010450000998000013422', 0);

INSERT INTO transaction (account_id, `time`, amount)
VALUES (1, '2022-01-01 10:10:01', 5);

UPDATE account
set balance = (SELECT SUM(amount) FROM transaction where account_id = 1)
WHERE id = 1;