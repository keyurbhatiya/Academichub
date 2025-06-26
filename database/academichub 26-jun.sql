-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2025 at 11:19 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `academichub`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add project', 7, 'add_project'),
(26, 'Can change project', 7, 'change_project'),
(27, 'Can delete project', 7, 'delete_project'),
(28, 'Can view project', 7, 'view_project'),
(29, 'Can add old paper', 8, 'add_oldpaper'),
(30, 'Can change old paper', 8, 'change_oldpaper'),
(31, 'Can delete old paper', 8, 'delete_oldpaper'),
(32, 'Can view old paper', 8, 'view_oldpaper'),
(33, 'Can add blog', 9, 'add_blog'),
(34, 'Can change blog', 9, 'change_blog'),
(35, 'Can delete blog', 9, 'delete_blog'),
(36, 'Can view blog', 9, 'view_blog');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$jwtrTBygcnkub7XQyp82lG$allgouwb8yOIE8qkm/qHGSPuQR5tFSdv9orjmv/wnVk=', '2025-06-26 09:17:48.644343', 1, 'keyur', '', '', 'keyur@admin.com', 1, 1, '2025-06-17 17:55:23.086154'),
(2, 'pbkdf2_sha256$600000$7aQF8zsYTiyNzvoeVY6iSh$5UZwWkor+8TzHwwhRqM5/aXo2MKTaRdQuBTlDvFqYEw=', '2025-06-26 09:18:33.643229', 0, 'user1', '', '', 'user@example.com', 0, 1, '2025-06-17 18:01:56.104546'),
(3, 'pbkdf2_sha256$600000$kgRqwO8PJJKF94Dq7JzSVi$nHv03q6hQaMRzjyx0j6JWPGHpZXktAuYQWluT6YGLBo=', '2025-06-22 06:48:01.520222', 0, 'Yash', '', '', 'yash@gmail.com', 0, 1, '2025-06-22 04:57:26.000059'),
(4, 'pbkdf2_sha256$600000$Vuw3krCcHLyPdEDWXi3fKj$qh/7+wehmGzbiBBbZe8c3YDTK/FaZs/9fe5wh/fMz7E=', '2025-06-26 08:23:00.494371', 0, 'Jay', '', '', 'jay123@gmail.com', 0, 1, '2025-06-22 07:06:29.907321');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_blog`
--

CREATE TABLE `core_blog` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `author_id` int(11) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_blog`
--

