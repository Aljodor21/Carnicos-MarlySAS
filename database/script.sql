-- Active: 1686698273021@@127.0.0.1@3306

CREATE DATABASE chorizoquibdo;

USE chorizoquibdo;

CREATE TABLE
    `chorizoquibdo`.`usuarios` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `login` VARCHAR(45) NOT NULL,
        `password` VARCHAR(45) NOT NULL,
        `nombre` VARCHAR(45) NOT NULL,
        `direccion` VARCHAR(45) NOT NULL,
        `email` VARCHAR(60) NOT NULL,
        `tipo` BIT(1) NOT NULL,
        PRIMARY KEY (`id`)
    );

CREATE TABLE `chorizoquibdo`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad` INT NOT NULL,
  `preciou` DECIMAL NOT NULL,
  `code` INT NOT NULL,
  PRIMARY KEY (`id`));

INSERT INTO `chorizoquibdo`.`productos` (`id`, `nombre`, `cantidad`, `preciou`, `code`) VALUES ('1', 'Chorizos de cerdo', '10', '200', '1');

INSERT INTO `chorizoquibdo`.`productos` (`id`, `nombre`, `cantidad`, `preciou`, `code`) VALUES ('2', 'Butifarra ahumada', '5', '300', '2');

INSERT INTO `chorizoquibdo`.`productos` (`id`, `nombre`, `cantidad`, `preciou`, `code`) VALUES ('3', 'Carnes pulpas', '8', '400', '3');