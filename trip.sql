-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 03, 2022 at 08:00 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `register`
--

-- --------------------------------------------------------

--
-- Table structure for table `trip`
--

CREATE TABLE `trip` (
  `id` int(100) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `semester` varchar(500) NOT NULL,
  `std_id` varchar(100) NOT NULL,
  `gender` varchar(1000) NOT NULL,
  `remarks` varchar(1000) NOT NULL,
  `timestamp` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trip`
--

INSERT INTO `trip` (`id`, `Name`, `Last_Name`, `contact`, `email`, `semester`, `std_id`, `gender`, `remarks`, `timestamp`) VALUES
(8, 'sam', 'sah', '98', 'sam@gmail.com', '5th semester', '12', '123', '123', '2022-01-24 16:37:48'),
(14, 'NTR', 'JR', '090909', 'ntr@gmail.com', 'Male', '0909', 'Male', 'interested to visit new place', '2022-01-24 18:50:40'),
(16, 'avi', 'npt', '98765432', 'avi@gmail.com', 'Male', '9898', 'Male', 'for moj garnyy', '2022-01-25 22:22:55'),
(17, 'Racema', 'oli', '456789', 'oliracema@gmail.com', 'Female', '174588', 'Female', 'Refereshment', '2022-01-25 22:38:18'),
(18, 'sushant', 'yadav', '45678', 'sushant@gmail.com', 'Male', '3456', 'Male', 'for enjoyment', '2022-01-26 06:43:04'),
(19, 'ram', 'nt', '987654', 'ram@gmail.com', 'Male', '8765', 'Male', 'for enjoyment', '2022-01-26 07:09:56'),
(20, 'Bibek', 'sah', '987654321', 'bibeksah@gmail.com', 'Male', '175466', 'Male', 'for the refereshment', '2022-01-26 10:27:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `trip`
--
ALTER TABLE `trip`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `trip`
--
ALTER TABLE `trip`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
