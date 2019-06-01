# newspaper.hasname.com

## Database

    CREATE TABLE posts (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, url VARCHAR(255) NOT NULL, title VARCHAR(255) NOT NULL, content TEXT NOT NULL, fingerprint BINARY(32) NOT NULL, claimed_at INT UNSIGNED NOT NULL, created_at INT UNSIGNED NOT NULL, updated_at INT UNSIGNED NOT NULL);

## License

See [LICENSE](LICENSE).
