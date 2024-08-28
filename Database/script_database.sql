-- MySQL Script generated by MySQL Workbench
-- Wed Aug 28 21:23:06 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema PAC-MAN
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema PAC-MAN
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PAC-MAN` DEFAULT CHARACTER SET utf8 ;
USE `PAC-MAN` ;

-- -----------------------------------------------------
-- Table `PAC-MAN`.`results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PAC-MAN`.`results` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nickname` VARCHAR(15) NOT NULL,
  `score` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
