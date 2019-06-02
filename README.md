# newspaper.hasname.com

## Database

    CREATE TABLE `posts` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `url` varchar(255) NOT NULL,
      `title` varchar(255) NOT NULL,
      `content` text NOT NULL,
      `fingerprint` binary(32) NOT NULL,
      `claimed_at` int(10) unsigned NOT NULL,
      `created_at` int(10) unsigned NOT NULL,
      `updated_at` int(10) unsigned NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE KEY `url` (`url`,`fingerprint`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

## License

See [LICENSE](LICENSE).