INSERT INTO `core_blog` (`id`, `title`, `content`, `created_at`, `author_id`, `status`) VALUES
(1, 'Testing a blog Title', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus eum aut, illo culpa repudiandae eius voluptatum eos vitae eveniet esse quam? Sit reprehenderit sunt numquam fuga exercitationem autem obcaecati laborum!', '2025-06-17 18:06:16.525266', 2, 'Pending'),
(2, 'Testing', 'Djhdgdvdhvd gutter yaar udgeygeusvs gh dchsbs', '2025-06-22 04:58:55.453921', 3, 'Pending'),
(3, 'Testing blog', 'Yash bhatiya yash bhatiya yash bhatiya', '2025-06-22 07:08:54.896946', 4, 'Rejected');

-- --------------------------------------------------------

--
-- Table structure for table `core_oldpaper`
--

CREATE TABLE `core_oldpaper` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `university` varchar(100) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `uploaded_by_id` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  `course` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_oldpaper`
--

INSERT INTO `core_oldpaper` (`id`, `title`, `university`, `semester`, `file`, `uploaded_at`, `uploaded_by_id`, `status`, `course`) VALUES
(1, 'Python', 'Gujarat-technological-university', '2', 'papers/629403_Programming_in_Python__NOV-2024.pdf', '2025-06-17 18:03:20.530856', 2, 'Pending', 'MCA'),
(2, 'Data Structure', 'Gujarat-technological-university', '2', 'papers/629401-SUMMER-2023.pdf', '2025-06-25 13:09:09.520269', 2, 'Pending', 'MCA'),
(3, 'Java', 'HNGU', '1', 'papers/JAVA__MAY_2024.pdf', '2025-06-25 13:55:24.023465', 2, 'Pending', 'MCA');

-- --------------------------------------------------------

--
-- Table structure for table `core_project`
--

CREATE TABLE `core_project` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `semester` varchar(50) NOT NULL,
  `zip_file` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `uploaded_by_id` int(11) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_project`
--

INSERT INTO `core_project` (`id`, `title`, `description`, `semester`, `zip_file`, `uploaded_at`, `uploaded_by_id`, `status`) VALUES
(1, 'demo template', 'Testing', '2', 'projects/demo_tempalete.zip', '2025-06-17 18:05:00.191260', 2, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'core', 'blog'),
(8, 'core', 'oldpaper'),
(7, 'core', 'project'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-17 17:50:36.673154'),
(2, 'auth', '0001_initial', '2025-06-17 17:50:36.978052'),
(3, 'admin', '0001_initial', '2025-06-17 17:50:37.061873'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-06-17 17:50:37.067959'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-17 17:50:37.074028'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-06-17 17:50:37.127119'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-06-17 17:50:37.166453'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-06-17 17:50:37.176927'),
(9, 'auth', '0004_alter_user_username_opts', '2025-06-17 17:50:37.186147'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-06-17 17:50:37.222556'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-06-17 17:50:37.225560'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-06-17 17:50:37.231624'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-06-17 17:50:37.242049'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-06-17 17:50:37.255586'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-06-17 17:50:37.264644'),
(16, 'auth', '0011_update_proxy_permissions', '2025-06-17 17:50:37.272640'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-06-17 17:50:37.282938'),
(18, 'core', '0001_initial', '2025-06-17 17:50:37.414123'),
(19, 'sessions', '0001_initial', '2025-06-17 17:50:37.438123'),
(20, 'core', '0002_blog_status_oldpaper_status_project_status', '2025-06-21 12:00:06.141440'),
(21, 'core', '0003_oldpaper_course', '2025-06-25 13:01:48.382213');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2jti6zglhwh4p7rrjgtst5nsubvoeosb', '.eJxVjEEOwiAQRe_C2hCmHaC4dO8ZCAyMVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRZoDj9bjHQI9cdpHuotyap1XWZo9wVedAury3l5-Vw_w5K6OVbA4yaGMBpgkmrEBFjys6OkMCitTAQs3LIEZ2aGA1al7WxhGwUjYN4fwDCeDbu:1uTEnF:WO1aSOCT1a8BZpzGcDmhmvpesON3G-mofdInxyCXnqM', '2025-07-06 07:07:09.855492'),
('zabk9faj3xlgpexoa4140f776vcp005v', 'e30:1uSr8e:C_nykviZNrk084_RZvEBQZRz-W3vg8XIYDzJNdUR0To', '2025-07-05 05:51:40.127638');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `core_blog`
--
ALTER TABLE `core_blog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_blog_author_id_1575e3e5_fk_auth_user_id` (`author_id`);

--
-- Indexes for table `core_oldpaper`
--
ALTER TABLE `core_oldpaper`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_oldpaper_uploaded_by_id_f1c70608_fk_auth_user_id` (`uploaded_by_id`);

--
-- Indexes for table `core_project`
--
ALTER TABLE `core_project`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_project_uploaded_by_id_64ee3153_fk_auth_user_id` (`uploaded_by_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_blog`
--
ALTER TABLE `core_blog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `core_oldpaper`
--
ALTER TABLE `core_oldpaper`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `core_project`
--
ALTER TABLE `core_project`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `core_blog`
--
ALTER TABLE `core_blog`
  ADD CONSTRAINT `core_blog_author_id_1575e3e5_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `core_oldpaper`
--
ALTER TABLE `core_oldpaper`
  ADD CONSTRAINT `core_oldpaper_uploaded_by_id_f1c70608_fk_auth_user_id` FOREIGN KEY (`uploaded_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `core_project`
--
ALTER TABLE `core_project`
  ADD CONSTRAINT `core_project_uploaded_by_id_64ee3153_fk_auth_user_id` FOREIGN KEY (`uploaded_by_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
