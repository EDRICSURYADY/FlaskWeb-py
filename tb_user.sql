-- phpMyAdmin SQL Dump
-- version 4.5.0.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 16, 2022 at 06:09 PM
-- Server version: 10.0.17-MariaDB
-- PHP Version: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_pdip`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_user`
--

CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`id`, `username`, `email`, `password`) VALUES
(1, 'edricsuryady', 'EDRICSURYADY@GMAIL.COM', 'pbkdf2:sha256:260000$TmLA39ZKwx93q4Ty$8754ab16f383d2973a5f3d74793ad2d517b4cb1d9d96a175c5e3d789166aa894'),
(2, 'silvia', 'silvia@gmail.com', 'pbkdf2:sha256:260000$6Rx6dqvlYqpwxeey$def8780b55cb96dec907a892fdac0534d57d7a75e29dab5aa10d2176a9069342'),
(3, 'malvin', 'malvin@gmail.com', 'pbkdf2:sha256:260000$40fFf7t5fc1RQwu0$26119dd8f4df8a54975ffc6776e648ac3c26413bd721655607a421fe1b02e596'),
(4, 'agustina', 'agustina@gmail.com', 'pbkdf2:sha256:260000$4c9TaXTcYOSW3Jqi$1e274fdfad16e9734918284b889a07586686576cc177c36a78bb5d6a185fd488'),
(5, 'admin', 'admin@gmail.com', 'pbkdf2:sha256:260000$K4yw8J9bhFOb1fH8$469f97c627d68c43db617b14299d7c90410e839e1659a16f47cd37ba3a8e956b');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
