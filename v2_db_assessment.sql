
/* creation of table user */
CREATE TABLE `db`.`User` (
  `idUser` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `gov_id` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `company` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `idUser_UNIQUE` (`idUser` ASC),
  UNIQUE INDEX `gov_id_UNIQUE` (`gov_id` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  UNIQUE INDEX `company_UNIQUE` (`company` ASC));

/* creation of table order */
CREATE TABLE `db`.`Order` (
  `idOrder` INT NOT NULL,
  `date` DATE NOT NULL,
  `total` DOUBLE NOT NULL,
  `subtotal` DOUBLE NOT NULL,
  `taxes` DOUBLE NOT NULL,
  `paid` DOUBLE NOT NULL,
  `id_user` INT NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `cost` INT NOT NULL,
  PRIMARY KEY (`idOrder`),
  INDEX `FK_user_id_idx` (`id_user` ASC),
  CONSTRAINT `FK_user_id`
    FOREIGN KEY (`id_user`)
    REFERENCES `db`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

/* creation of table payment */
CREATE TABLE `db`.`payment` (
  `idpayment` INT NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `txn_id` INT NOT NULL,
  `total` DOUBLE NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `id_order` INT NOT NULL,
  PRIMARY KEY (`idpayment`),
  UNIQUE INDEX `idpayment_UNIQUE` (`idpayment` ASC),
  INDEX `FK_order_id_idx` (`id_order` ASC),
  CONSTRAINT `FK_order_id`
    FOREIGN KEY (`id_order`)
    REFERENCES `db`.`Order` (`idOrder`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

/* creation of table shipping
CREATE TABLE `db`.`Shipping` (
  `idShipping` INT NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `cost` INT NOT NULL,
  UNIQUE INDEX `idShipping_UNIQUE` (`idShipping` ASC),
  CONSTRAINT `FK_orders_id`
    FOREIGN KEY (`idShipping`)
    REFERENCES `db`.`Order` (`idOrder`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
 */
