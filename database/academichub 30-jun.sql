-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2025 at 06:40 PM
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
(36, 'Can view blog', 9, 'view_blog'),
(37, 'Can add site settings', 10, 'add_sitesettings'),
(38, 'Can change site settings', 10, 'change_sitesettings'),
(39, 'Can delete site settings', 10, 'delete_sitesettings'),
(40, 'Can view site settings', 10, 'view_sitesettings');

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
(1, 'pbkdf2_sha256$600000$jwtrTBygcnkub7XQyp82lG$allgouwb8yOIE8qkm/qHGSPuQR5tFSdv9orjmv/wnVk=', '2025-06-30 05:50:30.112233', 1, 'keyur', '', '', 'keyur@admin.com', 1, 1, '2025-06-17 17:55:23.086154'),
(2, 'pbkdf2_sha256$600000$7aQF8zsYTiyNzvoeVY6iSh$5UZwWkor+8TzHwwhRqM5/aXo2MKTaRdQuBTlDvFqYEw=', '2025-06-27 10:14:41.727136', 0, 'user1', '', '', 'user@example.com', 0, 1, '2025-06-17 18:01:56.104546'),
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
  `status` varchar(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `uploaded_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_blog`
--

INSERT INTO `core_blog` (`id`, `title`, `content`, `created_at`, `author_id`, `status`, `image`, `uploaded_by_id`) VALUES
(1, 'Testing a blog Title', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus eum aut, illo culpa repudiandae eius voluptatum eos vitae eveniet esse quam? Sit reprehenderit sunt numquam fuga exercitationem autem obcaecati laborum!', '2025-06-17 18:06:16.525266', 2, 'Pending', NULL, NULL),
(2, 'Testing', 'Djhdgdvdhvd gutter yaar udgeygeusvs gh dchsbs', '2025-06-22 04:58:55.453921', 3, 'Pending', NULL, NULL),
(3, 'Testing blog', 'Yash bhatiya yash bhatiya yash bhatiya', '2025-06-22 07:08:54.896946', 4, 'Rejected', NULL, NULL),
(4, 'Sail into summer with books kids love', '<p>Summer is in full swing, bringing sunny days and plenty of time to get lost in a good book! We’ve put together a vibrant selection of stories that will keep kids entertained and learning all season long. To make reading even more fun, we’ve included some Education.com worksheets that encourage creativity and help kids stay focused while keeping their skills sharp.</p><p>This summer reading list was created in partnership with our sister site&nbsp;<a href=\"http://vocabulary.com/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Vocabulary.com</a>, where you can find word lists that perfectly complement each book and support vocabulary growth.</p><h2><strong>Education.com reading resources</strong></h2><p><a href=\"https://www.education.com/worksheet/article/have-fun-reading-choice-board/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Have Fun Reading: Choice Board</a>&nbsp;– PreK-2</p><p>From building blanket forts to acting out story moments, these reading activities make early literacy feel like playtime.</p><p><a href=\"https://www.education.com/worksheet/article/what-is-a-narrative-key-features/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Complete the Table: Narrative Elements</a>&nbsp;– Grade 2-5</p><p>Help kids build stronger reading comprehension skills by exploring key story elements like setting, characters, and plot through a fun and interactive matching activity.</p><p><a href=\"https://www.education.com/worksheet/article/compare-and-contrast-written-vs-audio-visual-forms-of-a-text/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Compare and Contrast Written vs. Audio/Visual Forms of a Text</a>&nbsp;– Grade 6-7</p><p>Get middle schoolers thinking critically with a graphic organizer that guides them in comparing what they read to what they see and hear in an audio or visual version of the same text.</p><p><a href=\"https://www.education.com/worksheet/article/analyzing-an-adaptation-book-vs-movie/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Analyzing an Adaptation: Book vs. Movie</a>&nbsp;– Grade 8</p><p>Is the book always better? Let learners decide with this activity that helps them compare a story on the page to its big-screen adaptation.</p><h2><strong>Summer book list</strong></h2><h3><strong>Books for young readers</strong></h3><p><a href=\"https://www.vocabulary.com/lists/in52ky3q/amari-and-the-night-brothers\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Amari and the Night Brothers</em></a>: Amari Peters is thrust into a world of magic and mystery as she competes for a spot at the Bureau of Supernatural Affairs while trying to uncover the truth behind her brother’s sudden disappearance.</p><p><a href=\"https://www.vocabulary.com/lists/ovtziqzg/lawn-boy\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Lawn Boy</em></a><em>:&nbsp;</em>On his 12th birthday, the narrator receives an old lawnmower and shares the story of an eventful summer spent mowing neighbors’ lawns and discovering the spirit of entrepreneurship.</p><p><a href=\"https://www.vocabulary.com/lists/d2q2zaqr/witchlings\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Witchlings</em></a><em>:&nbsp;</em>Twelve-year-old Seven Salazar of Ravenskill must team up with the bully Valley Pepperhorn and the new girl Thorn Laroux to defeat the Nightbeast and protect their coven, preserve their magic, and avoid being turned into toads.</p><h3><strong>Books for advanced readers</strong></h3><p><a href=\"https://www.vocabulary.com/lists/gn7gcdmm/ballad-of-songbirds-and-snakes\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>The Ballad of Songbirds and Snakes</em></a>: Dive into the prequel to the Hunger Games trilogy, where a young Coriolanus Snow mentors a tribute during the 10th Hunger Games.</p><p><a href=\"https://www.vocabulary.com/lists/c6vahplc/prairie-lotus\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Prairie Lotus</em></a><em>:&nbsp;</em>Set in 1880, this historical novel follows Hanna, a young girl of Chinese descent, as she navigates life in the Dakota Territory and faces the challenges of discrimination in her new town.</p><p><a href=\"https://www.vocabulary.com/lists/d23lnf6e/lost-year\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>The Lost Year</em></a><em>:&nbsp;</em>While stuck at home in New Jersey during the Covid pandemic, thirteen-year-old Matthew helps his hundred-year-old great-grandmother sort through her belongings and discovers her story as a Young Pioneer in 1930s Ukraine.</p>', '2025-06-27 09:19:35.296713', 1, 'Pending', '', 1),
(5, 'Sail into summer with books kids love', '<p>Summer is in full swing, bringing sunny days and plenty of time to get lost in a good book! We’ve put together a vibrant selection of stories that will keep kids entertained and learning all season long. To make reading even more fun, we’ve included some Education.com worksheets that encourage creativity and help kids stay focused while keeping their skills sharp.</p><p>This summer reading list was created in partnership with our sister site&nbsp;<a href=\"http://vocabulary.com/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Vocabulary.com</a>, where you can find word lists that perfectly complement each book and support vocabulary growth.</p><h2><strong>Education.com reading resources</strong></h2><p><a href=\"https://www.education.com/worksheet/article/have-fun-reading-choice-board/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Have Fun Reading: Choice Board</a>&nbsp;– PreK-2</p><p>From building blanket forts to acting out story moments, these reading activities make early literacy feel like playtime.</p><p><a href=\"https://www.education.com/worksheet/article/what-is-a-narrative-key-features/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Complete the Table: Narrative Elements</a>&nbsp;– Grade 2-5</p><p>Help kids build stronger reading comprehension skills by exploring key story elements like setting, characters, and plot through a fun and interactive matching activity.</p><p><a href=\"https://www.education.com/worksheet/article/compare-and-contrast-written-vs-audio-visual-forms-of-a-text/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Compare and Contrast Written vs. Audio/Visual Forms of a Text</a>&nbsp;– Grade 6-7</p><p>Get middle schoolers thinking critically with a graphic organizer that guides them in comparing what they read to what they see and hear in an audio or visual version of the same text.</p><p><a href=\"https://www.education.com/worksheet/article/analyzing-an-adaptation-book-vs-movie/\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\">Analyzing an Adaptation: Book vs. Movie</a>&nbsp;– Grade 8</p><p>Is the book always better? Let learners decide with this activity that helps them compare a story on the page to its big-screen adaptation.</p><h2><strong>Summer book list</strong></h2><h3><strong>Books for young readers</strong></h3><p><a href=\"https://www.vocabulary.com/lists/in52ky3q/amari-and-the-night-brothers\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Amari and the Night Brothers</em></a>: Amari Peters is thrust into a world of magic and mystery as she competes for a spot at the Bureau of Supernatural Affairs while trying to uncover the truth behind her brother’s sudden disappearance.</p><p><a href=\"https://www.vocabulary.com/lists/ovtziqzg/lawn-boy\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Lawn Boy</em></a><em>:&nbsp;</em>On his 12th birthday, the narrator receives an old lawnmower and shares the story of an eventful summer spent mowing neighbors’ lawns and discovering the spirit of entrepreneurship.</p><p><a href=\"https://www.vocabulary.com/lists/d2q2zaqr/witchlings\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Witchlings</em></a><em>:&nbsp;</em>Twelve-year-old Seven Salazar of Ravenskill must team up with the bully Valley Pepperhorn and the new girl Thorn Laroux to defeat the Nightbeast and protect their coven, preserve their magic, and avoid being turned into toads.</p><h3><strong>Books for advanced readers</strong></h3><p><a href=\"https://www.vocabulary.com/lists/gn7gcdmm/ballad-of-songbirds-and-snakes\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>The Ballad of Songbirds and Snakes</em></a>: Dive into the prequel to the Hunger Games trilogy, where a young Coriolanus Snow mentors a tribute during the 10th Hunger Games.</p><p><a href=\"https://www.vocabulary.com/lists/c6vahplc/prairie-lotus\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>Prairie Lotus</em></a><em>:&nbsp;</em>Set in 1880, this historical novel follows Hanna, a young girl of Chinese descent, as she navigates life in the Dakota Territory and faces the challenges of discrimination in her new town.</p><p><a href=\"https://www.vocabulary.com/lists/d23lnf6e/lost-year\" target=\"_blank\" style=\"color: rgb(86, 114, 196);\"><em>The Lost Year</em></a><em>:&nbsp;</em>While stuck at home in New Jersey during the Covid pandemic, thirteen-year-old Matthew helps his hundred-year-old great-grandmother sort through her belongings and discovers her story as a Young Pioneer in 1930s Ukraine.</p>', '2025-06-27 09:23:55.924687', 1, 'Pending', 'blog_images/banner.jpg', 1),
(6, 'Comparing MCA and MSc IT: Selecting the Appropriate Career Path After BCA', '<p>Are you a recent Bachelor of Computer Applications (BCA) graduate, eager to take the next leap in your academic and professional journey? The decision between pursuing a Master of Computer Applications (MCA) or a Master of Science in Information Technology (MSc IT) can be both exciting and daunting. Let\'s explore the distinctive features of each option to help you make an informed choice.</p><p><br></p><p>Understanding the Choices:</p><p><br></p><p>MCA: Specialized Expertise for Industry Success</p><p><br></p><p>Concentration: Emphasizes practical skills with direct industry relevance.</p><p><br></p><p>Course of Study: Covers software development, database management, networking, and management concepts.</p><p>Duration: Typically a three-year program.</p><p><br></p><p>Professional Trajectory: Leads to careers in software engineering, system administration, network administration, and IT consulting.</p><p><br></p><p>Market Demand: Highly sought after, catering to specific skill sets and regional trends.</p><p><br></p><p>MSc IT: Comprehensive Understanding of IT Fundamentals</p><p><br></p><p>Concentration: Focuses on theoretical foundations, spanning computer science, mathematics, statistics, and research methodology.</p><p><br></p><p>Course of Study: Explores a wide array of subjects essential for IT professionals.</p><p><br></p><p>Duration: Generally a two-year program.</p><p><br></p><p>Professional Trajectory: Prepares for roles in research, academia, data analysis, and software development, with opportunities for specialization.</p><p><br></p><p>Market Demand: Valued for research-oriented positions and academic pursuits.</p><p><br></p><p>Making the Right Choice:</p><h3>The decision between MCA and MSc IT hinges on your career objectives and personal interests. Here are some factors to consider:</h3><p>1. Interest and Goals: If you\'re passionate about software development and eager to enter the industry swiftly, MCA might be the right fit. On the other hand, if you aspire to delve into research or academia, MSc IT offers a broader foundation.</p><p>2. Financial Considerations: Evaluate the cost of each program, considering the duration and potential return on investment in terms of future salaries and career advancement.</p><p>3. Local Job Market: Research the demand for MCA and MSc IT graduates in your area to align your choice with industry needs and opportunities.</p><p>4. Long-Term Prospects: Consider your aspirations beyond the master\'s degree. MCA could fast-track your entry into the workforce, while MSc IT might pave the way for advanced academic pursuits or specialized roles.</p><p>Pursuing MSc IT After BCA:</p><p>Yes, it\'s entirely possible to pursue an MSc in Information Technology after completing a BCA. Several institutions offer specialized MSc IT programs tailored for BCA graduates, providing a seamless transition to advanced studies.</p><p>Conclusion:</p><p>Both MCA and MSc IT offer promising career paths in the ever-evolving IT landscape. To make an informed decision, reflect on your career goals, assess the market demand, and consider the long-term implications. Engage with industry professionals, seek guidance from mentors, and conduct thorough research to chart your course toward success.</p><h3>#BCA #MCA #MScIT #CareerAdvice #ITIndustry #HigherEducation #CareerPath #DecisionMaking #FutureReady #Research #Academia #SoftwareDevelopment</h3>', '2025-06-27 10:17:29.509569', 2, 'Pending', '', 2),
(7, 'q2e3rwe4grthgrnf', 'eewewewf', '2025-06-29 07:56:10.837342', 1, 'Pending', '', 1);

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
(1, 'Python', 'GTU', '2', 'papers/629403_Programming_in_Python__NOV-2024.pdf', '2025-06-17 18:03:20.530856', 2, 'Pending', 'MCA'),
(2, 'Data Structure', 'GTU', '2', 'papers/629401-SUMMER-2023.pdf', '2025-06-25 13:09:09.520269', 2, 'Pending', 'MCA'),
(3, 'Java', 'HNGU', '1', 'papers/JAVA__MAY_2024.pdf', '2025-06-25 13:55:24.023465', 2, 'Pending', 'MCA'),
(4, 'Programming with C', 'GTU', '1', 'papers/MC01094011.pdf', '2025-06-29 11:15:49.839756', 1, 'Pending', 'MCA');

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
  `status` varchar(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `language` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_project`
--

INSERT INTO `core_project` (`id`, `title`, `description`, `semester`, `zip_file`, `uploaded_at`, `uploaded_by_id`, `status`, `image`, `language`) VALUES
(1, 'demo template', 'Testing', '2', 'projects/demo_tempalete.zip', '2025-06-17 18:05:00.191260', 2, 'Pending', NULL, 'other'),
(2, 'Academic hub', 'This is my first project ', '2', 'projects/pdf2docx.zip', '2025-06-27 17:13:01.740258', 1, 'Pending', 'project_images/Screenshot_2025-06-27_222315.png', 'Python');

-- --------------------------------------------------------

--
-- Table structure for table `core_sitesettings`
--

CREATE TABLE `core_sitesettings` (
  `id` bigint(20) NOT NULL,
  `website_name` varchar(100) NOT NULL,
  `contact_email` varchar(254) NOT NULL,
  `allow_registrations` tinyint(1) NOT NULL,
  `email_notifications` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_sitesettings`
--

INSERT INTO `core_sitesettings` (`id`, `website_name`, `contact_email`, `allow_registrations`, `email_notifications`) VALUES
(1, 'AcademicHub', 'admin@academichub.com', 1, 1);

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
(10, 'core', 'sitesettings'),
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
(21, 'core', '0003_oldpaper_course', '2025-06-25 13:01:48.382213'),
(22, 'core', '0004_blog_image_blog_uploaded_by_and_more', '2025-06-27 07:55:22.737008'),
(23, 'core', '0005_project_image_project_language_and_more', '2025-06-27 12:13:39.366565'),
(24, 'core', '0006_sitesettings_alter_oldpaper_course_and_more', '2025-06-30 06:13:24.521481');

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
  ADD KEY `fk_uploaded_by` (`author_id`);

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
-- Indexes for table `core_sitesettings`
--
ALTER TABLE `core_sitesettings`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `core_oldpaper`
--
ALTER TABLE `core_oldpaper`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `core_project`
--
ALTER TABLE `core_project`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `core_sitesettings`
--
ALTER TABLE `core_sitesettings`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

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
  ADD CONSTRAINT `core_blog_author_id_1575e3e5_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `fk_uploaded_by` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`);

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
