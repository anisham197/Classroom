-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 16, 2017 at 11:05 PM
-- Server version: 5.7.17-0ubuntu0.16.04.1
-- PHP Version: 7.0.15-0ubuntu0.16.04.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Classroom`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `usn` varchar(255) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `user_id`, `name`, `usn`, `branch`, `email`) VALUES
(1, 4, 'Anisha Mascarenhas', '1MS14IS013', 'ISE', 'anisham197@gmail.com'),
(4, 7, 'Amisha', '1MS14IS004', 'ISE', 'amisha@gmail.com'),
(5, 8, 'Arjun', '1MS14IS018', 'ISE', 'mailarjunrao@gmail.com'),
(6, 9, 'Ivy', '1MS14IS009', 'ISE', 'joanivy303@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(4, 'anisha', '$6$rounds=656000$SDtj1scfr/4bFuNM$ciCC7f2sZnOooOiWhuqcyAr6i1q5EDYPx54y3tLC8g3YmGUL86g/RgW8st4Rl48I/opk27/j12LHtikv1ADxP/', 1),
(7, 'amisha29', '$6$rounds=656000$eE9UEcCFrPTnbOTM$b9yQ5PV.smyAOHCmAhBxz9T9FJUsHtycNArY9YNuxQsPa7auxY2lBfhzuITGnIM2rU/6cJM2GtzEwDY/uOCxm.', 1),
(8, 'arjun-rao', '$6$rounds=656000$ias6DQlknqGBBzlb$8E6QpajZn8BRn9NluIugCw2.qY4UKqMDOxFo.6V450cRQht76/LTR98SSZ0l9bhoKQcuDtWFV1Z7ROeB4iMO01', 1),
(9, 'joanivy', '$6$rounds=656000$06UHN9fADldFKENO$jeQDJkfTJ76vmbK7AWBs8KRYvWUl5jKXIIV/BRHEzRI1nDI9LG.YvqxytZ23yQhIx3TClGxp3FwkImrN1qr5n0', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `usn` (`usn`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UNIQUE` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
